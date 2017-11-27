import ffmpy
import config as cfg

ff = ffmpy.FFmpeg(
    inputs={'cs_test.mp4':None },
    outputs={'frame.jpg': ' -ss 00:00:16 -t 00:00:2 -s 640x360 -r 1 -f mjpeg',
    'frame_crop.jpg': '-filter:v "crop=50:30:322:333" -ss 00:00:16 -t 00:00:2 -s 640x360 -r 1 -f mjpeg'}
    )

ff.run()