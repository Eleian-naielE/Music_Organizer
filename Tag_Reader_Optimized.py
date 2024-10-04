from tinytag import TinyTag as tnytg
import os
import shutil as su
from collections import defaultdict


playlist = "/storage/emulated/0/Playlist"       # main music dir
playlist_Others = os.path.join(playlist, 'Others')      # others dir

os.makedirs(playlist_Others, exist_ok=True) # if there's no others dir, this makes one(might not need it?)


items = os.listdir(playlist) # scans playlist including directories
Files = [f for f in items if os.path.isfile(os.path.join(playlist, f))] # filters files only


artist_Dict = defaultdict(list) # dictionary containing files categorized by artist
others_genre_Dict = defaultdict(list) #


# file categorizes by artist. 
# ex) artist_Dict = {'artist A' : [dir of songA, dir of songB, dir of songC], 'Unknown Artist' : [...], ...} (songs are in form of directory)
for file in Files:
    file_path = os.path.join(playlist, file)
    artist_info = tnytg.get(file_path).artist or "Unknown Artist"
    artist_Dict[artist_info].append(file_path)

# Moves files to the directory names after the artist if the artist category has 3 or more songs
# if not, it moves to the others where it re-organizes under the its labeled genre
for artist, file_paths in artist_Dict.items():
    if len(file_paths) >= 3:                            # if the artist has 3 or more songs
        artist_dir = os.path.join(playlist, artist)
        os.makedirs(artist_dir, exist_ok=True)
        for src_mvd in file_paths:
            su.move(src_mvd, artist_dir)
    else:                                               # less than 3
        for other_audio in file_paths : 
            genre_info = tnytg.get(other_audio).genre
            genre_dir=os.path.join(playlist_Others, genre_info)
            os.makedirs(genre_dir, exist_ok=True)
            su.move(other_audio, genre_dir)