import os
import shutil
source = "meal.ico"
target = "image/meal.ico"

shutil.copy(source,target)
os.remove(source)