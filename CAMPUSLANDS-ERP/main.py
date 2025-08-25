from modules import campers, trainers, coordinators, routes, enrollments, evaluations, reports

def main():
    while True:
        print("=======CAMPUSLANDS MENU=======")
        print("1) Gestionar Campers")
        print("2) Gestionar Trainers")
        print("3) Gestionar Coordinadores")
        print("4) Gestionar Rutas")
        print("5) Matriculas")
        print("6) Evaluaciones")
        print("7) Reportes")
        print("0) Salir")
        print("=============================")
        
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                campers.menu()
            case "2":
                trainers.menu()
            case "3":
                coordinators.menu()
            case "4":
                routes.menu()
            case "5":
                enrollments.menu()
            case "6":
                evaluations.menu()
            case "7":
                reports.menu()
            case "0":
                print("👋 Saliendo del sistema...")
                break
            case _:
                print("❌ No seleccionaste NADA...")

if __name__ == "__main__":
    main()