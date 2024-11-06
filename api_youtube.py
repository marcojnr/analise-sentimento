import os
import sys
import re
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DATA_DIR = os.getcwd()+'/'

def get_comment_replies(youtube, parent_id):
    "Retorna lista de respostas a um comentario"
    replies = []
    try:
        response = youtube.comments().list(
            part="snippet",
            parentId=parent_id,
            maxResults=100,
            textFormat="plainText"
        ).execute()

        for element in response["items"]:
            replies.append(element["snippet"]["textDisplay"])

    except HttpError as e:
        print(e)
    return replies

def save_video_comments(youtube, video_id, filename):
    "Salva comentarios de um video em um arquivo"

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    try:
        response = request.execute()
        has_next = True
        page_idx = 0
        comments = []
        while has_next:
            qtde = [] # limpar só para a contagem
            page_idx += 1
            print(f"Page: {page_idx}")
            
            for item in response["items"]:
                snippet = item["snippet"]
                comment = snippet["topLevelComment"]
                text = comment["snippet"]["textDisplay"]
                comments.append(text)
                qtde.append(text)
                # Pegar respostas tambem!
                if snippet["totalReplyCount"] > 0:
                    # print(text), se quiser ter um feedback
                    replies = get_comment_replies(youtube, parent_id = comment["id"])
                    comments.extend(replies)
                    qtde.extend(replies)

            print(f"Comentários: {len(qtde)}\n")
            
            if "nextPageToken" in response:
                token = response["nextPageToken"]
                response = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=100,
                    textFormat="plainText",
                    pageToken=token
                ).execute()
            else:
                has_next = False
        
            # criar csv
            df = pd.DataFrame(comments, columns=['Comentarios']).reset_index()
            df['Comentarios'] = df['Comentarios'].str.replace('\n', ' ', regex=False).str.replace('\r', '', regex=False)
            # print(f"Total de comentários: {len(df)}\n")
            df.to_csv(filename, encoding="UTF-8", sep=';', index=False)
        print(f"Total de Comentários: {len(comments)}\n")
            
    except HttpError as e:
        print(e)


# def count_hashtag(comments, hashtag):
#     counter = 0
#     for comment in comments:
#         if hashtag in comment.lower():
#             counter += 1
#     return counter

def id_video_format(lind_video: str):
    # link = lind_video
    id_v = re.findall('v=.+$', lind_video)
    id_v = str(id_v[0])
    id_v = id_v[2:]
    if id_v[-1] == "'":
        id_v = id_v.replace(id_v[-1],"")
        # print(id_v)
    return id_v


if __name__ == '__main__':
    with open("key-api.txt") as apifile:
        api_key = apifile.read().strip()
    api_name = "youtube"
    api_version = "v3"
    try:
        input_link = sys.argv[1]
        video_id = id_video_format(input_link)
        # video_id = "JfJJIrOhWwQ" 
        filename = "result.csv"
        # hashtag = "#sql"

        youtube = build(api_name, api_version, developerKey=api_key)

        save_video_comments(youtube, video_id, filename)
        print(f"veja resultado no arquivo -> {filename}")

    except IndexError as a:
        print('\nRode novamente! Passando o link do video como paramentro.\n ex:\n api_youtube.py lind_do_video_youtube')