################################################################################
# Image Vegetator                                                              # 
# ============================================================================ #
# Phil Stubbings, ONS Data Science Campus.                                     #
################################################################################
import Algorithmia

class Vegetator():

    def __init__(self):
        self.client = Algorithmia.client()

    def pre_processing(self, src):
        """hook method."""
        pass

    def post_processing(self, src):
        """hook method."""
        return -1

    def process(self, src):
        """Process the input street-level images.

        Parameters
        ----------
        src: str
            The location of the input images.

        Returns
        -------
        list
            A list of predicted percentage vegetation for each image.
            A dictionary containing filenames and associated percentage vegetation scores.
        """
        
        def get_datafile(img_loc):
            idx = img_loc.rfind("/")
            data_dir = img_loc[:idx]
            file_str = img_loc[idx+1:]
            return self.client.dir(data_dir).file(file_str)

        files = self.pre_processing(src).files()
        file_name = lambda file_str: file_str[file_str.rfind("/")+1:]      



        orig_files = [file_name(f.getName()) for f in self.client.dir(src).files()]
        file_map = {f[:f.rfind(".")]+".bmp":f for f in orig_files}
        results = {file_name(img_loc.getName()):self.post_processing(img_loc) for img_loc in files}
        fixed_results = {file_map[k]:v for k, v in results} # hack: map back .bmp to original filenames.
        return fixed_results


        #return dict(zip([file_name(f.getName()) for f in self.client.dir(src).files()], [self.post_processing(img_loc) for img_loc in files]))
