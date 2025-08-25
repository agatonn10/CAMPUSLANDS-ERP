from modules.utils import load_data, save_data

def menu():
    while True:
        print("======= GESTION DE RUTAS =======")
        print("1) crear  rutas")
        print("2) listar rutas")
        print("0) volver")
        print("================================")

        try:
            opcion = print("ingrese una opcion: ")
        
        except ValueError:

            print("Error")

        match opcion:
            case "1":
                create_R()
            case "2":
                list_R()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ SELECCIONA ALGO VALIDO... ")

#crear las rutas y gestionarlas
def create_R():
    pass
        

#ver las listas de las rutas
def list_R():
    pass

data = load_data
print("===== LISTA DE RUTAS =====")
