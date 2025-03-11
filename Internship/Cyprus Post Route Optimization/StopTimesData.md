# Stop Times Data - Cyprus Post Route Optimization

## 📌 Overview
This section contains the **Stop Times** dataset, collected during real-world testing with postmen. The data represents the time spent at various stops during delivery routes, providing insights for optimizing postal operations and improving efficiency.

## 📂 Folder Contents
- `stop_times.csv` – The primary dataset containing timestamps and stop durations.
- `analysis_notebook.ipynb` – Jupyter Notebook used for in-depth analysis and visualization of stop time data.

## 📊 Data Description
The dataset consists of the following key columns:

| Column Name      | Description                                      |
|-----------------|--------------------------------------------------|
| `Stop_ID`       | Unique identifier for each stop                 |
| `Route_ID`      | Identifier for the route the stop belongs to    |
| `Arrival_Time`  | Time the postman arrived at the stop            |
| `Departure_Time`| Time the postman left the stop                  |
| `Duration`      | Time spent at the stop (calculated in minutes)  |
| `Latitude`      | Geographic latitude of the stop                 |
| `Longitude`     | Geographic longitude of the stop                |

## 🚀 Analysis & Findings
Key insights derived from the collected data:
- **Average Stop Time:** 📌 The average stop duration at each location.
- **Peak Time Analysis:** ⏰ Identification of the busiest periods in the route.
- **Route Efficiency:** 🛣️ Assessment of routes with excessive delays.
- **Optimization Strategies:** ✨ Recommendations for minimizing stop durations and improving overall delivery time.

## 📈 Visualizations
Visualizations enhance the understanding of stop time trends and delivery efficiency. Some key plots included:
- **Stop Duration Histogram:** Displays the distribution of stop times.
- **Route Efficiency Line Graph:** Compares efficiency across different routes.
- **Geospatial Heatmap:** Highlights clusters of long stop durations for optimization.

### 📍 Data Mappings & Insights
The following images showcase various aspects of the analysis:

#### 1. Raw Data Mapped Using Gmaps API
![image](https://github.com/user-attachments/assets/b893e9e0-4ebb-401a-835f-63042e15222b)

#### 2. Smoothed Data Representation
![image](https://github.com/user-attachments/assets/cfaac6a7-fe2e-4873-a023-6e08cc56adcb)

#### 3. Average and Standard Deviation Calculations & Plottings
![image](https://github.com/user-attachments/assets/dc4c71e5-5c83-4579-b734-67085cdecb27)
![image](https://github.com/user-attachments/assets/6ff24b11-0e4e-4a13-bd8e-307d09e10b1b)
![image](https://github.com/user-attachments/assets/d9e042b8-10d7-4c41-aa0e-2b5ccd56604e)
![image](https://github.com/user-attachments/assets/ad7d22ae-6b9b-49a3-8f11-d6ca351b86fc)

By analyzing these visualizations, we can better understand delivery patterns, pinpoint inefficiencies, and propose actionable improvements for optimizing postal routes.
