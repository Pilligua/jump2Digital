import json
from main import *

with open("json/skinsjson.json") as archivo: 
    archivoJSON = json.load(archivo)
    
skinsDocumento = json.dumps(archivoJSON, sort_keys=True)
achivoLoads = json.loads(skinsDocumento)

for skin_data in archivoJSON["skin"]:
   skin = Skin(**skin_data)
   skin.guardar()