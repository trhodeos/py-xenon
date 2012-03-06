"""
All information used to construct these containers can be found here:
  - http://free60.org/old/Generic_Xbox_360_File_Container.html
"""

import os

class LiveContainer:
    def set_directory(self, dir):
        for root, dirs, files in os.walk(dir):
            for file in files:
                pass
        self.directory = dir

    def set_title(self, title):
        if (len(title) >= 256):
            title = title[:256]
        assert(len(title) < 256)
        self.title = title

    def write_header(self, file):
        """
        Write the header information (minus any hashes) to file.
        file - file to write into.
        """
        # magic int
        file.seek(0x0)
        file.write('LIVE')

        # content type
        file.seek(0x344)
        file.write("\x00\x00\x70\x00") # XNA Community / xbox title

        # title
        file.seek(0x410)
        file.write(self.title)

        # icons
        file.seek(0x1712) # length of big icon
        file.write("\x00\x00\x00\x00") # temporarily 0

        file.seek(0x1716) # length of small icon
        file.write("\x00\x00\x00\x00") # temporarily 0

    def write_files(self, file):
        pass

    def write(self, filename):
        # open up the file
        file = open(filename, 'wb')

        # write header info
        self.write_header(file)

        # write content info
        self.write_files(file)

        # close up shop
        file.close()
