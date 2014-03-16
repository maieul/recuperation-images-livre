# les imports
from config import *
import urllib.request
import roman
import os
# le code

## création du dossier
try:
    os.mkdir(dossier)
except:
    pass

## récupération de chaques images
i = min
while i <= max:
    try:   
        if romain:
            url = base.format(nombre=roman.toRoman(i).lower)
            name = roman.toRoman(i).lower()
        else:
            url = base.format(nombre=str(i).zfill(complete))
            name = str(i).zfill(len(str(max)))
        fichier =  os.path.join(dossier,name+extension)
        print (fichier)
        print (url)
        
        http = urllib.request.urlopen(url)
        file = open(fichier,"wb")
        file.write(http.read())
        file.close()
    except:
        pass
    i = i + 1
