# from zip_processor import ZipProcessor
# import sys
from PIL import Image


class ScaleZip:

    def __init__(self, size):
        self.size = size

    def processs(self, proc):
        """
        Scales each image in the directory to 640x480.
        """
        for filename in proc.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize(self.size)
            scaled.save(str(filename))

# if __name__ == "__main__":
#     ScaleZip(*sys.argv[1:4]).process_zip()
