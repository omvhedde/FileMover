import os
import sys
import time
import shutil
from watchdog import observers, events

sourceDir = '/home/omprasad/Downloads'
docDir ='/home/omprasad/Documents'
vidDir = '/home/omprasad/Videos'
imgDir = '/home/omprasad/Pictures/Images'
pkgDir = '/home/omprasad/Packages'
archDir = '/home/omprasad/Archives'

imgFormats = ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2']
vidFormats = ['.mp4', '.mkv', '.wmv', '.mov', '.avi', '.webm','.mp4v', '.m4v', '.flv', '.f4v', '.f4p', '.f4a', '.f4b']
docFormats = ['.doc','.pdf', '.ppt', '.pptx', '.txt', '.xls', '.xlsx', '.srt']
pkgFormats = ['.deb', '.pkg', '.whl', '.rpm']
archFormats = ['.zip', '.xz', '.tar', '.gz', '.rar', '.7z']

def moveFile(src, dest):
    if os.path.exists(f'{dest}/{src.name}'):
        os.remove(f'{dest}/{src.name}')
    shutil.move(f'{src.path}', f'{dest}/{src.name}')

class Handler(events.FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(sourceDir) as entries:
            for entry in entries:
                name, ext = os.path.splitext(entry.name)
                if os.path.isfile(entry.path):
                    if ext in imgFormats:
                        moveFile(entry, imgDir)
                    elif ext in vidFormats:
                        moveFile(entry, vidDir)
                    elif ext in docFormats:
                        moveFile(entry, docDir)
                    elif ext in pkgFormats:
                        moveFile(entry, pkgDir)
                    elif ext in archFormats:
                        moveFile(entry, archDir)
                    else:
                        pass

if __name__ == '__main__':
    observer = observers.Observer()
    observer.schedule(Handler(), sourceDir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
