import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the CSV file
file_path = 'covid_data.csv'  # Make sure this is in the same folder as the script
df = pd.read_csv(file_path)

# 2. Print first few rows to check data
print("Data preview:")
print(df.head())

# 3. Sort top countries by cases
top_countries = df.sort_values(by='cases', ascending=False).head(10)

# 4. Create a horizontal bar chart of cases
plt.figure(figsize=(12, 6))
sns.barplot(x='cases', y='country', data=top_countries, palette='Reds_r')
plt.title('Top 10 Countries by COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# 5. Compare cases, deaths, and recoveries
melted = top_countries.melt(
    id_vars='country',
    value_vars=['cases', 'deaths', 'recovered'],
    var_name='Type',
    value_name='Count'
)

# 6. Grouped bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='Count', y='country', hue='Type', data=melted)
plt.title('COVID-19 Cases, Deaths, and Recoveries (Top 10 Countries)')
plt.xlabel('Count')
plt.ylabel('Country')
plt.legend(title='Metric')
plt.tight_layout()
plt.show()



