import tinytag as tnytg
import os
import shutil as su

cdir = "/storage/emulated/0/Playlist"

other_dir = cdir+'/Others'

items = os.listdir(cdir)

Files = [f for f in items if os.path.isfile(cdir+'/'+f)]

artist_Dict={}

for file in Files :
    tag=tnytg.get(file)
    artist_info=tag.artist
    
    if artist_info in artist_Dict :
        artist_Dict.get(artist_info).append(file)
    else : 
        artist_Dict[artist_info] = [file,]

folderNames = artist_Dict.keys()

#fix indentation erorr (?)
# this loop should move files from playlist to folder named as artists if the artist has more than 3 tracks
for folderCheck in folderNames:
    if len(artist_Dict[folderCheck]) >= 3 :
      artist_dir=os.mkdir(cdir+'/'+folderCheck)
      for src_mvd in artist_Dict[folderCheck]:
         su.move(src_mvd, dst_dir)
    else:
      #other_subdir=os.mkdir(other_dir)
      for src_mvd in artist_Dict[folderCheck]:
         su.move(src_mvd, other_dir)     