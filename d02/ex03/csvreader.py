class CsvReader():
    def __init__(self,
                 filename,
                 sep=',',
                 header=False,
                 skip_top=0,
                 skip_bottom=0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.filename = filename
        self.mode = 'r'
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.nlines = len(self.file.readlines())
        self.file.seek(0)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def getdata(self):
        data = []
        self.file.seek(0)
        if self.header is False:
            self.file.readline()
        for i in range(self.skip_top):
            self.file.readline()
        for i in range(self.nlines - self.skip_top - self.skip_bottom):
            data.extend(self.file.readline().split(self.sep))
        return data

    def getheader(self):
        self.file.seek(0)
        return self.file.readline()


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
    print(data)
    print()
    print(header)
