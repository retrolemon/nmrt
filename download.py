from requests import get
from os import makedirs

def bdownload(entries):
    makedirs(".\\_dl", exist_ok = True)
    for entry in entries:
        open(".\\_dl\\" + entry[1], "wb").write(get(entry[0], allow_redirects=True).content)
