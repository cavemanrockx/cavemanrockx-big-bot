from cogs.memes import caption
from moviepy.video.fx import mask_and, mask_color
from moviepy.video.io.VideoFileClip import VideoFileClip
import requests
from io import BytesIO
import os.path
import json

def mask():
    meme_clip_loc = os.path.join(os.path.dirname(__file__), "videos/kickdoor.mp4")
    
    main_clip = VideoFileClip(meme_clip_loc)
    main_clip = mask_color.mask_color(main_clip, [110, 246, 24], 5)

