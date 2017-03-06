import sys
from zip.zip_processor import *
from zip.zip_replace import *

zipreplace = ZipReplace("test_document.zip", 'rr', 'ss')
zipprocessor = ZipProcessor("test_document.zip")
zipprocessor.process_zip()
