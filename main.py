import PIL
from PIL import Image,ExifTags
from PIL.ExifTags import TAGS
import os

def displayexif(image):
    e=image.getexif()
    if not e:
        print("None")
        return
    for tagid in e:
        name=TAGS.get(tagid,tagid)
        val=e.get(tagid)
        if isinstance(val,bytes):
            val=val.decode()
        print("{}:{}".format(name,val))

def main():
    imgpath=input("Enter the path to the pdf file: ")
    if not os.path.exists(imgpath):
        print("File not found")
        return
    img=Image.open(imgpath)

    print("Existing data: ")
    displayexif(img)
    print("----------------------------------")
    pdata=list(img.getdata())
    copy=Image.new(img.mode,img.size)
    copy.putdata(pdata)
    f=str(img.format)
    f=f.lower()
    copy.save("output."+f,format=f)
    print("Data in output file:")
    displayexif(copy)
    print("----------------------------------")
    print("Output file stored in current working directory")

if __name__=="__main__":
    main()
