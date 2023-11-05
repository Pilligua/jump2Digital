import datetime
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from modelos import *
from sistema import *

app = FastAPI()


#http://127.0.0.1:8000

@app.get("/")
def index():
    return "Prova backend jump2digital :). Alba Pilligua Costa"

#Devuelve una lista de todas las skins disponibles para comprar.
@app.get("/skins/avaible")
def getSkinsDisponibles():
    cursor.execute("SELECT * FROM skins WHERE disponible = 1")
    resultado = cursor.fetchall()
    if(resultado is not None):
        return [Skin(**dict(zip(["id", "nombre", "descripcion", "tipo", "precio", "color", "disponible"], valores))) for valores in resultado]
    else:
        return {"message": "No quedan skins disponibles para comprar"}

#Devuelve una lista de las skins compradas por el usuario
@app.get("/skins/myskins/")
def getSkinsUsuario(idUsuario:int):
    query = "SELECT * FROM skinsusuario WHERE idUsuario = %s"
    cursor.execute(query, (idUsuario,))
    resultado = cursor.fetchall()
    if(resultado is not None):
        return [skinsUsuario(**dict(zip(["id", "idSkin", "idUsuario", "color", "fechaAdquisicion"], valores))) for valores in resultado]
    else:
        return {"message": "No tienes skins compradas"}
    
#Devuelve una determinada skin.
@app.get("/skin/getskin/")
def getSkin(id:int):
    query = "SELECT * FROM skins WHERE id = %s"
    cursor.execute(query, (id,))
    resultado = cursor.fetchone()
    if(resultado is not None):
        return Skin(**dict(zip(["id", "nombre", "descripcion", "tipo", "precio", "color", "disponible"], resultado)))
    else:
        return {"message": "No existe ninguna skin con ese id"}

#Elimina una skin de invientario.
@app.delete("/skins/delete/")
def borrarSkin(idSkinUsuario:int):
    skinusuarioTemp= get_SkinUsuario(idSkinUsuario)
    if(skinusuarioTemp is not None):
        skinTemp = get_Skin(skinusuarioTemp.idSkin)
        skinusuarioTemp.borrar()
        skinTemp.cambiarDisponibilidad()
        return {"message": "Se ha eliminado correctamente de tu inventario la skin "+ skinTemp.nombre}
    else:
        return {"message": "No existe, prueba con otro id"}

#- Permite a los usuarios cambiar el color de una skin comprada.
@app.put("/skins/color/")
def cambiarColor(idSkinUsuario:int, color:str):
    skinusuarioTemp= get_SkinUsuario(idSkinUsuario)
    if(skinusuarioTemp is not None):
        if(color != None or ""):
            skinTemp = get_Skin(skinusuarioTemp.idSkin)
            skinusuarioTemp.color = color
            skinusuarioTemp.guardar()
            return {"message": "Se ha cambiado el color correctamente. La skin "+ skinTemp.nombre + " ahora es de color "+ skinusuarioTemp.color}
        else:
            return {"message": "Inserta un color por favor."}
    else: 
        return {"message": "No existe, prueba con otro id"}

#- Permite a los usuarios adquirir una skin y guardarla en la base de datos.
@app.post("/skins/buy/")
def comprarSkin(idSkin:int, idUsuario:int):
    skinTemp = get_Skin(idSkin)
    usuarioTemp = get_Usuario(idUsuario)
    if(skinTemp is not None and usuarioTemp is not None):
        if(skinTemp.disponible== 1):
            skinsUsuarioTemp= skinsUsuario(id=None, idSkin=skinTemp.id, idUsuario=usuarioTemp.id, color=skinTemp.color, fechaAdquisicion=datetime.datetime.now())
            skinsUsuarioTemp.guardar()
            skinTemp.cambiarDisponibilidad()
            return {"message": "Se ha añadido al inventario de "+ usuarioTemp.nombre + " la skin " + skinTemp.nombre}
        else:
            return {"message": "La skin " + skinTemp.nombre + " no está disponible para comprar"}
    else:
        return {"message": "Los datos introducidos son incorrectos."}