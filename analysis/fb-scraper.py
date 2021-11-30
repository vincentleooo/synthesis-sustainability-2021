#%%
from facebook_scraper import get_posts
from time import sleep
from datetime import datetime
from random import randint
#%%
posts=[]
# set_cookies("cookies.json")
try:
	for post in get_posts("TheStraitsTimes", cookies="cookies.json", options={"allow_extra_requests": True, "posts_per_page": 10, "pages": None, "progress": True, "reactions": True, "reaction_count": True, "reactors": False, "comments": True, "HQ_images": False}):
		print(post.get("time"))
		posts.append(post)
		# sleep(randint(5,30))
		if post.get("time") < datetime(2019,1,1):
			break
except:
	print('sleeping for 30-60 mins')
	sleep(randint(1800,3600))

print(posts)
# %%
import json
