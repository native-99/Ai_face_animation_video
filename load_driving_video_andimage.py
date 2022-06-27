import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
from demo import make_animation
from skimage import img_as_ubyte
warnings.filterwarnings("ignore")



source_image = imageio.imread('/content/elsa_frozen.png')


driving_video_path = '/content/face_conlusion' # do not write ".mp4" here

driving_video_path_mp4 = driving_video_path + '.mp4'
driving_video = imageio.mimread(driving_video_path_mp4) #must be mp4


#Resize image and video to 256x256
def resize_image(imageio_image):
  return resize(imageio_image, (256, 256))[..., :3]

source_image = resize_image(source_image)
driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]



def get_video_fps(video_path, verbose=False):
  reader = imageio.get_reader(video_path)
  fps = reader.get_meta_data()['fps']
  if verbose:  print( video_path, 'fps:', fps )
  reader = None  
  return fps

def fast_display_for_small_videos(source, driving, generated=None):
    fig = plt.figure(figsize=(8 + 4 * (generated is not None), 6))
    #
    ims = []
    for i in range(len(driving)):
        cols = [source]
        cols.append(driving[i])
        if generated is not None:
            cols.append(generated[i])
        im = plt.imshow(np.concatenate(cols, axis=1), animated=True)
        plt.axis('off')
        ims.append([im])
    #
    ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000) # interval = 50 for 20 fps
    plt.close()
    return ani

def write_video_source_plus_driving(fps, source_image, driving_video):    
  from skimage import img_as_ubyte
  video_path = '/content/side_by_side2.mp4'
  imageio.mimsave(video_path, [img_as_ubyte(np.hstack( (source_image, driving_video[i]) )) for i in range(len(driving_video))], fps=fps)
  return video_path

def write_video_source_driving_generated(fps, source_image, driving_video, generated):    
  from skimage import img_as_ubyte
  video_path = '/content/side_by_side3.mp4'
  imageio.mimsave(video_path, [img_as_ubyte(np.hstack( (source_image, driving_video[i], generated[i]) )) for i in range(len(driving_video))], fps=fps)
  return video_path

def mp4_as_html(mp4_path):
  from base64 import b64encode
  mp4 = open(mp4_path,'rb').read()
  data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
  return """
    <video height=400 controls>
          <source src="%s" type="video/mp4">
    </video>
    """ % data_url


fps = get_video_fps(driving_video_path_mp4, verbose=True)