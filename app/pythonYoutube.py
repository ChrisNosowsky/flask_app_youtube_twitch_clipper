from pytube import YouTube
from moviepy.editor import *
import os


def get_youtube(link):
    """Gets a YouTube link from the front-end and downloads it to users default download path"""
    try:
        timestamp_index = link.find('&t=') + 3
        timestamp = ""
        for i in range(timestamp_index, len(link)):
            if link[i].isdigit():
                timestamp += link[i]
            else:
                break
        #download_path = get_download_path()
        yt = YouTube(link)
        bounds = get_bounds(timestamp, yt)
        print('before')
        yt.streams.first().download('/usr/local/bin/')
        print('middle')
        cwd = os.getcwd()
        print('hey')
        print(cwd)
        print('HEYHEY YOUSADSAHDKJHSADKJHK' + cwd)

        # filename = yt.streams.first().default_filename
        # full_path = download_path + '\\' + filename
        # video = VideoFileClip(full_path)
        # video_cut = video.subclip(bounds[0], bounds[1])
        # video_cut.write_videofile(download_path + '\\' + "CLIPPED.mp4")
    except:
        print("ERROR. PLEASE RETURN TO PREVIOUS SCREEN AND TRY AGAIN")


def get_bounds(timestamp, yt):
    if int(timestamp) - 30 < 0:
        lower_bound = 0
    else:
        lower_bound = int(timestamp) - 30

    if yt.length < int(timestamp) + 60:
        upper_bound = yt.length
    else:
        upper_bound = int(timestamp) + 60

    return [lower_bound, upper_bound]


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')