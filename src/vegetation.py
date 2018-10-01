import Algorithmia

from .util import sanity 

def vegetation(src):
    return 0


def vegetation_dir(src):
    segmented_images = []
    return [vegetation(img_loc) for img_loc in segmented_images]


    


def apply(input):
    sanity(input)
    src_images = input['src']
    return "{}"
