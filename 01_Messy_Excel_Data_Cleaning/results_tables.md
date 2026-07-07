---

## Sample Results

The Python workflow creates dashboard ready summary tables from the cleaned sales order dataset. These outputs can be used in Power BI, Excel, Amazon QuickSight, or other reporting tools.

### Revenue Summary by Region

| region | total_orders | total_revenue | total_net_revenue | average_order_value | total_quantity |
| --- | --- | --- | --- | --- | --- |
| West | 145 | $183,510.25 | $173,569.51 | $1,197.03 | 408 |
| South | 143 | $181,307.25 | $170,281.20 | $1,190.78 | 416 |
| Unknown | 77 | $96,628.50 | $90,666.88 | $1,177.49 | 218 |
| Midwest | 74 | $84,875.50 | $79,621.50 | $1,075.97 | 211 |
| Northeast | 61 | $78,575.25 | $73,536.04 | $1,205.51 | 166 |

### Revenue Summary by Product Category

| product_category | total_orders | total_net_revenue | average_order_value | total_quantity |
| --- | --- | --- | --- | --- |
| Furniture | 170 | $201,682.46 | $1,186.37 | 487 |
| Technology | 163 | $194,058.25 | $1,190.54 | 454 |
| Office Supplies | 82 | $98,584.19 | $1,202.25 | 245 |
| Unknown | 85 | $93,350.23 | $1,098.24 | 233 |

### Revenue Summary by Order Status

| status | total_orders | total_net_revenue |
| --- | --- | --- |
| Completed | 257 | $307,534.56 |
| Pending | 168 | $193,799.09 |
| Unknown | 75 | $86,341.47 |

### Monthly Revenue Summary

| order_month | total_orders | total_net_revenue |
| --- | --- | --- |
| 2025-01 | 346 | $397,421.71 |
| 2025-02 | 80 | $99,764.77 |
| 2025-03 | 74 | $90,488.64 |

### Data Quality Summary

| column_name | missing_values | missing_percent | data_type |
| --- | --- | --- | --- |
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

## Results Created by Python

This project produces reusable reporting outputs instead of only creating charts.

| Output | Description |
|---|---|
| Cleaned sales order data | Transaction level dataset after cleaning |
| Data quality summary | Missing values, data types, and quality checks |
| Region summary | Orders, revenue, net revenue, average order value, and quantity by region |
| Category summary | Sales performance by product category |
| Status summary | Sales performance by order status |
| Monthly summary | Monthly order and revenue trend table |
| Chart images | Saved visuals for README and portfolio preview |
