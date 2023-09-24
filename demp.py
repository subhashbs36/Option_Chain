import os
import zipfile

zf = zipfile.ZipFile("myzipfile.zip", "w")
a = r"E:\Apowersoft Screen Recorder Pro"
for dirname, subdirs, files in os.walk(a):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
