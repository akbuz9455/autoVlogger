import subprocess
(
    
    ffmpeg
    .input('C:\mypics\img%03d.jpg', pattern_type='glob', framerate=25)
    .filter('deflicker', mode='pm', size=10)
    .filter('scale', size='hd1080', force_original_aspect_ratio='increase')
    .output('movie.mp4', crf=20, preset='slower', movflags='faststart', pix_fmt='yuv420p')
    .view(filename='filter_graph')
    .run()
)
