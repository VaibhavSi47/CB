from gnewsclient import gnewsclient

client = gnewsclient.NewsClient(language='english',
								location='india',
								topic='covid-19 twitter',
								max_results=300)

# prints location
print("Location: \n",client.locations)
print()

# prints languages
print("Language \n",client.languages)
print()

# prints topics
print("Topic \n",client.topics)

news_list = client.get_news()
print(news_list)

for item in news_list:
	print("Title : ", item['title'])
	print("Link : ", item['link'])
	print("")
