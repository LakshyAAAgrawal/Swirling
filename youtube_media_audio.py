import youtube_dl
import subprocess
def youtube_audio(url):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
	command1 = "pwd"
	s1 = str(subprocess.call(command1, shell = True))
	#print(s1)
	command3 = 'grep -e "mp4" -e "mkv"' 
	s2 = str(subprocess.call(command3, shell = True))
	print(s2)
	s = s1+s2
	print(s)
	command2 = "ffmpeg -i " + s +" -ab 160k -ac 2 -ar 44100 -vn audio.wav"
	subprocess.call(command2, shell=True)
youtube_audio("https://www.youtube.com/watch?v=7wtfhZwyrcc")
