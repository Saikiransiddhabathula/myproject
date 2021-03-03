#import moviepy if the module is not present install it


#pip install moviepy--------through command prompt
import moviepy.editor
output = input("enter the video file path : ")
video = moviepy.editor.VideoFileClip(output)
audio = video.audio
audio.write_audiofile("output1.mp3")
#change the output folder name whenever working with new Mp4 file
