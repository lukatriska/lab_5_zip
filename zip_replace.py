class ZipReplace:

    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string
    
    def processs(self, proc):
        """
        Performs a search and replace on all files in the temporary directory.
        """
        for filename in proc.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)
