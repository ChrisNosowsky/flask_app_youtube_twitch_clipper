import pytube
from moviepy.editor import VideoClip, VideoFileClip
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
        yt = pytube.YouTube(link)
        bounds = get_bounds(timestamp, yt)
        yt.streams.first().download('./download_folder/')
        filename = yt.streams.first().default_filename
        full_path = './download_folder/' + filename

        video = VideoFileClip(full_path)
        video_cut = video.subclip(bounds[0], bounds[1])
        video_cut.write_videofile(download_path + '\\' + "CLIPPED.mp4")
        return "SUCCESS" + full_path
    except:
        print("ERROR. PLEASE RETURN TO PREVIOUS SCREEN AND TRY AGAIN.")
        return "ERROR" + link[:-5]


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
