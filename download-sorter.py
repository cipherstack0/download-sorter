from pathlib import Path
import shutil
import argparse

parser = argparse.ArgumentParser(usage="use flags -f or -p")
parser.add_argument("-f", "--file", help="file descriptor to sort into the Documents folder. e.g: pdf, txt ...")
parser.add_argument("-p", "--picture", help="file descriptor to sort into the Pictures folder. e.g: gif,jpeg...")

args = parser.parse_args()

src_download = Path.home() / "Downloads"
dst_files = Path.home() / "Documents"
dst_pictures = Path.home() / "Pictures"

# please add more filetypes of your choice
files = [".pdf", ".docx", ".txt"]
pictures = [".jpg", ".jpeg", ".png"]


def move_file(suffix, dst):
     for iter_suffix in suffix:
        for f in list(src_download.iterdir()):
            if f.suffix == iter_suffix:
                shutil.move(f, dst)    

if args.file:
    arg_files = args.file.split(",")
    if (arg_files):
        move_file(arg_files, dst_files)
    else:
        move_file(files,dst_files)


elif args.picture:
    arg_pictures = args.picture.split(",")
    if (arg_pictures):
        move_file(arg_pictures, dst_pictures)
    else:
        move_file(pictures, dst_pictures)

else:
    print("Nothing was moved")
