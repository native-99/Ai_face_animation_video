# load Deep Learning model from disk into memory

from demo import load_checkpoints

def Load_model()
	#generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
#                            checkpoint_path='/content/gdrive/My Drive/DL/first-order-model/vox-adv-cpk.pth.tar')
	generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
                            checkpoint_path='/content/first-order-model/vox-cpk.pth.tar')

Load_model()