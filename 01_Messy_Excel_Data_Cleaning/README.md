# Messy Excel Data Cleaning and Reporting Automation

This project demonstrates how Python can be used to clean a messy Excel sales file and transform it into clean, dashboard ready reporting outputs.

The project simulates a real business scenario where sales order data contains inconsistent formatting, duplicate rows, missing values, mixed date formats, messy text fields, currency symbols, percentage fields, and invalid entries.

Python is used to automate the cleaning process, validate the data, create summary tables, and export clean files that can be used in Power BI, Excel, Amazon QuickSight, or other reporting tools.

---

## Project Preview

### Total Net Revenue by Region

<img src="images/total_net_revenue_by_region.png" width="900">

### Total Net Revenue by Product Category

<img src="images/total_net_revenue_by_category.png" width="900">

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

## Files

| File or Folder | Description |
|---|---|
| `notebooks/01_messy_excel_data_cleaning.ipynb` | Main Jupyter Notebook with cleaning workflow |
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
