from pytubefix import Search
from pytubefix import YouTube
import os
import shutil  # Importing libs


# This is funcs file


def give_link(name):
    s = Search(f"{name}")
    yt_id = s.results
    video_ids = [video.video_id for video in yt_id]

    video_id = video_ids[0]
    base_url = f"https://www.youtube.com/watch?v={video_id}"
    return base_url


def delete_audio():
    shutil.rmtree('music')


def find_music_name():
    return os.listdir("music")[0]


def remove_all_files(dir):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


def download_vid(name):
    s = Search(f"{name}")
    yt_id = s.videos
    video_ids = [video.video_id for video in yt_id]

    video_id = video_ids[0]
    base_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(url=base_url)
    audio_stream = yt.streams.filter(
        only_audio=True,
        file_extension="mp4"
    ).first().download(output_path='music')


def delete_selected_file(param):
    os.remove(f"music/{param}")
