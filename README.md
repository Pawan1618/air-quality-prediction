# air-quality-prediction
📂 Dataset Description

The dataset includes the following columns:

City – Name of the city where measurement is taken

Date – Timestamp of measurement (daily/hourly depending on source)

PM2.5 – Particulate Matter 2.5 micrometers (µg/m³)

PM10 – Particulate Matter 10 micrometers (µg/m³)

NO – Nitric Oxide (µg/m³)

NO2 – Nitric Dioxide (µg/m³)

NOx – Any Nitric Oxide compound (ppb)

NH3 – Ammonia (µg/m³)

CO – Carbon Monoxide (mg/m³)

SO2 – Sulphur Dioxide (µg/m³)

🧹 Data Cleaning Steps

Duplicate removal – Removed duplicate records.

Column standardization – Cleaned column names (lowercase, snake_case).

Date parsing – Converted Date column into proper datetime format.

Missing values – Handled [null], NaN, and invalid entries:

Replaced missing pollutant values with median imputation.

Numeric conversion – Converted pollutant columns to float.

📊 Exploratory Data Analysis (EDA)

The following analysis was performed:

Summary statistics for pollutants.

Missing values heatmap to identify data quality issues.

Histograms of pollutant distributions.

Correlation heatmap to analyze relationships between pollutants.

City-wise comparison (Top 10 cities by PM2.5).

Time series trends (e.g., PM2.5 levels over time).
