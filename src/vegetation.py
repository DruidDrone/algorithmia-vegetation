import Algorithmia
from Algorithmia.errors import AlgorithmException
from .util import sanity 
from PIL import Image
import numpy as np


def vegetation(data_file, vegetation_class_index=8):
    """Determine percentage vegetation present in an algorithmia DataFile.

    Parameters
    ----------
    data_file: DataFile
        An algorithmia data file.
    vegetation_class_index: int
        Vegetation class index. Each pixel can have up to 256 possible labels.
        In this implementation, we make use of a pre-trained PSPNet which will
        assign 8 to a pixel if that pixel belongs to the vegetation class.

    Returns
    -------
    float
        Percentage vegetation present in the scene.
    """
    f = data_file.getFile()
    bmp_img = Image.open(f.name)
    np_img = np.array(bmp_img)
    np_img = np_img.flatten()
    return round(np.sum(np_img == vegetation_class_index)/len(np_img), 4)


def vegetation_dir(src):
    """Determine percentage vegetation for all images in an algorithmia hosted
    directpry.

    Parameters
    ----------
    src: str
        An algorithmia hosted directory of street-level images.

    Returns
    -------
    list
        List of (filename, percentage) tuples.            
    """
    client = Algorithmia.client()
    
    src_dir = client.dir(src)
    if not src_dir.exists():
        raise AlgorithmException("src ({}) does not exist.".format(src))

    algo = client.algo('nocturne/segment').set_options(timeout=3600)
    segmented_images = 'data://.session'
    result = algo.pipe(dict(src=src, dst=segmented_images))
    seg_dir = client.dir(segmented_images)
    percent = [vegetation(img_loc) for img_loc in seg_dir.files()]
    #f_names = [f.getName() for f in seg_dir.files()]
    #return zip(f_names, percent)
    return percent


def apply(input):
    """Algorithmia entry point."""
    sanity(input)
    src_images = input['src']
    return {'percentage_vegetation': vegetation_dir(src_images)}
