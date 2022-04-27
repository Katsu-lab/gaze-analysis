import cv2
import sys
import numpy as np
import moviepy.editor as mp

# 画像加工
def mkimg(img):
    # ここに変更を記述する

    return img

# 動画関連 -------------------------------------------------------------
def set_audio(srcfile,imgfile,outfile):
    # Extract audio from input video.
    clip_input = mp.VideoFileClip(srcfile)
    clip_input.audio.write_audiofile('audio.mp3')
    # Add audio to output video.
    clip = mp.VideoFileClip(imgfile).subclip()
    clip.write_videofile(outfile, audio='audio.mp3')

# 動画のファイル名設定
srcfile = sys.argv[0]
imgfile = "out.mp4"
outfile = sys.argv[0].replace(".mp4","out.mp4").replace(".MP4","out.MP4")
video = cv2.VideoCapture("../data/sample.mp4")

# 幅と高さを取得
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

#総フレーム数/フレームレートを取得
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = int(video.get(cv2.CAP_PROP_FPS))

# 保存用
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter(imgfile, fmt, frame_rate, size)

for i in range(frame_count):
    ret, frame = video.read()
    write_frame = mkimg(frame)
    writer.write(write_frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("newf", write_frame)
    cv2.moveWindow("newf",3700,0)

    # qキーが押されたら途中終了
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()
video.release()
cv2.destroyAllWindows()

# 音声付与
set_audio(srcfile,imgfile,outfile)