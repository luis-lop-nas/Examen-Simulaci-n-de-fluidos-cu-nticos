# Examen - Simulación de fluidos cuánticos

https://github.com/luis-lop-nas/Examen-Simulaci-n-de-fluidos-cu-nticos.git

Este proyecto es una simulación simplificada de conceptos básicos de mecánica cuántica usando Python y programación orientada a objetos (POO). El objetivo principal es modelar estados cuánticos, operadores y procesos de medición dentro de un sistema modular, extensible y profesionalmente organizado.

## Resumen del ejercicio

El programa permite:
- Registrar y listar **estados cuánticos** definidos por vectores de amplitudes complejas en una base dada.
- Aplicar **operadores cuánticos** (puertas lógicas como X o Hadamard) sobre estos estados.
- Calcular las **probabilidades teóricas** al medir un estado cuántico.
- **Persistir** el conjunto de estados en un archivo `JSON` para conservarlos entre sesiones.
- Realizar pruebas unitarias para validar la funcionalidad del sistema.

Todo esto se hace sin interfaz gráfica, únicamente mediante consola o ejecución de scripts.

## Estructura del proyecto

```
.
├── main.py                 # Punto de entrada, solo llama al lanzador
├── lanzador.py            # Orquesta la ejecución general
├── src/                   # Código fuente principal
│   ├── estado_cuantico.py     # Clase EstadoCuantico
│   ├── operador_cuantico.py   # Clase OperadorCuantico
│   └── repositorio.py         # Clase RepositorioDeEstados
├── tests/                 # Pruebas unitarias
│   ├── test_estado_cuantico.py
│   ├── test_operador_cuantico.py
│   └── test_repositorio.py
├── estados.json           # Archivo persistente de estados cuánticos
├── requirements.txt       # Dependencias externas
└── README.md              # Esta documentación
```

Esta organización separa claramente:
- Código fuente (`src/`)
- Entrada principal (`main.py` + `lanzador.py`)
- Pruebas (`tests/`)
- Recursos del proyecto (`estados.json`, `README.md`, etc.)

## Explicación detallada

### `main.py`
Archivo mínimo que simplemente llama a `lanzador.ejecutar()`. Permite ejecutar todo el programa con `python main.py`.

### `lanzador.py`
Se encarga de:
- Cargar estados previos desde `estados.json` si existe.
- Agregar un estado inicial.
- Aplicar un operador cuántico de ejemplo (puerta X).
- Medir el estado resultante.
- Guardar todos los estados actualizados.
Todo esto se muestra por consola para visualizar los resultados.

### `estado_cuantico.py`
Contiene la clase `EstadoCuantico`, que representa un estado individual.
- Atributos: `id`, `vector`, `base`.
- Método `medir()`: devuelve las probabilidades teóricas de cada resultado posible.
- Método `__str__()`: devuelve una representación legible del estado.

### `operador_cuantico.py`
Define la clase `OperadorCuantico`, que representa una matriz unitaria como operador.
- Atributos: `nombre`, `matriz`.
- Método `aplicar(estado)`: aplica la transformación al vector del estado y devuelve un nuevo `EstadoCuantico`.

### `repositorio.py`
Clase `RepositorioDeEstados`:
- Gestiona todos los estados registrados.
- Métodos:
  - `agregar_estado()`: añade un nuevo estado si no existe.
  - `listar_estados()`: muestra todos los estados actuales.
  - `obtener_estado()`: recupera un estado por id.
  - `aplicar_operador()`: transforma un estado con un operador y lo guarda.
  - `medir_estado()`: mide un estado y muestra sus probabilidades.
  - `guardar()` y `cargar()`: persistencia en archivo JSON.

### `tests/`
Contiene pruebas automatizadas con `unittest`:
- Verifica que los cálculos cuánticos y validaciones funcionen correctamente.
- Asegura que el código esté libre de errores básicos y sea mantenible.

### `estados.json`
Archivo donde se guardan los estados cuánticos entre sesiones. Formato JSON estándar.

### `requirements.txt`
Incluye:
```
numpy
pytest
```

Puedes instalar dependencias con:
```bash
pip install -r requirements.txt
```

## Cómo ejecutar

1. Asegúrate de tener Python 3 y pip.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```
4. Para correr los tests:
   ```bash
   python -m unittest discover tests
   ```

---
Proyecto realizado como ejercicio de simulación de física cuántica con enfoque en programación orientada a objetos.