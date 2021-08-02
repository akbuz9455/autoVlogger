import os

def runBash(command):
	os.system(command)

def crop(start,end,input,output):
	str = "ffmpeg -i " + input + " -ss  " + start + " -to " + end + " -c copy " + output
	print (str)
	runBash(str)

crop("00:00:00","00:00:02","video1.mp4","video3.mp4")
