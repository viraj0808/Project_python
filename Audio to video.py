from tkinter.filedialog import *

import moviepy.editor

vid = askopenfilename()
video=moviepy.editor.VideoFileClip(vid)

aud = video.audio

aud.write_audiofile("demo.mp3")

print("---end----")