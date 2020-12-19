# import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the CSV files and create the DataFrames:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Paste print code here:
print(user_data.head(15))

# Paste merge code here:
new_df = pd.merge(user_data, pop_data)
print(new_df.head(15))

# Paste location code here:
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"
print(new_df.head(15))

# Paste histogram code:
age = new_df["age"]
sns.distplot(age)

plt.show()

# Paste mean age location code:
location_mean_age = new_df.groupby("location").age.mean()

print(location_mean_age)

# Paste barplot code:
plt.close()
sns.barplot(
    data = new_df,
    x = "location",
    y = "age"
)

plt.show()

# Paste violinplot code:
plt.close()
sns.violinplot(x = "location", y = "age", data = new_df)

plt.show()

# Paste code for scatter plot:
x = new_df["population_proper"]
y = new_df["age"]

plt.scatter(x, y, alpha=0.5)

# Paste code for linear regression:
sns.regplot(x="population_proper", y="age", data = new_df)

# Show plot
plt.show()

