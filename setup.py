from download import bdownload
from shutil import copyfile
from ziputil import unzipf
from os import makedirs
import nmrt

lzs = """comtype lzss0
idstring "SSZL"
goto 8
get ZSIZE long
get SIZE long
savepos OFFSET
get NAME basename
string NAME + ".arc"
clog NAME OFFSET ZSIZE SIZE
"""

arc = """idstring "VCRA"
get FILES long
goto 0x40
math NAMESZ = 56
for i = 0 < FILES
    get OFFSET long
    get SIZE long
    getdstring NAME NAMESZ
    log NAME OFFSET SIZE
next i
"""

bdownload([["https://aluigi.altervista.org/papers/quickbms.zip", "quickbms.zip"]])
unzipf(".\\_dl\\quickbms.zip", ".\\_dl")

copyfile(".\\_dl\\quickbms.exe", ".\\quickbms.exe")

with open("namco_sszl.bms", "w") as bms:
    bms.write(lzs)
    bms.close()

with open("namco_vcra.bms", "w") as bms:
    bms.write(arc)
    bms.close()

dirstm = ["_lzs", "_arc", "_unpacked"]

for dirtm in dirstm:
    makedirs(dirtm, exist_ok = True)

nmrt.extract("resource.lzs")
