from modules.utils import load_data, save_data

def menu_coordinators():
    while True:
        print("======= GESTIÓN DE COORDINADORES =======")
        print("1) Registrar Coordinador")
        print("2) Listar Coordinadores")
        print("0) Volver al Menú")
        print("=======================================")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                register_coordinator()
            case "2":
                list_coordinators()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ SELECCIONA UNA OPCIÓN VÁLIDA.")
                return
            
def register_coordinator():
    data = load_data()
    data.setdefault("coordinators", [])

    print("======= REGISTRO DE COORDINADOR =======")

    coordinator = {
        "id": int(input("ID: ").strip()),
        "nombre": input("Nombre: ").strip(),
        "apellido": input("Apellido: ").strip(),
        "telefono": input("Teléfono: ").strip(),
        "estado": "Activo"
    }

    data["coordinators"].append(coordinator)
    save_data(data)

    print("✅ Coordinador registrado exitosamente.")
    print(f"ID: {coordinator['id']} | {coordinator['nombre']} {coordinator['apellido']} | "
          f"Tel: {coordinator['telefono']} | Estado: {coordinator['estado']}")

def list_coordinators():
    data = load_data()
    print("======= LISTADO DE COORDINADORES =======")
    for c in data.get("coordinators", []):
        print(f"ID: {c['id']} | {c['nombre']} {c['apellido']} | Tel: {c['telefono']} | Estado: {c['estado']}")
