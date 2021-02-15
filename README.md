# Marvel-Ghibli Movie Script Sentiment-Analysis
Personal project to discover the differences in sentiment between Marvel (Phase 3) and Ghibli movie scripts.

Noteable Libraries Used:\
 Pandas\
 BeautifulSoup\
 Regular Expressions (re)\
 Pickle\
 Matplotlib\
 TextBlob (for sentiment analysis)

---------------------------------------------

The Jupyter notebooks are set up for different phases of the data analysis process. This is largely based on Alice Zhao's PyOhio presentation for NLP in Python (https://github.com/adashofdata/nlp-in-python-tutorial)

## scraper.py
Simple python script to scrape movie scripts from https://www.scripts.com/ using the "requests" and "BeautifulSoup" libraries

## Data Collection and Cleaning
My process for placing all of the transcripts into a Pandas dataframe to conduct data cleaning. This notebook largely uses the "regular expressions" library to perform several rounds of data cleaning so that sentiment analysis can later be conducted.

## Exploratory Data Analysis
Notebook containing my process for performing basic EDA. CountVectorizer is heavily used to find the most commonly used words in each movie. Word clouds are also used to visualize these results.

## Sentiment
Using the cleaned data obtained from "Data Collection and Cleaning", the TextBlob library is used to find the sentiment and polarity of each movie script, which is then placed in a Pandas dataframe to be converted to CSV and subsequently statistically analyzed in R.

## graphs
This notebook is used to visualize the average sentiment and polarity between the two producers. Graphs are generated in matplotlib.
