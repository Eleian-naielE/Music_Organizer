from tinytag import TinyTag as tnytg
import os
import shutil as su
from collections import defaultdict


def init():
    
    global musicPath, path_files, path_unfiltered
    musicPath = os.getcwd()
    path_unfiltered = os.listdir()
    path_files = [f for f in path_unfiltered if os.path.isfile(os.path.join(musicPath, f))] # filters files only
    artist_Dict = defaultdict(list)