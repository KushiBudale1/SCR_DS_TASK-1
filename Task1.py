import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"API_SP.POP.TOTL_DS2_en_csv_v2_3369961.csv", skiprows=4)
print(data.head())
print(data.columns)

# Plotting the histogram
population_2023 = data['2023'].dropna()
plt.figure(figsize=(10, 6))
plt.hist(population_2023, bins=20, color='brown', edgecolor='black')
plt.title('Population Distribution Across Countries in 2023')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()

# Process data and calculate mean population by year
years = [str(year) for year in range(1999, 2020)]
if all(year in data.columns for year in years):
    mean_population_by_year = data[years].mean()
    fig, axes = plt.subplots(2, 1, figsize=(8, 10))

    # Bar Chart: Average Population by Year
    sns.barplot(x=mean_population_by_year.index, y=mean_population_by_year, palette="husl", ax=axes[0], edgecolor='black')
    axes[0].set_title('Average Population by Year (Bar Chart)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Average Population')
    axes[0].grid(True)

    # Histogram: Distribution of Average Population
    sns.histplot(mean_population_by_year, kde=False, color='green', edgecolor='black', ax=axes[1])
    axes[1].set_title('Distribution of Average Population (Histogram)')
    axes[1].set_xlabel('Average Population')
    axes[1].set_ylabel('Frequency')
    axes[1].grid(True)

    fig.subplots_adjust(hspace=1)
    plt.tight_layout()
    plt.show()
else:
    print("Year columns not found in the dataset.")
