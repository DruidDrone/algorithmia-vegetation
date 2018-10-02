################################################################################
# Algorithmia image vegetation algorithm                                       #
# ============================================================================ #
#                                                                              #
# This algorithm predicts the percentage vegetation present in street-level    #
# images. The implementation wraps the functionality of the                    #
# https://methods.officialstatistics.org/algorithms/nocturne/segment service.  #
#                                                                              #
# Phil Stubbings, ONS Data Science Campus.                                     #
################################################################################
import Algorithmia
from PIL import Image
import numpy as np
from .vegetator import Vegetator

class Deep(Vegetator): 

    def __init__(self):
        super().__init__()

    def pre_processing(self, src):
    
        # use https://methods.officialstatistics.org/algorithms/nocturne/segment
        # set timeout to maximum 50 minutes.
        # segment algo. will output results in to data//.session location which is
        # only active during the request.
        segmented_images = 'data://.session'
        algo = client.algo('nocturne/segment').set_options(timeout=3000)
        result = algo.pipe(dict(src=src, dst=segmented_images))

        return client.dir(segmented_images)

    def post_processing(self, src):
        """Use deep image segmentation to determine percentage vegetation present
        in an algorithmia DataFile.

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
        f = src.getFile()
        bmp_img = Image.open(f.name)
        np_img = np.array(bmp_img)
        np_img = np_img.flatten()
        return round(np.sum(np_img == 8)/len(np_img), 4)
