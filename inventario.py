import json
import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_datos()

    def añadir_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_datos()

    def eliminar_producto(self, id_p):
        if id_p in self.productos:
            del self.productos[id_p]
            self.guardar_datos()

    def actualizar_producto(self, id_p, can=None, pre=None):
        if id_p in self.productos:
            if can is not None: self.productos[id_p].cantidad = can
            if pre is not None: self.productos[id_p].precio = pre
            self.guardar_datos()

    def buscar_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def obtener_todos(self):
        return self.productos.values()

    def guardar_datos(self):
        with open(self.archivo, 'w') as f:
            datos = {id_p: p.to_dict() for id_p, p in self.productos.items()}
            json.dump(datos, f, indent=4)

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    datos = json.load(f)
                    for d in datos.values():
                        p = Producto(d['id'], d['nombre'], d['cantidad'], d['precio'])
                        self.productos[p.id_producto] = p
            except: pass