Thesis: Algorithmic techniques for detecting structural properties of news dissemination on Twitter 
Python3, NetworkX

In my Diploma Thesis I worked on the identification of fake news in Twitter. I tried to create an innovative network – based technique to identify the credibility of news in early stages of propagation. My study consists of the algorithm implementation and the data processing. At first, I implemented Collective Influence, while at the same time I was scraping Twitter via Twitter API. Subsequently, I processed, cleaned and stored the data, so I could apply the algorithm on them and get statistical results. Except from my data collection, I used pre-existing datasets and ready-to-apply algorithms to compare the efficiency of my implementation. In conclusion, a real story is spread mostly by the root user, while a fake one is spread by a couple of them.

twitterCrawler.py
The twitterCrawler was used to establish a connection to the Twitter Streaming API which means making a very long lived HTTP request and parsing the response incrementally. 
In order to connect to the API, you need to request for connecting credentials. Go check --> https://developer.twitter.com/en

relationships.py
The fetched data had to been cleaned and processed. All twitter posts indicate directly to each original tweet, so if the root tweet was avalaible, the story chain was created. Otherwise, the collected reactions were been discarded. To create the story chain we assume that the information flows from userA to userB if userB follows userA and userB reacts to the post after userA. Twitter allows to retrieve relationship data among users and each post has a timestamp.

ci.py
Collective Influence is an influence maximization algorithm, which finds the most significant node or nodes in a graph. A significant node is considered to be the one responsible for the dissemination of information at the network. The collective influence algorithm gives a value of significance to each node. Moment-N was used as statical measure. I assume that significant nodes gather at least 50% of the total significance of the network.

maxHeap.py
For collective influence implementation I used the GeeksForGeeks maxHeap. Go check -->https://www.geeksforgeeks.org/max-heap-in-python/
