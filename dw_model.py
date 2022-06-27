#Dont forget to take clone from repo of first-order-model

# download model from the internet to the disk
fid = '1wzcVtLMcqkzforAhDFc7kHhoX1yeNC2h' # vox-cpk.pth.tar
import gdown
url = 'https://drive.google.com/uc?id=' + fid
gdown.download(url, "/content/first-order-model/vox-cpk.pth.tar", quiet=True)


