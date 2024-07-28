import tinytag as tnytg
import os

cdir = "/storage/emulated/0/Playlist"

items = os.listdir(cdir)

files = [f for f in items if os.path.isfile(cdir+'/'+f)]

tnytg