# %%
from facebook_page_scraper import Facebook_scraper

page_name = "TheStraitsTimes"
posts_count = 1000
browser = "chrome"

straits_times = Facebook_scraper(page_name, posts_count, browser)

# %%
json_data = straits_times.scrap_to_json()

print(json_data)
# %%
csv_data = straits_times.