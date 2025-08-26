from modules.utils import load_data, save_data

def menu():
    while True:
        print("======= GESTIÓN DE RUTAS =======")
        print("1) Crear rutas")
        print("2) Listar rutas")
        print("3) Asignar campers")
        print("0) Volver")
        print("================================")

        opcion = input("👉 Ingrese una opción: ").strip()

        match opcion:
            case "1":
                create_R()
            case "2":
                list_R()
            case "3":
                assign_R()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ Selecciona una opción válida.")

# Crear rutas y gestionarlas
def create_R():
    data = load_data()
    routes = data.get("routes", [])

    nombre = input("📚 Ingresa el nombre de la ruta: ")
    duracion = input("⏳ Ingresa la duración (ej: 6 meses): ")
    modulos = input("📖 Ingresa los módulos separados por coma: ").split(",")

    nueva_ruta = {
        "id": str(len(routes) + 1),
        "nombre": nombre,
        "duracion": duracion,
        "modulos": [m.strip() for m in modulos],
        "campers_asignados": []
    }

    routes.append(nueva_ruta)
    data["routes"] = routes
    save_data(data)
    print(f"✅ Ruta '{nombre}' creada con éxito.")

# Ver las listas de las rutas
def list_R():
    data = load_data()
    routes = data.get("routes", [])

    if not routes:
        print('⚠️ No hay rutas registradas aún...')
        return

    print("\n📚 Listado de Rutas:")
    for r in routes:
        print(f"{r['id']} - {r['nombre']} ({r['duracion']})")
        print(f"   Módulos: {', '.join(r['modulos'])}")
        print(f"   Campers asignados: {len(r['campers_asignados'])}")
        print("-" * 40)

# Asignar campers a una ruta
def assign_R():
    data = load_data()
    campers = data.get("campers", [])
    routes = data.get("routes", [])
    aprobados = []

    # Listar campers aprobados
    print("\n👥 Campers aprobados:")
    for c in campers:
        if c['estado'] == 'Aprobado':
            print(f"{c['id']} - {c['nombre']} {c['apellidos']}")
            aprobados.append(c['id'])

    if not aprobados:
        print('⚠️ No hay campers aprobados para asignar...')
        return

    if not routes:
        print("⚠️ No hay rutas disponibles. Primero crea una ruta.")
        return

    camper_id = input("👉 Ingresa el ID del camper a asignar: ").strip()

    # Validar camper
    camper = next((c for c in campers if c['id'] == camper_id and c['estado'] == 'Aprobado'), None)
    if not camper:
        print("❌ Camper no encontrado o no está aprobado.")
        return

    print(f"👉 Deseas asignar a {camper['id']} - {camper['nombre']} {camper['apellidos']} ")
    asignar = input('Ingrese "S" para sí y "N" para no: ').strip().upper()

    if asignar != 'S':
        print("❌ No asignaste nada.")
        return

    # Mostrar rutas
    print("\n📚 Rutas disponibles:")
    for r in routes:
        print(f"{r['id']} - {r['nombre']}")

    route_id = input("👉 Ingresa el ID de la ruta a asignar: ").strip()
    ruta = next((r for r in routes if r['id'] == route_id), None)

    if not ruta:
        print("❌ Ruta no encontrada.")
        return

    if camper_id in ruta['campers_asignados']:
        print('❌ El camper ya está asignado a esta ruta.')
    else:
        ruta['campers_asignados'].append(camper_id)
        save_data(data)
        print(f"✅ Camper {camper['nombre']} asignado a la ruta {ruta['nombre']}.")
