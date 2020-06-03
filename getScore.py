import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 200)


#NLP packages
from textblob import TextBlob

from preprocessing import process_likes
from scraping import scrape


def getScore(link):
    vidName = scrape(link)
    process_likes(vidName)
    score = 0
    video_comm = pd.read_csv(vidName)
    video_comm = video_comm.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
    video_comm.rename(columns={'0': 'comment', '1': 'likes'}, inplace=True)
    print('likes:')
    print(video_comm.get('likes'))
    num_likes = video_comm.get('likes').sum()
    num_comments = video_comm['comment'].count()
    video_comm['likes'] = video_comm['likes'] + 1
    for index, comm in video_comm.iterrows():
        try:
            pol = TextBlob(comm['comment']).sentiment
            score_comm = pol.polarity * comm['likes']
            score += score_comm
        except:
            continue
    return score/num_likes

#Add links here
#print(getScore('https://www.youtube.com/watch?v=-niuhBmUPLU'))
#print(getScore('https://www.youtube.com/watch?v=fP17mIEv8lo'))
#print(getScore('https://www.youtube.com/watch?v=QD0IM5tfnVQ'))
#print(getScore('https://www.youtube.com/watch?v=rmQMKowvYeo'))
print(getScore('https://www.youtube.com/watch?v=QPkXJvULrN8'))