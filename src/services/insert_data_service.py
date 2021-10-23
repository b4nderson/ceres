from database.connection import database


def insert_data_service(video_name):
    try:
        print('[insert_data_service] Inserting data on database...')

        database.insert({'video_name': video_name})

        print('[insert_data_service] Data inserted succefully!')

    except ValueError:
        print(
            '[insert_data_service] Its not possible insert data on database!'
        )
