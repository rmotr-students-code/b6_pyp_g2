class Open(object):
    
    def __init__(self, filename, flags):
        self.filename = filename
        self.flags = flags
        self.filehandle = None
        
    def __enter__(self):
        self.filehandle = open(self.filename, self.flags)
        return self.filehandle
    
    def __exit__(self, type, value, traceback):
        print("Closing file..")
        self.filehandle.close()


with Open('names.txt', 'r') as f:
    print(f.readline() + 2)