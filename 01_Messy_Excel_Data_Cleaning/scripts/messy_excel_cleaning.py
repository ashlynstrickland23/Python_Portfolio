"""
Messy Excel Data Cleaning and Reporting Automation

This script creates a messy Excel style sales dataset, cleans it with Python,
creates dashboard ready summary tables, and saves clean outputs for reporting.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def create_project_folders(project_root):
    raw_path = project_root / "data" / "raw"
    cleaned_path = project_root / "data" / "cleaned"
    image_path = project_root / "images"

    raw_path.mkdir(parents=True, exist_ok=True)
    cleaned_path.mkdir(parents=True, exist_ok=True)
    image_path.mkdir(parents=True, exist_ok=True)

    return raw_path, cleaned_path, image_path


def create_messy_dataset(raw_path):
    np.random.seed(42)

    num_rows = 500

    customers = [f"Customer {i}" for i in range(1, 151)]
    regions = ["South", "West", "Midwest", "Northeast", "sOUTH", " west ", None]
    categories = ["Technology", "Furniture", "Office Supplies", "tech", "FURNITURE", None]
    sales_reps = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", None]

    messy_data = pd.DataFrame({
        "Order ID": np.arange(1001, 1001 + num_rows),
        "Customer Name": np.random.choice(customers, num_rows),
        "Order Date": np.random.choice(
            ["2025-01-05", "01/15/2025", "2025/02/10", "March 3 2025", "bad date", None],
            num_rows
        ),
        "Region ": np.random.choice(regions, num_rows),
        "Product Category": np.random.choice(categories, num_rows),
        "Sales Rep": np.random.choice(sales_reps, num_rows),
        "Revenue": np.random.choice(
            ["$1,200.50", "$850", "300", "$2,450.75", "missing", None],
            num_rows
        ),
        "Quantity": np.random.choice([1, 2, 3, 4, 5, "two", None], num_rows),
        "Discount": np.random.choice(["10%", "5%", "0%", "15%", None], num_rows),
        "Status": np.random.choice(["Complete", "complete", "Completed", "Pending", "pending", None], num_rows)
    })

    duplicates = messy_data.sample(25, random_state=42)
    messy_data = pd.concat([messy_data, duplicates], ignore_index=True)

    raw_file = raw_path / "messy_sales_orders.xlsx"
    messy_data.to_excel(raw_file, index=False)

    return raw_file


def clean_sales_data(raw_file):
    df = pd.read_excel(raw_file)
    clean_df = df.copy()

    clean_df.columns = (
        clean_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    clean_df["region"] = (
        clean_df["region"]
        .astype("string")
        .str.strip()
        .str.title()
        .replace({"Nan": "Unknown", "<NA>": "Unknown"})
        .fillna("Unknown")
    )

    clean_df["product_category"] = (
        clean_df["product_category"]
        .astype("string")
        .str.strip()
        .str.title()
        .replace({
            "Tech": "Technology",
            "Nan": "Unknown",
            "<NA>": "Unknown"
        })
        .fillna("Unknown")
    )

    clean_df["sales_rep"] = (
        clean_df["sales_rep"]
        .astype("string")
        .str.strip()
        .str.title()
        .replace({"Nan": "Unknown", "<NA>": "Unknown"})
        .fillna("Unknown")
    )

    clean_df["status"] = (
        clean_df["status"]
        .astype("string")
        .str.strip()
        .str.title()
        .replace({
            "Complete": "Completed",
            "Nan": "Unknown",
            "<NA>": "Unknown"
        })
        .fillna("Unknown")
    )

    clean_df["revenue"] = (
        clean_df["revenue"]
        .astype("string")
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace({"missing": np.nan, "None": np.nan, "<NA>": np.nan})
    )

    clean_df["revenue"] = pd.to_numeric(clean_df["revenue"], errors="coerce")

    clean_df["quantity"] = clean_df["quantity"].replace({"two": 2})
    clean_df["quantity"] = pd.to_numeric(clean_df["quantity"], errors="coerce")

    clean_df["discount"] = (
        clean_df["discount"]
        .astype("string")
        .str.replace("%", "", regex=False)
        .str.strip()
    )

    clean_df["discount"] = pd.to_numeric(clean_df["discount"], errors="coerce") / 100
    clean_df["order_date"] = pd.to_datetime(clean_df["order_date"], errors="coerce")

    quality_summary = pd.DataFrame({
        "column_name": clean_df.columns,
        "missing_values": clean_df.isna().sum().values,
        "missing_percent": (clean_df.isna().mean().values * 100).round(2),
        "data_type": clean_df.dtypes.astype(str).values
    })

    clean_df = clean_df.drop_duplicates()

    clean_df["revenue"] = clean_df["revenue"].fillna(clean_df["revenue"].median())
    clean_df["quantity"] = clean_df["quantity"].fillna(clean_df["quantity"].median())
    clean_df["discount"] = clean_df["discount"].fillna(0)
    clean_df["order_date"] = clean_df["order_date"].fillna(pd.Timestamp("2025-01-01"))

    clean_df["net_revenue"] = clean_df["revenue"] * (1 - clean_df["discount"])

    return clean_df, quality_summary


def create_summary_tables(clean_df):
    summary_by_region = (
        clean_df
        .groupby("region", as_index=False)
        .agg(
            total_orders=("order_id", "count"),
            total_revenue=("revenue", "sum"),
            total_net_revenue=("net_revenue", "sum"),
            average_order_value=("net_revenue", "mean"),
            total_quantity=("quantity", "sum")
        )
        .sort_values("total_net_revenue", ascending=False)
    )

    summary_by_category = (
        clean_df
        .groupby("product_category", as_index=False)
        .agg(
            total_orders=("order_id", "count"),
            total_net_revenue=("net_revenue", "sum"),
            average_order_value=("net_revenue", "mean"),
            total_quantity=("quantity", "sum")
        )
        .sort_values("total_net_revenue", ascending=False)
    )

    summary_by_status = (
        clean_df
        .groupby("status", as_index=False)
        .agg(
            total_orders=("order_id", "count"),
            total_net_revenue=("net_revenue", "sum")
        )
        .sort_values("total_orders", ascending=False)
    )

    summary_by_month = (
        clean_df
        .assign(order_month=clean_df["order_date"].dt.to_period("M").astype(str))
        .groupby("order_month", as_index=False)
        .agg(
            total_orders=("order_id", "count"),
            total_net_revenue=("net_revenue", "sum")
        )
        .sort_values("order_month")
    )

    return summary_by_region, summary_by_category, summary_by_status, summary_by_month


def save_outputs(clean_df, quality_summary, summary_by_region, summary_by_category, summary_by_status, summary_by_month, cleaned_path):
    clean_df.to_csv(cleaned_path / "cleaned_sales_orders.csv", index=False)
    quality_summary.to_csv(cleaned_path / "data_quality_summary.csv", index=False)
    summary_by_region.to_csv(cleaned_path / "summary_by_region.csv", index=False)
    summary_by_category.to_csv(cleaned_path / "summary_by_category.csv", index=False)
    summary_by_status.to_csv(cleaned_path / "summary_by_status.csv", index=False)
    summary_by_month.to_csv(cleaned_path / "summary_by_month.csv", index=False)


def save_visuals(summary_by_region, summary_by_category, image_path):
    plt.figure(figsize=(10, 6))
    plt.bar(summary_by_region["region"], summary_by_region["total_net_revenue"])
    plt.title("Total Net Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Net Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(image_path / "total_net_revenue_by_region.png", dpi=300, bbox_inches="tight")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(summary_by_category["product_category"], summary_by_category["total_net_revenue"])
    plt.title("Total Net Revenue by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Total Net Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(image_path / "total_net_revenue_by_category.png", dpi=300, bbox_inches="tight")
    plt.close()


def main():
    project_root = Path(__file__).resolve().parents[1]

    raw_path, cleaned_path, image_path = create_project_folders(project_root)

    raw_file = create_messy_dataset(raw_path)

    clean_df, quality_summary = clean_sales_data(raw_file)

    summary_by_region, summary_by_category, summary_by_status, summary_by_month = create_summary_tables(clean_df)

    save_outputs(
        clean_df,
        quality_summary,
        summary_by_region,
        summary_by_category,
        summary_by_status,
        summary_by_month,
        cleaned_path
    )

    save_visuals(summary_by_region, summary_by_category, image_path)

    print("Messy Excel cleaning project completed.")
    print("Raw file:", raw_file)
    print("Cleaned outputs:", cleaned_path)
    print("Images:", image_path)


if __name__ == "__main__":
    main()
