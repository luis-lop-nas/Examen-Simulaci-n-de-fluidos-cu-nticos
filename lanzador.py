from src.repositorio import RepositorioDeEstados
from src.operador_cuantico import OperadorCuantico

def ejecutar():
    repo = RepositorioDeEstados()

    # Cargar estados desde archivo si existe
    try:
        repo.cargar("estados.json")
        print("Estados cargados desde archivo.")
    except FileNotFoundError:
        print("No se encontró el archivo de estados, empezamos desde cero.")

    # Ejemplo de uso:
    print("\nEstados actuales:")
    for linea in repo.listar_estados():
        print(linea)

    # Agregar un estado inicial
    try:
        repo.agregar_estado("q0", [1, 0], "computacional")
        print("\nEstado q0 agregado.")
    except ValueError as e:
        print(f"\n{e}")

    # Aplicar operador X
    puerta_x = OperadorCuantico("X", [[0, 1], [1, 0]])
    try:
        repo.aplicar_operador("q0", puerta_x, nuevo_id="q0_X")
        print("Operador X aplicado a q0.")
    except ValueError as e:
        print(f"{e}")

    # Medir estado resultante
    try:
        resultados = repo.medir_estado("q0_X")
        print("\nMedición de q0_X:")
        for i, p in enumerate(resultados):
            print(f"  Estado base {i}: {p*100:.2f}%")
    except ValueError as e:
        print(f"{e}")

    # Guardar estados
    repo.guardar("estados.json")
    print("\nEstados guardados en 'estados.json'.")
