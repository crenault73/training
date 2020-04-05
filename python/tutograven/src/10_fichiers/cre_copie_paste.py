# Copié/collé de fichier
import os
import shutil

source = "logo.png"
target = "images/logo.png"

shutil.copy(source, target)
os.remove(source)