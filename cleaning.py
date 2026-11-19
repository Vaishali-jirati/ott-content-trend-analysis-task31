import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")

df.to_csv("netflix_cleaned.csv", index=False)

print("Cleaning complete! Total rows:", len(df))