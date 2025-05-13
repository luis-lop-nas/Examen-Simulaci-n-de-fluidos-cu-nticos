

import json
from src.estado_cuantico import EstadoCuantico
from src.operador_cuantico import OperadorCuantico

class RepositorioDeEstados:
    def __init__(self):
        self.estados = {}

    def agregar_estado(self, id, vector, base):
        if id in self.estados:
            raise ValueError(f"Ya existe un estado con id '{id}'")
        self.estados[id] = EstadoCuantico(id, vector, base)

    def listar_estados(self):
        return [str(estado) for estado in self.estados.values()]

    def obtener_estado(self, id):
        return self.estados.get(id)

    def aplicar_operador(self, id_estado, operador: OperadorCuantico, nuevo_id=None):
        estado = self.obtener_estado(id_estado)
        if estado is None:
            raise ValueError(f"No existe el estado con id '{id_estado}'")
        nuevo_estado = operador.aplicar(estado)
        nuevo_estado.id = nuevo_id or nuevo_estado.id
        if nuevo_estado.id in self.estados:
            raise ValueError(f"Ya existe un estado con id '{nuevo_estado.id}'")
        self.estados[nuevo_estado.id] = nuevo_estado

    def medir_estado(self, id):
        estado = self.obtener_estado(id)
        if estado is None:
            raise ValueError(f"No existe el estado con id '{id}'")
        return estado.medir()

    def guardar(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(
                [
                    {"id": est.id, "vector": est.vector, "base": est.base}
                    for est in self.estados.values()
                ],
                f,
                indent=4
            )

    def cargar(self, archivo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            self.estados = {}  # Limpiamos antes de cargar
            for est in datos:
                self.agregar_estado(est["id"], est["vector"], est["base"])