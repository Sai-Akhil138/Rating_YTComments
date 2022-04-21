from googletrans import Translator
import re
from googleapiclient.discovery import build
import pandas as pd


def video_comments(video_id, max_pages):
    api_key = 'AIzaSyDCGCR-1-raEtVJ_5wzfo71pihzaLO09jE'

    pages = 0

    comment_list = []

    # creating youtube resource object
    youtube = build('youtube', 'v3', developerKey=api_key)

    video_response = youtube.commentThreads().list(part='snippet,replies',
                                                 videoId=video_id,
                                                 maxResults=100).execute()
    # print(video_response)

    while video_response and pages < max_pages:
        pages += 1
        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            comment_list.append(comment)

        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(part='snippet,replies',
                                                           videoId=video_id,
                                                           maxResults=200).execute()
        else:
            break
    # print(pages, len(comment_list))
    return comment_list


def remove_emojis(comment_list: list):
    emojis = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F1E0-\U0001F1FF"
            u"\U00002500-\U00002BEF"
            u"\U00002702-\U000027B0"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2640-\u2642"
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"
            u"\u3030"
                        "]+", re.UNICODE)
    for index, comment in enumerate(comment_list):
        comment_list[index] = emojis.sub(r'', comment)


def remove_empty_comments(comment_list: list):
    count = 0
    for comment in comment_list:
        if comment == "":
            comment_list.remove(comment)
            count += 1


def remove_other_language_comments(comment_list: list):
    count = 0
    # print("Deleted Comment")
    translator = Translator()
    for index, comment in enumerate(comment_list):
        d = translator.detect(comment)
        # print(d)
        if len(d.lang) >= 2:
        # print(2, comment, d)
            count += 1
            del comment_list[index]
        elif len(d.lang) == 1 and d.lang != 'en' or d.confidence < 0.6:
        # print(1, comment, d)
            count += 1
            del comment_list[index]

    print("Deleted:", count)

def comments_to_csv(comment_list: list):
    comments_df = pd.DataFrame(comment_list)
    comments_df.to_csv("comments.csv")
    print("File Created Success")

def get_video_id( url: str, group: int):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    regex = re.compile(pattern)
   
    video_id = regex.search(url)
    if not video_id:
        return False
    return video_id.group(group)

def process_comments(url):
    #url = "https://www.youtube.com/watch?v=loja1AbkbP0"
    video_id = get_video_id(url, 1)

    # video_id = "ezCXTvYQcAY"
    # video_id = "loja1AbkbP0"
    # video_id ="TApMNhQPaCM"


    
    comment_list = video_comments(video_id, 2)
    print("\nExtracted Comments:")
    for comment in comment_list:
        print(comment)


    remove_emojis(comment_list)
    print("\nRemoved Emojis' from Comments:")
    for comment in comment_list:
        print(comment)

    remove_empty_comments(comment_list)
    print("\nDiscarded Empty Comments:")
    for comment in comment_list:
        print(comment)

    remove_other_language_comments(comment_list)
    print("\nFiltered English Langugage Comments:")
    for comment in comment_list:
        print(comment)

    comments_to_csv(comment_list)

#print(comment_list)
