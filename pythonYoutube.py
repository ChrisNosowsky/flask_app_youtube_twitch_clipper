from pytube import YouTube

def get_youtube(link):
    yt = YouTube(link).streams.first().download("C:/Users/Racec/OneDrive/Videos/")
    print(yt.title, " has been downloaded!")