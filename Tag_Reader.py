import tinytag as tnytg
import os

cdir = "/storage/emulated/0/Playlist"

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


#fix indentation erorr
#for folderCheck in artist_Dict:
