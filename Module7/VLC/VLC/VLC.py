import vlc
import time

#media player constructor
media_player = vlc.MediaPlayer()

# media obj
media = vlc.Media("vlcvid.mp4")

#setting media to the media player
media_player.set_media(media)

# start playing the video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective of the length of the video
time.sleep(30)

# get media
value = media_player.get_media()

# printing media
print("media : ")
print(value)

#pip install tkvideo
#pip install pillow
#pip install imageio

# from tkinter import *
# from tkvideo import tkvideo
# # create instance for the window
# root = Tk()

# #set window title
# root.title("Video Player")

# #create label
# video_label = Label(root)
# video_label.pack()

# #read video to display on lebale
# player = tkvideo("vlcvid.mp4", video_label, loop = 1, size = (700, 500))

# player.play()
# root.mainloop()
