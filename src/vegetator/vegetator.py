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
        src_dir = self.pre_processing(src)
        return [self.post_processing(img_loc) for img_loc in src_dir.files()]
