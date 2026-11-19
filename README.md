# OTT Streaming Content Trend Analysis (Netflix Catalog)

End-to-end exploratory data analysis (EDA), SQL aggregation queries, visual charts, and a content strategy memo on the Netflix titles dataset (**8,807 titles**).

## Project Overview
This project examines catalog composition, release trends, genres, countries, audience ratings, and movie durations on Netflix to identify clear content and programming takeaways.

## Key Highlights
- **Content Split:** **6,131 Movies (69.6%)** and **2,676 TV Shows (30.4%)**, showing a movie-heavy catalog alongside steady TV show growth in recent years.
- **Top Genres:** **International Movies**, **Dramas**, and **Comedies** lead catalog volume.
- **Top Countries:** The **United States** and **India** rank among the top primary content-producing markets.
- **Top Ratings:** `TV-MA` and `TV-14` account for the largest share of titles, pointing to strong mature and teen/young-adult positioning.
- **Movie Runtime:** Movie lengths have a median duration of around **98 minutes**, highlighting a ~90–105 minute sweet spot.

## Tools & Workflow
- **Python (`pandas`, `matplotlib`, `seaborn`):** Data cleaning (`cleaning.py`) and generating 6 EDA charts (`charts.py`).
- **SQL:** Aggregation queries (`netflix_queries.sql`) for content counts, top release years, ratings, primary countries, and average movie runtime.
- **Strategy Memo:** Concise content recommendations in `strategy_memo.md`.

## Repository Structure
- `cleaning.py` — Loads raw data, fills missing `country` and `rating` values with `"Unknown"`, standardizes `date_added`, and exports `netflix_cleaned.csv`.
- `netflix_cleaned.csv` — Cleaned dataset ready for analysis.
- `netflix_queries.sql` — SQL queries covering type counts, top release years, top ratings, top primary countries, and average movie duration.
- `charts.py` — Script generating all 6 visualizations.
- `1_movies_vs_tv_shows.png` to `6_movie_duration.png` — Saved EDA charts (Movies vs TV Shows, Top 10 Genres, Release Trend by Year, Top 10 Countries, Top 8 Ratings, and Movie Duration Distribution).
- `strategy_memo.md` — Actionable content strategy recommendations.

## Key Strategy Takeaways
1. Test new shows in **1–2 season** runs and renew strong performers.
2. Focus acquisitions and originals on **core ratings (`TV-MA`, `TV-14`)** and high-demand **dramas, comedies, and international titles**.
3. Keep feature movie runtimes close to the **~90–105 minute** range around the **98-minute** median.
