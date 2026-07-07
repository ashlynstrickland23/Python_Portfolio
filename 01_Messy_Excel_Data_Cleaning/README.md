# Messy Excel Data Cleaning and Reporting Automation

This project demonstrates how Python can be used to clean a messy Excel sales file and transform it into clean, dashboard ready reporting outputs.

The project simulates a real business scenario where sales order data contains inconsistent formatting, duplicate rows, missing values, mixed date formats, messy text fields, currency symbols, percentage fields, and invalid entries.

Python is used to automate the cleaning process, validate the data, create summary tables, export clean files, and create visuals that can support reporting in Power BI, Excel, Amazon QuickSight, or other business intelligence tools.

---

## Project Preview

### Total Net Revenue by Region

<img src="images/total_net_revenue_by_region.png" width="900">

### Total Net Revenue by Product Category

<img src="images/total_net_revenue_by_category.png" width="900">

---

## View the Python Work

| File | Description |
|---|---|
| [Jupyter Notebook](notebooks/01_messy_excel_data_cleaning.ipynb) | Full notebook with code, outputs, tables, and visuals |
| [Python Script](scripts/messy_excel_cleaning.py) | Clean script version of the full data cleaning workflow |

---

## Business Problem

Messy Excel files are common in business reporting. Before a dashboard can be built, the data often needs to be cleaned, standardized, validated, and reshaped.

This project answers the question:

> How can Python automate the process of turning a messy Excel sales file into clean reporting tables?

---

## Dataset

The raw dataset is a simulated messy sales order file.

It includes fields such as:

* Order ID
* Customer Name
* Order Date
* Region
* Product Category
* Sales Rep
* Revenue
* Quantity
* Discount
* Status

The raw file intentionally includes common data quality issues such as:

* Duplicate rows
* Blank values
* Mixed date formats
* Currency symbols in numeric fields
* Percentage symbols in discount fields
* Inconsistent capitalization
* Extra spaces in text fields
* Invalid values like `missing`, `bad date`, and `two`

---

## Workflow

The notebook follows this process:

1. Import Python libraries
2. Create a simulated messy Excel file
3. Load the raw Excel file
4. Clean column names
5. Standardize text fields
6. Clean currency values
7. Convert quantity fields to numeric values
8. Convert discount percentages
9. Convert order dates
10. Create a data quality summary
11. Remove duplicate records
12. Fill missing values
13. Create net revenue calculation
14. Build dashboard ready summary tables
15. Export cleaned CSV files
16. Save visual outputs

---

## Python Code Preview

### Cleaning Column Names

```python
clean_df.columns = (
    clean_df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
```

### Cleaning Revenue Values

```python
clean_df["revenue"] = (
    clean_df["revenue"]
    .astype("string")
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

clean_df["revenue"] = pd.to_numeric(clean_df["revenue"], errors="coerce")
```

### Creating a Dashboard Ready Summary Table

```python
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
```

---

## Sample Results

The Python workflow creates dashboard ready summary tables from the cleaned sales order dataset. These outputs can be used in Power BI, Excel, Amazon QuickSight, or other reporting tools.

### Revenue Summary by Region

| Region | Total Orders | Total Revenue | Total Net Revenue | Average Order Value | Total Quantity |
|---|---:|---:|---:|---:|---:|
| West | 145 | $183,510.25 | $173,569.51 | $1,197.03 | 408 |
| South | 143 | $181,307.25 | $170,281.20 | $1,190.78 | 416 |
| Unknown | 77 | $96,628.50 | $90,666.88 | $1,177.49 | 218 |
| Midwest | 74 | $84,875.50 | $79,621.50 | $1,075.97 | 211 |
| Northeast | 61 | $78,575.25 | $73,536.04 | $1,205.51 | 166 |

### Revenue Summary by Product Category

| Product Category | Total Orders | Total Net Revenue | Average Order Value | Total Quantity |
|---|---:|---:|---:|---:|
| Furniture | 170 | $201,682.46 | $1,186.37 | 487 |
| Technology | 163 | $194,058.25 | $1,190.54 | 454 |
| Office Supplies | 82 | $98,584.19 | $1,202.25 | 245 |
| Unknown | 85 | $93,350.23 | $1,098.24 | 233 |

### Revenue Summary by Order Status

| Status | Total Orders | Total Net Revenue |
|---|---:|---:|
| Completed | 257 | $307,534.56 |
| Pending | 168 | $193,799.09 |
| Unknown | 75 | $86,341.47 |

### Monthly Revenue Summary

| Order Month | Total Orders | Total Net Revenue |
|---|---:|---:|
| 2025 01 | 346 | $397,421.71 |
| 2025 02 | 80 | $99,764.77 |
| 2025 03 | 74 | $90,488.64 |

### Data Quality Summary

| Column Name | Missing Values | Missing Percent | Data Type |
|---|---:|---:|---|
| order_id | 0 | 0.0% | int64 |
| customer_name | 0 | 0.0% | object |
| order_date | 191 | 36.38% | datetime64[ns] |
| region | 0 | 0.0% | string |
| product_category | 0 | 0.0% | string |
| sales_rep | 0 | 0.0% | string |
| revenue | 182 | 34.67% | Float64 |
| quantity | 65 | 12.38% | float64 |
| discount | 110 | 20.95% | Float64 |
| status | 0 | 0.0% | string |

---

## Files

| File or Folder | Description |
|---|---|
| `notebooks/01_messy_excel_data_cleaning.ipynb` | Main Jupyter Notebook with cleaning workflow |
| `scripts/messy_excel_cleaning.py` | Python script version of the project |
| `data/raw/messy_sales_orders.xlsx` | Simulated messy Excel source file |
| `data/cleaned/cleaned_sales_orders.csv` | Cleaned transaction level dataset |
| `data/cleaned/data_quality_summary.csv` | Data quality summary by column |
| `data/cleaned/summary_by_region.csv` | Dashboard ready region summary |
| `data/cleaned/summary_by_category.csv` | Dashboard ready category summary |
| `data/cleaned/summary_by_status.csv` | Dashboard ready order status summary |
| `data/cleaned/summary_by_month.csv` | Dashboard ready monthly summary |
| `images/` | Saved project visuals |

---

## Tools Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Excel file automation
* GitHub

---

## Skills Demonstrated

* Data cleaning
* Excel file automation
* Missing value handling
* Duplicate detection
* Date conversion
* Currency field cleaning
* Percentage field cleaning
* Text standardization
* Data quality reporting
* Dashboard ready dataset creation
* Business reporting automation
* Data visualization

---

## Outputs Created

This project produces several cleaned and reporting ready outputs:

* Cleaned sales order dataset
* Data quality summary
* Revenue summary by region
* Revenue summary by product category
* Revenue summary by order status
* Revenue summary by month
* Chart image for revenue by region
* Chart image for revenue by product category

---

## Business Value

This project shows how Python can reduce manual Excel cleanup work and create reliable reporting outputs.

Instead of cleaning the same messy spreadsheet by hand every month, the process can be automated and reused. This type of workflow supports faster dashboard development, cleaner reporting, and more accurate business analysis.

---

## Portfolio Note

This project is part of my Python Business Analytics Portfolio. It supports my broader portfolio work in Power BI, SQL, PostgreSQL, and business intelligence reporting.

[Back to Main Python Portfolio](../README.md)
