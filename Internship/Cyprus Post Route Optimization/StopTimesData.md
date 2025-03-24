# Route Optimization & Stop Time Analysis for Cyprus Post

## 📌 Overview
This document presents the analysis of postal collection routes for optimizing travel efficiency. The project involved:
- Collecting **GPS location data** from a mobile tracking application.
- Identifying **stop locations** where postmen spent time collecting letters.
- **Optimizing routes** to reduce travel time and increase efficiency.
- **Visualizing** real-world vs. optimized routes.
- **Data analysis performed using Python and Jupyter Notebook** for route optimization and statistical evaluation.

## 📂 Data Collection & Processing
### 💡 How the Data Was Collected
1. **GPS tracking** recorded the postman's location **every second**, storing **latitude, longitude, and timestamps**.
2. Stops were identified where **the postman remained stationary** near pillar boxes.
3. The collected data was processed to:
   - **Remove GPS noise** (minor deviations due to signal errors).
   - **Detect stops** based on time spent at a location.
   - **Compare real-world vs. optimized routes**.

### 📈 Dataset Structure
| Column Name      | Description                                      |
|-----------------|--------------------------------------------------|
| `Stop_ID`       | Unique identifier for each stop                 |
| `Route_ID`      | Identifier for the optimized route              |
| `Arrival_Time`  | Timestamp when the postman arrived at a stop    |
| `Departure_Time`| Timestamp when the postman left a stop          |
| `Duration`      | Time spent at the stop (minutes)                |
| `Latitude`      | Geographic latitude of the stop                 |
| `Longitude`     | Geographic longitude of the stop                |
| `Optimized_Route` | Suggested sequence for best efficiency       |

## 🌍 Route Visualization
### **1. Raw GPS Route**
- **First map**: Shows the **unprocessed route**, directly plotted from raw latitude-longitude data.
- **Dense and jagged**, as it captures every second of movement.
![image](https://github.com/user-attachments/assets/b893e9e0-4ebb-401a-835f-63042e15222b)

### **2. Smoothed GPS Route**
- **Second map**: A **cleaned version** of the route using data smoothing techniques.
- **Removes small deviations**, making analysis easier and more accurate.
![image](https://github.com/user-attachments/assets/cfaac6a7-fe2e-4873-a023-6e08cc56adcb)

## 🔍 Analysis & Findings
### **Stop Time Statistics**
- **Bar charts** illustrate:
  - **Average stop duration** across all locations.
  - **Standard deviation**, showing variation in stop times.
![image](https://github.com/user-attachments/assets/dc4c71e5-5c83-4579-b734-67085cdecb27)
![image](https://github.com/user-attachments/assets/ad7d22ae-6b9b-49a3-8f11-d6ca351b86fc)

- **Outlier detection**:
  - **Red points** in scatter plots show abnormally long stops.
  - Helps **identify inefficiencies** (e.g., delays due to traffic, manual errors, or unoptimized collection points).
![image](https://github.com/user-attachments/assets/6ff24b11-0e4e-4a13-bd8e-307d09e10b1b)
![image](https://github.com/user-attachments/assets/d9e042b8-10d7-4c41-aa0e-2b5ccd56604e)

### **Route Efficiency Evaluation**
- **Comparison of actual vs. optimized routes**:
  - Identifies **unnecessary detours**.
  - Evaluates **potential time savings** with optimized routing.
- **Recalculated stop times after adjustments**:
  - A second analysis after **removing outliers** gives a **more accurate efficiency estimate**.

## 🌟 Key Takeaways
- **Route Optimization:**
  - Reduces total collection time.
  - Minimizes unnecessary stops and improves efficiency.
- **Data Smoothing & Outlier Removal:**
  - Helps refine travel patterns for **better route planning**.
- **Visual Insights:**
  - Allow real-time tracking of collection patterns.
  - Support decision-making for **future route planning improvements**.

## 📚 Conclusion
This study successfully **demonstrates the power of GPS tracking and data-driven optimization** for postal route efficiency. The approach allows:
✅ **More efficient letter collection.**
✅ **Reduced operational costs.**
✅ **Better-informed route adjustments.**

By leveraging these insights and using **Python and Jupyter Notebook for data analysis**, postal operations can significantly **improve efficiency, save fuel, and reduce collection time**. 🚀

