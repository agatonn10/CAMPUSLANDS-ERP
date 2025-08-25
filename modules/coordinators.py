from modules.utils import load_data, save_data

def menu():
    while True:
        print("======= GESTIÓN DE COORDINADORES =======")
        print("1) Evaluar al Camper")
        print("2) Listar Campers en proceso de ingreso")
        print("0) Volver")
        print("========================================")
        
        try:
            opcion = input("Seleccione una opción: ")

        except ValueError:
            
            print("Error")
        
        match opcion:
            case "1":
                evaluate_coordinator()    
            case "2":
                list_coordinators()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ SELECCIONA ALGO VALIDO... ")
                
        
def evaluate_coordinator():
    data = load_data()
    print("=======EVALUAR AL CAMPER======="),
    id_camper = int(input("ID del camper a evaluar: "))
    for camper in data["campers"]:
        if camper["id"] == id_camper:
            print(f"Evaluando al camper: {camper['nombre']} {camper['apellido']}")
            estado ="en proceso"
            match input("Estado (1)aprobado/2)rechazado/3)en proceso): "):
                case "1":
                    estado = "aprobado"
                case "2":
                    estado = "rechazado"
                case "3":
                    estado = "en proceso"
                case _:
                    print("❌ Estado no valido, cambios no aplicados"),
            
            riesgo = "sin riesgo"
            match input("1)alto/2)medio/3)bajo/4)sin riesgo): "):
                case "1":
                    riesgo = "alto"
                case "2":
                    riesgo = "medio"
                case "3":
                    riesgo = "bajo"
                case "4":
                    riesgo = "sin riesgo"
                case _:
                    print("❌ Riesgo no valido, cambios no aplicados"),
            

            camper["estado"] = estado
            camper["riesgo"] = riesgo
            save_data(data)
            print("✅ Evaluación registrada exitosamente.")
            return
    print("❌ No se creo un camper con esa ID.")

def list_coordinators():
    data = load_data()
    print("=======CAMPERS EN PROCESO DE INGRESO=======")
    for camper in data["campers"]:
        if camper["estado"] == "en proceso":
            print(f"id: {camper['id']}, Nombre: {camper['nombre']} {camper['apellido']}, Acudiente: {camper['acudiente']}, Teléfono: {camper['telefono']}, Estado: {camper['estado']}, Riesgo: {camper['riesgo']}")