Overview:
This project visualizes global CO2 emissions along with several gender and development-related indicators, combining environmental and social data to highlight disparities across countries. The visualization is done using a choropleth map that allows users to explore how countries perform in terms of CO2 emissions, gender inequality, labor force participation, and maternal health, while also presenting quotes that offer perspectives from affected regions.

Requirements:
Python 3.x
Pandas: for data manipulation.
Plotly Express: for creating the interactive choropleth map.
NumPy: for numerical operations (specifically for logarithmic transformation).
Data:
The script loads multiple datasets (countries.csv, data1.csv, data2.csv, data3.csv, and data4.csv) that contain information on various indicators such as:

CO2 emissions
Gender inequality index (GII)
Labor force participation (male and female)
Adolescent birth rate
Maternal mortality
Life expectancy
Population
Additionally, quotes related to gender, climate change, and social justice are included for specific countries, offering context for the data.

README: Eco-Gender Bridge Data Visualization
Overview:
This project visualizes global CO2 emissions along with several gender and development-related indicators, combining environmental and social data to highlight disparities across countries. The visualization is done using a choropleth map that allows users to explore how countries perform in terms of CO2 emissions, gender inequality, labor force participation, and maternal health, while also presenting quotes that offer perspectives from affected regions.

Requirements:
Python 3.x
Pandas: for data manipulation.
Plotly Express: for creating the interactive choropleth map.
NumPy: for numerical operations (specifically for logarithmic transformation).
Data:
The script loads multiple datasets (countries.csv, data1.csv, data2.csv, data3.csv, and data4.csv) that contain information on various indicators such as:

CO2 emissions
Gender inequality index (GII)
Labor force participation (male and female)
Adolescent birth rate
Maternal mortality
Life expectancy
Population
Additionally, quotes related to gender, climate change, and social justice are included for specific countries, offering context for the data.

Data Processing:
1)Data Loading: Multiple CSV files are loaded, and one of the columns ('name') in countries.csv is renamed to match the 'Country' column in other datasets for merging.
2)Merging Data: The dataframes are merged on the Country field, and missing values are handled using an outer join to ensure all countries are included.
3)Numerical Conversion: Certain columns representing numeric data (e.g., CO2 emissions, population, and development indicators) are converted to numeric types, and any non-convertible values are coerced to NaN. Missing values are then replaced with the mean value of the corresponding columns.
4)Quotes Assignment: Predefined quotes for specific countries are assigned to a Quote column in the merged data for display in the hover tooltip of the choropleth map.
5)CO2 Emissions Formatting: A custom function format_emissions is used to format CO2 emissions into readable formats (e.g., millions or billions), and the logarithm of CO2 emissions is calculated to scale the color intensity of the map more effectively.

Visualization:
Choropleth Map: A choropleth map is generated using Plotly Express. The map displays countries shaded based on their log-transformed CO2 emissions. Users can hover over countries to view additional information like:
CO2 emissions (formatted for readability)
Adolescent birth rate
Gender Inequality Index (GII)
Labor force participation (for males and females)
Maternal mortality rate
Life expectancy
Quotes from individuals in certain regions
The map uses the Viridis color scale and a natural Earth projection for the globe.
