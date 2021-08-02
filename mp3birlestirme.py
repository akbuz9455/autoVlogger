import subprocess

def convert_seq_to_mov():
    input = r"C:\mypics\img%03d.jpg"
    output = r"ciktim2.flv"
    frame_rate = 24
    cmd = f'ffmpeg -f concat -safe 0 -i mylist.txt -c copy output24.mp3'
    
    print(cmd)
    subprocess.check_output(cmd, shell=True)

convert_seq_to_mov()


