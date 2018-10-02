import Algorithmia
from Algorithmia.errors import AlgorithmException
from .util import sanity 
from PIL import Image
import numpy as np


def vegetation(data_file, vegetation_class_index=8):
    """."""
    f = data_file.getFile()
    bmp_img = Image.open(f.name)
    np_img = np.array(bmp_img)
    np_img = np_img.flatten()
    return "{:.4f}".format(np.sum(np_img == vegetation_class_index)/len(np_img))


def vegetation_dir(src):
    client = Algorithmia.client()
    
    src_dir = client.dir(src)
    if not src_dir.exists():
        raise AlgorithmException("src ({}) does not exist.".format(src))

    algo = client.algo('nocturne/segment/0d0646cbca4747a4d0b38f93e8acb41c5cef5c61').set_options(timeout=600)
    #segmented_images = 'data://.session/'
    segmented_images = 'data://.my/tmp'
    result = algo.pipe(dict(src=src, dst=segmented_images))
    seg_dir = client.dir(segmented_images)
    return [vegetation(img_loc) for img_loc in seg_dir.files()]


def apply(input):
    sanity(input)
    src_images = input['src']
    return {'percentage_vegetation': vegetation_dir(src_images)}
