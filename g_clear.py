import winshell
import os
import shutil
import glob

def main():

    folders = ["icons_pics", "Executables", "Readable"]

    # Looping against the list to create the folders if not existed 
    for folder in folders:
        os.makedirs(fr"C:\Users\Hassa\Downloads\{folder}",exist_ok=True)

    # Packing the paths and the extensions in a dictionary
    destinations_extensions = {
        r"C:\Users\Hassa\Downloads\icons_pics": ["jpg", "png", "jpeg", "gif"],
        r"C:\Users\Hassa\Downloads\Executables": ["exe", "msi"],
        r"C:\Users\Hassa\Downloads\Readable": ["pdf", "doc", "docx"],
        r"C:\Users\Hassa\Videos": ["mp4", "mkv", "srt"]
    }

    # Unpacking it
    for destination, extension in destinations_extensions.items():
        for ex in extension:
                # The globe function finds all the files that ends with a specific extension
            for source in glob.glob(fr"C:\Users\Hassa\Downloads\*.{ex}"):
                shutil.move(source, destination)

    # Clear the recycle bin
    recycle_bin_items = winshell.recycle_bin()

    # Cumputing the junks
    junks = 0
    for junk in recycle_bin_items:
        junks += 1

    if junks == 0:
        return
    recycle_bin_items.empty(False, False, False)
     
if __name__ == "__main__":
    main()  
    