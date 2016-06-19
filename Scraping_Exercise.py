# AUTHOR: MOHAMMAD M. GHASSEMI, MIT
# IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests
import string
from ast import literal_eval
from subprocess import call

# Clear the screen
call(["clear"])

# Go to the New York Times Website.
url = 'http://www.nytimes.com/'

# Grab the HTML
r = requests.get(url)
r_html = r.text

# Format the HTML using Beautiful Soup
soup = BeautifulSoup(r_html,"lxml")

# Grab the stories from h1s
mydivs = soup.findAll('h1')
stories = []
for hs in mydivs:
	class_name = str(hs["class"])
	template = "['story-heading']"
	if class_name == template:
		try:
			stories.append(hs.a.string)
		except:
			pass

# Grab the stories from h2s
mydivs = soup.findAll('h2')
for hs in mydivs:
	class_name = str(hs["class"])
	template = "['story-heading']"
	if class_name == template:
		try:
			stories.append(hs.a.string)
		except:
			pass

# Grab the stories from h3s		
mydivs = soup.findAll('h3')
for hs in mydivs:
	class_name = str(hs["class"])
	template = "['story-heading']"
	if class_name == template:
		try:
			stories.append(hs.a.string)
		except:
			pass

# Convert it to the right format and clean the extra whitespace.
out = []
for i in range(0,len(stories)):
	try:
		this_string = stories[i]
		this_string = this_string.encode('ascii', 'ignore')
		this_string = this_string.lstrip()
		this_string = this_string.strip()
		out.append(this_string)
	except:
		print("error")	
		#print(i.replacesplit()))

print(out)
