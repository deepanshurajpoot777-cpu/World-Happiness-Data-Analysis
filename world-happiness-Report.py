import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("world happiness Report.csv")

df=df.dropna(subset=["Region","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Country"])

type_Region=df["Region"].value_counts()
plt.figure(figsize=(8,8))
plt.pie(type_Region.values,labels=type_Region.index,autopct="%1.1f%%",startangle=90)
plt.title("Distribution of contries by Region")
plt.tight_layout()
plt.savefig("Region_vs_countries.png")
plt.show()

region_avg=df.groupby("Region")["Happiness Score"].mean()
plt.figure(figsize=(10,6))
plt.bar(region_avg.index,region_avg.values,color="skyblue")
plt.xticks(rotation=45)
plt.xlabel("Region")
plt.ylabel("Average Happines Score")
plt.title("Average Happines score by Region")
plt.tight_layout()
plt.savefig("Region_vs_avg happines score.png")
plt.show()

plt.hist(df["Happiness Score"],bins=10,edgecolor="black",color="skyblue")
plt.xlabel("Happiness Score")
plt.ylabel("Number of Countries")
plt.title("Distribution of Happiness Score")
plt.savefig("Happiness_score_vs_country.png")
plt.show()

plt.scatter(df["Economy (GDP per Capita)"],df["Happiness Score"])
plt.xlabel("GDP Per Capita")
plt.ylabel("Happiness Score")
plt.title("GDP VS Happines Score")
plt.savefig("GDP_vs_Happiness Score.png")
plt.show()

top10=df.nlargest(10,"Happiness Score")
plt.figure(figsize=(8,6))
plt.barh(top10["Country"],top10["Happiness Score"],color="teal")

plt.xlabel("Happiness SCore")
plt.ylabel("Country")
plt.title("TOP 10 Happiest Country")
plt.savefig("top-10-happiest-country.png")
plt.show()