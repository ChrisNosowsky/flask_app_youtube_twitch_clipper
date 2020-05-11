from pytube import YouTube
import os


def get_youtube(link):
    """Gets a YouTube link from the front-end and downloads it to users default download path"""
    download_path = get_download_path()
    yt = YouTube(link).streams.first().download(download_path)
    print(yt.title, " has been downloaded!")


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