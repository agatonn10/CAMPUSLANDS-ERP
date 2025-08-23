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
                campers.menu_campers()
            case "2":
                trainers.menu_trainers()
            case "3":
                coordinators.menu_coordinators()
            case "4":
                routes.menu_routes()
            case "5":
                enrollments.menu_enrollments()
            case "6":
                evaluations.menu_evaluations()
            case "7":
                reports.menu_reports()
            case "0":
                print("👋 Saliendo del sistema...")
                break
            case _:
                print("❌ No seleccionaste NADA...")

if __name__ == "__main__":
    main()