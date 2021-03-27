# Ranking Youtube Videos
Python Scripts to Scrape Youtube Videos for number of likes of comments. Youtube Data API doesn't allow you to get the number of likes of a specific comments, thus Selenium has been used to scrape for comments.

# Files
1. GetScore.py : Main File, Run this with the links of the video to be scraped. Returns and prints individual score of the link given.
2. preprocessing.py : Converts Scraped text into Readible Format. (K = 1,000, M = 1,000,000 etc)
3. scraping.py : uses Selenium to scrape the links given.
4. scoring.ipynb : tried example. Do not Use for testing purposes. Use full script from getScore.py.
5. GetData.ipynb : Jupyter Notebook to create DataSet (Used Kaggle Youtube-Comments Dataset, modified to add comment polarities).
6. AllComents.csv : Kaggle unprocessed Dataset.
7. FinalDataset.csv : Processed Dataset.
