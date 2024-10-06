import plotly.express as px
import pandas as pd

# Load the data again to ensure it's fresh
co2_data = pd.read_csv('data1.csv')

# Create an improved interactive map with more data
fig_map = px.choropleth(
    co2_data,
    locations='Code',
    color='CO2Emissions',
    hover_name='Country',
    hover_data=['Percapita', 'Population', 'LifeExpectancy'],
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Global CO2 Emissions with Additional Data',
    labels={'CO2Emissions': 'CO2 Emissions'}
)

# Update layout for better display
fig_map.update_geos(projection_type='natural earth')
fig_map.update_layout(margin={'r':0,'t':50,'l':0,'b':0})

# Save the improved map as HTML
fig_map.write_html('improved_interactive_co2_emissions_map.html')

print("Improved interactive map has been created and saved as 'improved_interactive_co2_emissions_map.html'.")
