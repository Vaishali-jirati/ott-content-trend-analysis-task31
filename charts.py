import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Clean data load karein
df = pd.read_csv("netflix_cleaned.csv")
sns.set_theme(style="whitegrid")

# 1. Movies vs TV Shows
plt.figure(figsize=(6, 4))
type_counts = df["type"].value_counts()
plt.bar(
    type_counts.index,
    type_counts.values,
    color=["#E50914", "#221F1F"],
    width=0.45,
)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("1_movies_vs_tv_shows.png", dpi=150)
plt.close()

# 2. Top 10 Genres
plt.figure(figsize=(8, 5))
genres = (
    df["listed_in"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
    .sort_values()
)
plt.barh(genres.index, genres.values, color="#E50914")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("2_top_10_genres.png", dpi=150)
plt.close()

# 3. Release Trend by Year (2005-2021)
plt.figure(figsize=(8, 4.5))
trend = (
    df[df["release_year"] >= 2005]
    .groupby(["release_year", "type"])
    .size()
    .unstack(fill_value=0)
)
plt.plot(trend.index, trend["Movie"], marker="o", color="#E50914", label="Movie")
plt.plot(
    trend.index, trend["TV Show"], marker="s", color="#221F1F", label="TV Show"
)
plt.title("Content Release Trend by Year (2005–2021)")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend(title="Type")
plt.tight_layout()
plt.savefig("3_release_year_trend.png", dpi=150)
plt.close()

# 4. Top 10 Countries (Primary Country)
plt.figure(figsize=(8, 5))
primary_countries = df["country"].apply(lambda x: str(x).split(",")[0].strip())
top_c = (
    primary_countries[primary_countries != "Unknown"]
    .value_counts()
    .head(10)
    .sort_values()
)
plt.barh(top_c.index, top_c.values, color="#434343")
plt.title("Top 10 Primary Content Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("4_top_10_countries.png", dpi=150)
plt.close()

# 5. Top 8 Ratings
plt.figure(figsize=(7, 4.5))
top_r = df[df["rating"] != "Unknown"]["rating"].value_counts().head(8)
plt.bar(top_r.index, top_r.values, color="#E50914", alpha=0.85)
plt.title("Top 8 Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("5_top_ratings.png", dpi=150)
plt.close()

# 6. Movie Duration Distribution (Minutes)
plt.figure(figsize=(7, 4.5))
movies_df = df[df["type"] == "Movie"].copy()
movies_df["mins"] = pd.to_numeric(
    movies_df["duration"].str.replace(" min", "", regex=False), errors="coerce"
)
movies_df = movies_df.dropna(subset=["mins"])
plt.hist(
    movies_df["mins"], bins=25, color="#221F1F", alpha=0.85, edgecolor="white"
)
plt.title("Movie Duration Distribution (Minutes)")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("6_movie_duration.png", dpi=150)
plt.close()

print("charts are ready")