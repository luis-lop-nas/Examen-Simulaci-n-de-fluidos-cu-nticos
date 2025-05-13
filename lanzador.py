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

    while True:
        print("\n=== MENÚ CUÁNTICO ===")
        print("1. Ver estados registrados")
        print("2. Agregar nuevo estado")
        print("3. Aplicar puerta X a un estado")
        print("4. Aplicar puerta Hadamard (H) a un estado")
        print("5. Medir estado")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            estados = repo.listar_estados()
            if not estados:
                print("No hay estados registrados.")
            else:
                for est in estados:
                    print(est)

        elif opcion == "2":
            try:
                id = input("ID del nuevo estado: ")
                vector_str = input("Vector (ej: 1,0 o 0.707+0j,0.707+0j): ")
                base = input("Base del estado: ")
                vector = [complex(x.strip()) for x in vector_str.split(",")]
                repo.agregar_estado(id, vector, base)
                print(f"Estado {id} agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar estado: {e}")

        elif opcion == "3":
            try:
                id_original = input("ID del estado a transformar: ")
                nuevo_id = input("Nuevo ID para el estado transformado: ")
                puerta_x = OperadorCuantico("X", [[0, 1], [1, 0]])
                repo.aplicar_operador(id_original, puerta_x, nuevo_id=nuevo_id)
                print(f"Puerta X aplicada a {id_original}. Nuevo estado: {nuevo_id}")
            except Exception as e:
                print(f"Error al aplicar operador: {e}")

        elif opcion == "4":
            try:
                id_original = input("ID del estado a transformar: ")
                nuevo_id = input("Nuevo ID para el estado transformado: ")
                h = 1 / (2 ** 0.5)
                puerta_h = OperadorCuantico("H", [[h, h], [h, -h]])
                repo.aplicar_operador(id_original, puerta_h, nuevo_id=nuevo_id)
                print(f"Puerta Hadamard aplicada a {id_original}. Nuevo estado: {nuevo_id}")
            except Exception as e:
                print(f"Error al aplicar operador Hadamard: {e}")

        elif opcion == "5":
            try:
                id = input("ID del estado a medir: ")
                resultados = repo.medir_estado(id)
                print(f"Medición de {id}:")
                for i, p in enumerate(resultados):
                    print(f"  Estado base {i}: {p*100:.2f}%")
            except Exception as e:
                print(f"Error al medir: {e}")

        elif opcion == "6":
            repo.guardar("estados.json")
            print("Estados guardados. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")
