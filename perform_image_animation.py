import load_driving_video_andimage
import matplotlib.animation as animation

write_video_source_plus_driving=write_video_source_plus_driving(fps, source_image, driving_video)
write_video_source_driving_generated=write_video_source_driving_generated(fps, source_image, driving_video, generated)

#source_image = imageio.imread('/content/lisa_blackpink.png')
source_image = resize_image(source_image)

sbys2 = write_video_source_plus_driving(fps, source_image, driving_video)
HTML( mp4_as_html( sbys2 ) )

predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

#save resulting video
imageio.mimsave('/content/generated.mp4', [img_as_ubyte(frame) for frame in predictions], fps=fps)

# show sie by side
#HTML(fast_display_for_small_videos(source_image, driving_video, predictions).to_html5_video())
sbs3 = write_video_source_driving_generated(fps, source_image, driving_video, predictions)
HTML( mp4_as_html(sbs3) )


# add audio to generated videos
for video_path in ('side_by_side3', 'generated'):
  !ffmpeg -i /content/{video_path}.mp4 -i {driving_video_path_mp4} -map 0:v -map 1:a -c:v copy -shortest /content/{video_path}_audio.mp4 -y  > /dev/null 2>&1 &


#videos can be downloaded from /content folder
from google.colab import files
files.download('/content/generated_audio.mp4') 
files.download('/content/side_by_side3_audio.mp4') 