"""
Módulo de repositorio de estados cuánticos.
Define la clase RepositorioDeEstados para gestionar el ciclo de vida
de los estados: alta, consulta, transformación, medición y persistencia.
"""

import json
from src.estado_cuantico import EstadoCuantico
from src.operador_cuantico import OperadorCuantico

class RepositorioDeEstados:
    """Gestiona el almacenamiento y operaciones sobre múltiples estados cuánticos."""
    def __init__(self):
        """Inicializa un repositorio vacío de estados."""
        self.estados = {}  # Estructura interna: dict {id: EstadoCuantico}

    def agregar_estado(self, id, vector, base):
        """
        Añade un nuevo estado al repositorio.
        :param id: identificador único del estado.
        :param vector: lista de amplitudes del estado.
        :param base: nombre de la base de representación.
        :raises ValueError: si ya existe un estado con el mismo id.
        """
        if id in self.estados:
            raise ValueError(f"Ya existe un estado con id '{id}'")
        # Crear y almacenar nuevo estado
        self.estados[id] = EstadoCuantico(id, vector, base)

    def listar_estados(self):
        """
        Retorna una lista de descripciones legibles de todos los estados.
        :return: List[str] con representaciones tipo "id: vector ...".
        """
        # Convertir cada estado en su forma de cadena
        return [str(estado) for estado in self.estados.values()]

    def obtener_estado(self, id):
        """
        Recupera un estado por su identificador.
        :param id: identificador del estado buscado.
        :return: EstadoCuantico o None si no existe.
        """
        return self.estados.get(id)

    def aplicar_operador(self, id_estado, operador: OperadorCuantico, nuevo_id=None):
        """
        Aplica un operador cuántico a un estado existente y guarda el resultado.
        :param id_estado: id del estado a transformar.
        :param operador: instancia de OperadorCuantico.
        :param nuevo_id: id opcional para el estado resultante.
        :raises ValueError: si el estado no existe o el nuevo_id ya está en uso.
        """
        # Buscar estado original
        estado = self.obtener_estado(id_estado)
        if estado is None:
            raise ValueError(f"No existe el estado con id '{id_estado}'")
        # Generar nuevo estado aplicando el operador
        nuevo_estado = operador.aplicar(estado)
        # Asignar identificador adecuado
        nuevo_estado.id = nuevo_id or nuevo_estado.id
        if nuevo_estado.id in self.estados:
            raise ValueError(f"Ya existe un estado con id '{nuevo_estado.id}'")
        # Almacenar el estado transformado
        self.estados[nuevo_estado.id] = nuevo_estado

    def medir_estado(self, id):
        """
        Realiza la medición teórica de un estado, devolviendo probabilidades.
        :param id: identificador del estado a medir.
        :return: lista de probabilidades normalizadas.
        :raises ValueError: si no existe el estado.
        """
        # Obtener y medir
        estado = self.obtener_estado(id)
        if estado is None:
            raise ValueError(f"No existe el estado con id '{id}'")
        return estado.medir()

    def guardar(self, archivo):
        """
        Guarda todos los estados actuales en un archivo JSON.
        :param archivo: ruta del archivo de destino.
        """
        try:
            with open(archivo, 'w') as f:
                json.dump(
                    [
                        {"id": est.id, "vector": est.vector, "base": est.base}
                        for est in self.estados.values()
                    ],
                    f,
                    indent=4
                )
        except IOError:
            print(f"Error: No se pudo guardar el archivo '{archivo}'. Verifica permisos o espacio en disco.")

    def cargar(self, archivo):
        """
        Carga estados desde un archivo JSON, reemplazando los existentes.
        :param archivo: ruta del archivo origen.
        """
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.estados = {}
                for est in datos:
                    self.agregar_estado(est["id"], est["vector"], est["base"])
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Advertencia: No se pudo cargar '{archivo}' (vacío, corrupto o inexistente). Se continuará con un repositorio vacío.")