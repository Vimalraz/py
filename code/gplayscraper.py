from google_play_scraper import Sort, reviews_all
import pandas as pd

# Replace 'com.example.yourapp' with the actual package ID of the app
# You can find the package ID in the app's Play Store URL (after id=)
app_id = 'com.bigwinepot.nwdn.international' # Example: Busuu app

# Scrape all reviews
# You can customize 'lang' and 'country' for specific language/region reviews
all_reviews = reviews_all(
    app_id,
    lang='en', # Language of reviews to fetch (e.g., 'en' for English)
    country='IN', # Country to fetch reviews from (e.g., 'us' for United States)
    sort=Sort.NEWEST # Sort order (e.g., NEWEST, MOST_RELEVANT)
)

# Convert the list of review dictionaries into a Pandas DataFrame for easier analysis
df_reviews = pd.DataFrame(all_reviews)

# Display the first few rows of the DataFrame
print(df_reviews.head())

# You can now save this DataFrame to a CSV file or perform further analysis
df_reviews.to_csv('app_reviews_remini.csv', index=False)