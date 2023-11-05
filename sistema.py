from modelos import *
from database import *

def get_Skin(id):
    query = "SELECT * FROM skins WHERE id = %s"
    cursor.execute(query, (id,))
    resultado = cursor.fetchone()
    if(resultado is not None):
        return Skin(**dict(zip(["id", "nombre", "descripcion", "tipo", "precio", "color", "disponible"], resultado)))

def get_Usuario(id):
    query = "SELECT * FROM usuario WHERE id = %s"
    cursor.execute(query, (id,))
    resultado = cursor.fetchone()
    if(resultado is not None):
        return Usuario(**dict(zip(["id", "nombre", "apellidos", "email", "direccion", "telefono", "activo", "fechaRegistrado"], resultado)))
    else:
        return None
    
def get_SkinUsuario(id):
    query = "SELECT * FROM skinsusuario WHERE id = %s"
    cursor.execute(query, (id,))
    resultado = cursor.fetchone()
    if(resultado is not None):
        return skinsUsuario(**dict(zip(["id", "idSkin", "idUsuario", "color", "fechaAdquisicion"], resultado)))
    else:
        return None