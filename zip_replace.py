<<<<<<< HEAD
from zip.zip_processor import ZipProcessor
import sys
import os
=======
# from zip_processor import ZipProcessor
# import sys
# import os
>>>>>>> 908791e32a03ddbc4e2bc6131eaa418547efb801


class ZipReplace:

<<<<<<< HEAD
    def __init__(self, filename, search_string, replace_string):
        ZipProcessor.__init__(self, filename)
        self.search_string = search_string
        self.replace_string = replace_string
    
    def process(self):
=======
    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string
    
    def processs(self, proc):
>>>>>>> 908791e32a03ddbc4e2bc6131eaa418547efb801
        """
        Performs a search and replace on all files in the
        temporary directory.
        """
<<<<<<< HEAD
        for filename in self.temp_directory.iterdir():
=======
        for filename in proc.temp_directory.iterdir():
>>>>>>> 908791e32a03ddbc4e2bc6131eaa418547efb801
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)


# if __name__ == "__main__":
#     zipreplace = ZipReplace('rr', 'ss')
#     ZipProcessor("test_document.zip", zipreplace).process_zip()
<<<<<<< HEAD
=======
# if __name__ == "__main__":
#     ZipReplace(*sys.argv[1:4]).process_zip()
>>>>>>> 908791e32a03ddbc4e2bc6131eaa418547efb801
