from modules.utils import load_data, save_data

def menu_trainers():
    while True:
        print("======= GESTIÓN DE TRAINERS =======")
        print("1) Registrar Trainer")
        print("2) Listar Trainers")
        print("0) Volver al Menú")
        print("===================================")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                register_trainer()    
            case "2":
                list_trainers()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ SELECCIONA ALGO VÁLIDO... ")
                return


def register_trainer():
    data = load_data()
    print("======= REGISTRO DE TRAINER =======")
    
    trainer = {
        "id": int(input("ID: ")),
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "especialidad": input("Especialidad (Java, NodeJS, .NET): "),
        "disponibilidad": input("Disponibilidad (lunes a viernes 8am-12pm): "),
    }

    data["trainers"].append(trainer)
    save_data(data)
    print("✅ Trainer registrado exitosamente.")


def list_trainers():
    data = load_data()
    print("\n===== LISTA DE TRAINERS =====")
    for trainer in data["trainers"]:
        print(f"ID: {trainer['id']}  Nombre: {trainer['nombre']} {trainer['apellido']} "
              f"Especialidad: {trainer['especialidad']} dispoibilidad: {trainer['disponibilidad']}")