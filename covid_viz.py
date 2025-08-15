import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use a consistent plot style
sns.set(style="whitegrid")

# 1. Fetch data from a public API (COVID-19 data from disease.sh)
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

# 2. Check if the response is successful
if response.status_code != 200:
    print("Failed to fetch data from API")
    exit()

data = response.json()

# 3. Convert JSON data to a Pandas DataFrame
df = pd.json_normalize(data)

# 4. Select relevant columns for visualization
df = df[["country", "cases", "deaths", "recovered", "population"]]

# 5. Sort and get top 10 countries by case count
top10 = df.sort_values(by="cases", ascending=False).head(10)

# 6. Plot total cases by country
plt.figure(figsize=(12, 6))
sns.barplot(x="cases", y="country", data=top10, palette="Reds_r")
plt.title("Top 10 Countries by COVID-19 Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# 7. Plot comparison of cases, deaths, and recoveries
top10_melted = top10.melt(id_vars="country", value_vars=["cases", "deaths", "recovered"],
                          var_name="Type", value_name="Count")

plt.figure(figsize=(12, 6))
sns.barplot(x="Count", y="country", hue="Type", data=top10_melted)
plt.title("COVID-19 Cases, Deaths, and Recoveries (Top 10 Countries)")
plt.xlabel("Count")
plt.ylabel("Country")
plt.legend(title="Metric")
plt.tight_layout()
plt.show()

