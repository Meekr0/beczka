from pytubefix import YouTube

dest = './data/audio/'
fileName = 'audio.webm'

class MusicUtils:
    def __init__(self):
        pass


    @staticmethod
    async def downloadAudio(url):
        try:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            video.download(output_path=dest, filename=fileName)
            return True
        except Exception as e:
            print(f'Error: {str(e)}')
            return False


    @staticmethod
    async def getTitle(url):
        try:
            yt = YouTube(url)
            return yt.title
        except Exception as e:
            print(f'Error: {str(e)}')
            return "Something went wrong"


    @staticmethod
    def getFilePath():
       return dest + fileName