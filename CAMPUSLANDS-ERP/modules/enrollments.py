from json import load
from modules.utils import load_data, save_data

def menu():
    while True:
        print("======= GESTION DE MATRICULAS =======")
        print("1) crear matriculas")
        print("2) listar matriculas")
        print("0) volver")
        print("=====================================")
        
        try:
            opcion = input("ingrese una opcion: ")
        
        except ValueError:

            print('Error')
         
        match opcion:
            case "1":
                create_M()
            case "2":
                list_M()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ SELECCIONA ALGO VALIDO... ")
                
#crear las Matriculas              
def create_M():
    data = load_data()
    campers = data.get("campers")
    routes = data.get("routes")
    trainers = data.get("trainers")
    enrollment = data.get("enrollment")


#la lista de las matriculas            
def list_M():
    pass