import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS" : ['.pdf','.rtf','.txt'],
    "AUDIO" : ['.m4a','.m4b','.mp3'],
    "VIDEOS" : ['.mov','.avi','.mp4'],
    "IMAGES" : ['.jpg','.jpeg','.png']
}

def pickDictionary(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes :
            if suffix == value:
                return category
    return 'MISC'

def organizeDirectory():
    for item in os.scandir(): # scan a directory
        if item.is_dir(): 
            continue
        filePath = Path(item) # get a path of the item
        filetype = filePath.suffix.lower()
        directory = pickDictionary(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()