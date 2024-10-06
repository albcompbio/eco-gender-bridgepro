import pandas as pd
import plotly.express as px
import numpy as np

# Load the data with the correct encoding
countries_df = pd.read_csv('countries.csv', encoding='utf-8')
data1_df = pd.read_csv('data1.csv', encoding='utf-8')
data2_df = pd.read_csv('data2.csv', encoding='latin1')
data3_df = pd.read_csv('data3.csv', encoding='utf-8')
data4_df = pd.read_csv('data4.csv', encoding='utf-8')

# Adjust column names for merging
countries_df.rename(columns={'name': 'Country'}, inplace=True)

# Merge the dataframes
merged_df = data1_df.merge(data2_df, on='Country', how='outer')
merged_df = merged_df.merge(data3_df, on='Country', how='outer')
merged_df = merged_df.merge(data4_df, left_on='Country', right_on='Country Name', how='outer')

# Convert columns to numeric, coercing errors to NaN
numeric_columns = ['CO2Emissions', 'YearlyChange', 'Percapita', 'Population', 'LifeExpectancy',
                   'Human_development', 'GII', 'Rank', 'Maternal_mortality', 'Adolescent_birth_rate',
                   'Seats_parliament', 'F_secondary_educ', 'M_secondary_educ', 'F_Labour_force', 'M_Labour_force']

for col in numeric_columns:
    merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')

# Fill missing values with column means
merged_df[numeric_columns] = merged_df[numeric_columns].fillna(merged_df[numeric_columns].mean())

# Add quotes for specific countries
merged_df['Quote'] = ''

# Add quotes for specific countries with newlines for better formatting
quotes = {
    'Thailand': "If you are invisible in everyday life your needs will not be thought of,\n"
                "let alone addressed in a crisis situation - Matcha Phorn-In, UN Women",
    
    'Brazil': "In the Amazon, defending human rights means fighting for the survival of people\n"
              "and the rainforest every day, but there is no hierarchy between agendas.\n"
              "To finance social movements in the Amazon is to finance the survival of these communities,\n"
              "these people, and the rainforest. - Dandara Rudsan, UN Women",
    
    'Nigeria': "My future ambition is to become a medical doctor because we don't have enough female medical doctors.\n"
               "Mostly if you go to our hospitals, you find out that most of the specialist doctors are male. - Sa'idu, CNN",
    
    'Bangladesh': "I got married early because natural disasters are happening frequently now,\n"
                  "and our father cannot afford our expenses - Marufa Khatun, CNN",
    
    'Kenya': "Women hold the key to Climate's Future - Wangari Maathai, Wikipedia",
    
    'Philippines': "Climate change threatens my community's traditional livelihoods in the Philippines.\n"
                   "As a gay man, I'm more likely to be displaced. - Ging Cristobal, Rappler Interview",
    
    'Canada': "Climate change affects Indigenous LGBTQ+ communities in Canada.\n"
              "I've lost traditional lands and culture. - Joshua Whitehead, The Walrus",
    
    'India': "Whether it be from being displaced, experiencing drought, or from crops \n"
              "drying up and not having access to running water\n"
             "women are bearing the brunt of these issues. - Megha Desai, CNBC",
    
    'El Salvador': "I fight because I know that without water we cannot live.\n"
                   "I do this work for the love of my community, for my granddaughters\n"
                   "so that they can live in a healthy world. - Reyna Ortiz, Global Fund for Women",
    
    'Peru': "Women and girls experience disproportionate effects of climate change globally.\n"
            "Women and girls are often left out of school or unable to work.\n"
            "Many women and girls are dependent on their partners, increasing the risk of violence. - Esmeralda, OHCHR",
    
    'Honduras': "Mother Nature—militarized, fenced-in, poisoned—demands that we take action.\n"
                "- Berta Cáceres, Global Fund for Women",
    
    'Southern Europe': "As a young woman from Southern Europe increasingly experiencing extreme climate events\n"
                       "including disastrous floods, heat waves causing fires, and thunderstorms\n"
                       "I have witnessed the unequal impact of climate change.\n"
                       "This disproportionately affects vulnerable and marginalized groups. - Marta Pompii, ActionAid",
    
    'California': "There's greater risk of displacement, higher odds of being injured or killed during a natural disaster.\n"
                  "Prolonged drought can lead to early marriage or prostitution as women struggle to survive.\n"
                  "These dynamics are most acute under conditions of poverty. - Katherine Wilkilson, Wired"
}

# Safely assign quotes with newlines for better readability in hover data
for country, quote in quotes.items():
    merged_df.loc[merged_df['Country'] == country, 'Quote'] = quote


# Select key columns for visualization
selected_columns = ['Country', 'CO2Emissions', 'Adolescent_birth_rate', 'GII', 'LifeExpectancy',
                    'Human_development', 'F_Labour_force', 'M_Labour_force', 'Maternal_mortality', 'Quote']
selected_df = merged_df[selected_columns].copy()

# Function to format CO2 emissions for better readability
def format_emissions(value):
    if value >= 1e9:
        return f"{value / 1e9:.2f}B"
    elif value >= 1e6:
        return f"{value / 1e6:.2f}M"
    else:
        return f"{value:.2f}"

# Apply the function to create a new 'FormattedCO2Emissions' column
selected_df['FormattedCO2Emissions'] = selected_df['CO2Emissions'].apply(format_emissions)

# Calculate the logarithmic values of CO2 emissions for better color scaling
selected_df['LogCO2Emissions'] = np.log10(selected_df['CO2Emissions'].replace(0, np.nan))


# Create a choropleth map using the log-transformed CO2 emissions for color scaling
fig = px.choropleth(
    selected_df,
    locations='Country',
    locationmode='country names',
    color='LogCO2Emissions',  # Use the log-transformed CO2 emissions for color
    hover_name='Country',
    hover_data={
        'FormattedCO2Emissions': True,  # Show formatted emissions in hover
        'Adolescent_birth_rate': True,
        'GII': True,
        'LifeExpectancy': True,
        'Human_development': True,
        'F_Labour_force': True,
        'M_Labour_force': True,
        'Maternal_mortality': True,
        'Quote': True
    },
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Eco-Gender Bridge: Bridging the Gap, Empowering Change',
    labels={'LogCO2Emissions': 'Log CO2 Emissions'}
)

# Update layout for better visualization
fig.update_geos(projection_type="natural earth")
fig.update_layout(
    coloraxis=dict(
        colorscale="Viridis",  # Switch to a different color scale
        colorbar_title="CO2 Emissions"
    )
)

# Save the plot as an HTML file
fig.write_html("eco_gender_bridge.html")

# Display the map in a browser or interactive environment
fig.show()
