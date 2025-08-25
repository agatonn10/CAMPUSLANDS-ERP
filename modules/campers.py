from modules.utils import load_data, save_data

def menu():
    while True:
        print("=======GESTIÓN DE CAMPERS=======")
        print("1) Registrar Camper")
        print("2) Listar Campers")
        print("0) Volver al Menú")
        print("===============================")
        
        try:
            opcion = input("Seleccione una opción: ")
        
        except ValueError:

            print("Error")
        
        match opcion:
            case "1":
                register_camper()    
            case "2":
                list_campers()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ SELECCIONA ALGO VALIDO... ")
                


def register_camper():
    data = load_data()
    print("=======REGISTRO DE CAMPER======="),
    camper = {
        "id": int(input("ID: ")),
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "direccion": input("Dirección: "),
        "acudiente": input("Nombre del acudiente: "),
        "telefono": int(input("Teléfono (#celular, #fijo): ")),
        "estado": "en proceso de estado...",
        "riesgo": "sin riesgo..."
    }
    data["campers"].append(camper)
    save_data(data)
    print("✅ Camper registrado exitosamente.")

def list_campers():
    data = load_data()
    for camper in data["campers"]:
        print(f"id: {camper['id']}, Nombre: {camper['nombre']} {camper['apellido']}, Acudiente: {camper['acudiente']}, Teléfono: {camper['telefono']}, Estado: {camper['estado']}, Riesgo: {camper['riesgo']}")