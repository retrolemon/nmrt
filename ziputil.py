from zipfile import ZipFile

def unzipf(i, o):
    with ZipFile(i, "r") as z:
        z.extractall(o)
        z.close()
