from pathlib import Path
import shutil

src_download = Path.home() / "Downloads"
dst_files = Path.home() / "Documents"
dst_pictures = Path.home() / "Pictures"

# print(dst_files)            # what path is it actually looking at?
# print(dst_files.exists())   # does it exist?
# print(list(dst_files.iterdir()))  # anything inside?
# for item in dst_files.glob('*'):
#    print(item)
for suffix in (".pdf", ".docx", ".txt"):
    for f in list(src_download.iterdir()):
        if f.suffix == suffix:
            shutil.move(f, dst_files)

