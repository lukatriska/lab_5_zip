import shutil
import zipfile
from pathlib import Path
from zip_replace import ZipReplace
from scaleimage import ScaleZip


class ZipProcessor:
    def __init__(self, zipname, wanted_process):
        self.zipname = zipname
        self.wanted_process = wanted_process
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_zip(self):
        """
        This is the 'manager' of the whole program: it unzips, processes and zips files.
        """
        self.unzip_files()
        self.wanted_process.processs(self)
        self.zip_files()

    def unzip_files(self):
        """
        Unzips the file.
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        Zips the file.
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
