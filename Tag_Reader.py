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

folderNames = artist_Dict.Keys()

#fix indentation erorr (?)
# this loop should move files from playlist to folder named as artists.
for folderCheck in folderNames:
  if len(artist_Dict[folderCheck]) >= 3 :
    os.mkdir(cdir+'/'+folderCheck)
    su.
  else:
    os.mkdir(other_dir+'/'+folderCheck)
    