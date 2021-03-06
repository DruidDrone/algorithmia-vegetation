################################################################################
# Algorithmia (deep) image vegetation algorithm                                #
# ============================================================================ #
#                                                                              #
# Wraps functionality of the                                                   #
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
        """Pre process input images.

        In this case, pre-processing involves sending the iamges to the deep
        image segmentation service and returning the segmented images as the
        result.

        Parameters
        ----------
        src: str
            The location of input images e.g., "data://.my/stuff".

        Returns
        -------
        DataDirectory
            see https://github.com/algorithmiaio/algorithmia-python/blob/master/Algorithmia/datadirectory.py
        """
        # set timeout to maximum 50 minutes.
        # segment algo. will output results in to data//.session location which is
        # only active during the request.
        segmented_images = 'data://.session'
        algo = self.client.algo('nocturne/segment').set_options(timeout=3000)
        result = algo.pipe(dict(src=src, dst=segmented_images))
        return self.client.dir(segmented_images)

    def post_processing(self, src):
        """Calculate vegetation percentage.

        Given as input the segmented images, extract the percentage vegetation.

        Each pixel can have up to 256 possible labels.
        In this implementation, we make use of a pre-trained PSPNet which will
        assign 8 to a pixel if that pixel belongs to the vegetation class.

        Parameters
        ----------
        src: DataFile
            see https://github.com/algorithmiaio/algorithmia-python/blob/master/Algorithmia/datafile.py

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
