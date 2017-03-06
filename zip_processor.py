import os
import shutil
import zipfile
from pathlib import Path
from zip_replace import ZipReplace


class ZipProcessor:
<<<<<<< HEAD:zip_processor.py
    def __init__(self, zipname):
=======
    def __init__(self, zipname, wanted_process):
>>>>>>> 908791e32a03ddbc4e2bc6131eaa418547efb801:zip_processor.py
        self.zipname = zipname
        self.wanted_process = wanted_process
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))
        # self.processor = processor

    def process_zip(self):
        """
        This is the 'manager' of the whole program: it unzips, processes and zips files.
        """
        self.unzip_files()
<<<<<<< HEAD:zip_processor.py
        self.process()
=======
        self.wanted_process.processs(self)
>>>>>>> 908791e32a03ddbc4e2bc6131eaa418547efb801:zip_processor.py
        self.zip_files()
        # self.processor.process(self)

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
