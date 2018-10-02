################################################################################
# Image vegetation algorithm (L*a*b* colour space approach)                    #
# ============================================================================ #
#                                                                              #
#                                                                              #
# Phil Stubbings, ONS Data Science Campus.                                     #
################################################################################
from Algorithmia.errors import AlgorithmException
from PIL import Image
from .vegetator import Vegetator
import numpy as np

class Lab(Vegetator):

    def __init__(self):
        super().__init__()

    def pre_processing(self, src):
        src_dir = self.client.dir(src)
        if not src_dir.exists():
            raise AlgorithmException("src ({}) does not exist.".format(src))
        return src_dir

    def post_processing(self, src):
        """Use Lab colour space method to detect ratio of green pixels in the
        provided image.

        Default optimal values:
        https://datasciencecampus.ons.gov.uk/wp-content/uploads/sites/10/2018/09/ons-dsc-mapping-the-urban-forest.pdf

        The image is first converted to the L*a*b* colour space. Lab is better
        suited to image processing tasks since it is much more intuitive than 
        RGB. In Lab, the lightness of a pixel (L value) is seperated from the 
        colour (A and B values). A negative A value represents degrees of
        green, positive A, degrees of red. Negative B represents blue, while 
        positive B represents yellow. A colour can never be red _and_ green or
        yellow _and_ blue at the same time. Therefore the Lab colour space 
        provides a more intuitive seperability than RGB (where all values must 
        be adjusted to encode a colour.) Furthermore, since lightness value (L)
        is represented independently from colour, a 'green' value will be robust 
        to varying lighting conditions.

        Parameters
        ----------
        data_file: DataFile
            An algorithmia data file.
        a1, a2, b1, b2: int
            Threshold parameters.

        Returns
        -------
        float
            In the range [0, 1].
            Where 0 corresponds to 0% detected green in the image,
            1 corresponds to 100% green image.     
        """
        src_file = src.getFile()
        image = Image.open(src_file.name)
        image = np.array(image)

        # convert RGB ordered image to lab space
        lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

        # alpha value ( < 0 = green, > 0 = red).
        _, a, b = cv2.split(lab)

        # rescale
        a = a-128.0
        b = b-128.0

        # green mask.
        # optimal values from:
        # https://datasciencecampus.ons.gov.uk/wp-content/uploads/sites/10/2018/09/ons-dsc-mapping-the-urban-forest.pdf
        mask = (-31 <= a) & (a <= -6) & (5 <= b) & (b <= 57) 

        # ratio of green appearing in the image
        green = a[mask]
        cov = green.size/float(a.size) 
        
        return round(cov, 4)
