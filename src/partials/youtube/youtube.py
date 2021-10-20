from pytube import YouTube


def youtube():
    # input('URL VIDEO: ')
    youtube_url = 'https://www.youtube.com/watch?v=uMeR2W19wT0'

    try:
        youtube_response = YouTube(youtube_url)
        stream = youtube_response.streams.filter(
            progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        stream.download(output_path='./assets/videos')
    except ValueError:
        print('Algo deu errado!')
