from database.connection import database


def insert_data_service(video_name):
    try:
        database.insert({'video_name': video_name})
    except ValueError:
        print('Error ao inserir dado no database!')
