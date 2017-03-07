from zip_processor import *

zip_process = ZipProcessor("test_document.zip", ZipReplace("rr", "dd"))
zip_process.process_zip()

zip_process = ZipProcessor("imagry.zip", ScaleZip((600, 400)))
zip_process.process_zip()
