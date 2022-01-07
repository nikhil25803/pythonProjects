import os
from pytube import YouTube 
# Import Module

from os import path



src = input("Enter the URL: ")
#paste the download link here

src = YouTube(src)

video = src.streams.get_highest_resolution()

print(f"Downloading {src.title} by {src.author}")

print("The video is being downloading.... ")

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'Ddesktop')

video.download(desktop+"\youtube video")

print("Download Complete")