from tinytag import TinyTag as tnytg
import os
import shutil as su

cdir = "/storage/emulated/0/Playlist"
other_dir = os.path.join(cdir, 'Others')


if not os.path.exists(other_dir):
    os.mkdir(other_dir)

items = os.listdir(cdir)
Files = [f for f in items if os.path.isfile(os.path.join(cdir, f))]

artist_Dict = {}

for file in Files:
    file_path = os.path.join(cdir, file)
    tag = tnytg.get(file_path)
    artist_info = tag.artist
    
    if artist_info in artist_Dict:
        artist_Dict[artist_info].append(file_path)
    else:
        artist_Dict[artist_info] = [file_path]

folderNames = artist_Dict.keys()


for folderCheck in folderNames:
    if len(artist_Dict[folderCheck]) >= 3:
        artist_dir = os.path.join(cdir, folderCheck)
        if not os.path.exists(artist_dir):
            os.mkdir(artist_dir)
        for src_mvd in artist_Dict[folderCheck]:
            su.move(src_mvd, artist_dir)
    else:
        for src_mvd in artist_Dict[folderCheck]:
            su.move(src_mvd, other_dir)