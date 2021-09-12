# Thesis
Algorithmic techniques for detecting structural properties of news dissemination on Twitter

Python3, NetworkX

twitterCrawler.py
The twitterCrawler was used to establish a connection to the Twitter Streaming API which means making a very long lived HTTP request and parsing the response incrementally. 
In order to connect to the API, you need to request for the connecting credentials. Go check --> https://developer.twitter.com/en

relationships.py
The fetched data had to been cleaned and processed. All @tweets@ were indicated by the root tweet ID, so if the root tweet was avalaible, the story chain was created. Otherwise, the @tweets@ were been discarded.


