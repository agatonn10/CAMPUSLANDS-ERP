from modules.utils import load_data, save_data


def menu():
    while True:
        print("======= GESTION DE REPORTES =======")
        print("1) Registrar reportes al camper")
        print("2) Listar reportes")
        print("0) Volver")
        print("===================================")

        opcion = input("seleccione algo: ")

        match opcion:
            case "1":
                register_report()
            case "2":
                list_report()
            case "0":
                print("saliendo del menu")
                return
            case _:
                print("seleccione algo valido...")

def register_report():
    data = load_data()
    campers = data.get("campers", [])
    reports = data.get("reports", [])

    if not campers:
        print("no hay campers registrados")
        return
    
    print("campers disponibles: ")
    for c in campers:
        print(f"{c['id']} - {c['nombre']} {c['apellido']}")

    try:
        camper_id = int(input("ingrese el id del camper: "))
    except ValueError:
        print("id invalido.")
        return
    
    camper = next((c for c in campers if c["id"] == camper_id), None)
    if not camper:
        print("no existe un camper con esta id")
        return
    
    nuevo_reporte = {
        "camper_id": camper_id,
        "camper_nombre": f"{camper['nombre']} {camper['apellido']}",
    }
    
    reports.append(nuevo_reporte)
    data["reports"] = reports
    save_data(data)

    print(f"reporte registrado para {camper['nombre']} {camper['apellido']}")

def list_report():
    data = load_data()
    reports = data.get("reports", [])

    if not reports:
        print("no hay reportes")
        return
    
    print("lista de reportes:")
    for r in reports:
        print(f"campers {r['camper_id']} - {r['camper_nombre']}")
                                            