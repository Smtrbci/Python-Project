from moviepy.editor import *

video_mp4 = input("Uzantı ile birlikte video dosyasının adını girin-")
audio_mp3 = input("Dönüştürülen ses için dosya adını girin (uzantısız-)")

clip = VideoFileClip(video_mp4)
audio = clip.audio

audio.write_audiofile(audio_mp3+".mp3")

clip.close()
audio.close()
