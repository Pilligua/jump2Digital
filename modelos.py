import datetime
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from database import *

class Skin(BaseModel):
    id: Optional[int]
    nombre: str
    descripcion: str
    tipo: str
    precio: float
    color: str
    disponible: bool
    
    def guardar(self):
        query = f"INSERT INTO skins(id, nombre, descripcion, tipo, precio, color, disponible) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE nombre='{self.nombre}', descripcion='{self.descripcion}', tipo='{self.tipo}', precio={self.precio}, color='{self.color}', disponible={self.disponible}"
        cursor.execute(query, (self.id, self.nombre, self.descripcion, self.tipo, self.precio, self.color, self.disponible))
        self.id = cursor.lastrowid
        conexion.commit()

    def borrar(self):
        cursor.execute(f"DELETE FROM skins WHERE id={self.id}")
        conexion.commit()
    
    def cambiarDisponibilidad(self):
        if(self.disponible==1):
            self.disponible=0
        else:
            self.disponible=1
        self.guardar()


class Usuario(BaseModel): 
    id: Optional[int]
    nombre: str
    apellidos: str
    email: str
    direccion: str
    telefono: int
    activo: bool
    fechaRegistrado: datetime.datetime
    
    def guardar(self):
        query = f"INSERT INTO usuario(id, nombre, apellidos, email,  direccion, telefono, activo, fechaRegistrado) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE nombre='{self.nombre}', apellidos='{self.apellidos}', email='{self.email}',  direccion='{self.direccion}', telefono={self.telefono}, activo={self.activo}, fechaRegistrado={self.fechaRegistrado})"
        cursor.execute(query, (self.id, self.nombre, self.apellidos, self.email, self.direccion, self.telefono, self.activo, datetime.datetime.now()))
        self.id = cursor.lastrowid
        conexion.commit()
    
    def borrar(self):
        cursor.execute(f"DELETE FROM usuario WHERE id={self.id}")
        conexion.commit()
    

class skinsUsuario(BaseModel):
    id: Optional[int]
    idSkin: int
    idUsuario: int
    color: str
    fechaAdquisicion: datetime.datetime
    
    def guardar(self):
        query = f"INSERT INTO skinsusuario(id, idSkin, idUsuario, color,  fechaAdquisicion) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE color='{self.color}'"
        cursor.execute(query, (self.id, self.idSkin, self.idUsuario, self.color, self.fechaAdquisicion))
        self.id = cursor.lastrowid
        conexion.commit()

    def borrar(self):
        cursor.execute(f"DELETE FROM skinsusuario WHERE id={self.id}")
        conexion.commit()