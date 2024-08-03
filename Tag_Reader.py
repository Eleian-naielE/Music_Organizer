from tinytag import TinyTag as tnytg
import os
import shutil as su

playlist = "/storage/emulated/0/Playlist"
playlist_Others = os.path.join(playlist, 'Others')


if not os.path.exists(playlist_Others):
    os.mkdir(playlist_Others)

items = os.listdir(playlist)
Files = [f for f in items if os.path.isfile(os.path.join(playlist, f))]

artist_Dict = {}

for file in Files:
    file_path = os.path.join(playlist, file)
    tag = tnytg.get(file_path)
    artist_info = tag.artist
    
    if artist_info in artist_Dict:
        artist_Dict[artist_info].append(file_path)
    else:
        artist_Dict[artist_info] = [file_path]

folderName_Candidates = artist_Dict.keys()


for folderNameCheck in folderName_Candidates:
    if len(artist_Dict[folderNameCheck]) >= 3:
        artist_dir = os.path.join(playlist, folderNameCheck)
        if not os.path.exists(artist_dir):
            os.mkdir(artist_dir)
        for src_mvd in artist_Dict[folderNameCheck]:
            su.move(src_mvd, artist_dir)
    else:
        for src_mvd in artist_Dict[folderNameCheck]:
            su.move(src_mvd, playlist_Others)