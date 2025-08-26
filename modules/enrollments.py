from modules.utils import load_data, save_data

# ================== MENÚ PRINCIPAL DE MATRÍCULAS ==================
def menu():
    while True:
        print("======= GESTIÓN DE MATRÍCULAS =======")
        print("1) Crear matrícula")
        print("2) Listar matrículas")
        print("0) Volver")
        print("=====================================")

        opcion = input("👉 Ingrese una opción: ")

        match opcion:
            case "1":
                create_M()
            case "2":
                list_M()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ Selecciona una opción válida.")


# ================== CREAR MATRÍCULAS ==================
def create_M():
    data = load_data()
    campers = data.get("campers", [])
    routes = data.get("routes", [])
    trainers = data.get("trainers", [])
    enrollments = data.get("enrollments", [])

    disponibles = []

    # Listar campers aprobados con ruta asignada y que NO tengan matrícula
    print("\n👨‍🎓 Campers aprobados con ruta asignada:")
    for c in campers:
        for r in routes:
            if c["estado"] == "Aprobado" and c["id"] in r["campers_asignados"]:
                # verificar si ya está matriculado
                if not any(e['camper_id'] == c['id'] for e in enrollments):
                    print(f"{c['id']} - {c['nombre']} {c['apellidos']} (Ruta: {r['nombre']})")
                    disponibles.append(c)

    if not disponibles:
        print("⚠️ No hay campers disponibles para matricular.")
        return

    if not routes:
        print("⚠️ No hay rutas registradas.")
        return

    if not trainers:
        print("⚠️ No hay trainers registrados.")
        return

    # Selección del camper
    try:
        camper_id = int(input("👉 Ingresa el ID del camper a matricular: "))
    except ValueError:
        print("❌ ID inválido.")
        return

    camper_seleccionado = next((c for c in disponibles if c["id"] == camper_id), None)
    if not camper_seleccionado:
        print("❌ Camper no válido o ya matriculado.")
        return

    # Ruta correspondiente
    ruta_asignada = next((r for r in routes if camper_id in r["campers_asignados"]), None)
    if not ruta_asignada:
        print("❌ El camper no tiene ruta asignada.")
        return

    # Trainers ocupados
    trainers_ocupados = [e["trainer_id"] for e in enrollments]

    # Mostrar solo trainers libres
    print("\n👨‍🏫 Trainers disponibles:")
    trainers_disponibles = [t for t in trainers if t["id"] not in trainers_ocupados]

    if not trainers_disponibles:
        print("⚠️ No hay trainers disponibles.")
        return

    for t in trainers_disponibles:
        print(f"{t['id']} - {t['nombre']} {t['apellidos']} (Especialidad: {t['especialidad']})")

    try:
        trainer_id = int(input("👉 Ingresa el ID del trainer: "))
    except ValueError:
        print("❌ ID inválido.")
        return

    trainer_seleccionado = next((t for t in trainers_disponibles if t["id"] == trainer_id), None)
    if not trainer_seleccionado:
        print("❌ Trainer no válido o ya está ocupado.")
        return

    # Asignar salón
    salon = input("🏫 Ingresa el salón asignado: ")

    # Crear matrícula
    nueva_matricula = {
        "camper_id": camper_seleccionado["id"],
        "camper_nombre": camper_seleccionado["nombre"],
        "route_nombre": ruta_asignada["nombre"],
        "trainer_id": trainer_seleccionado["id"],
        "trainer_nombre": trainer_seleccionado["nombre"],
        "salon": salon
    }

    enrollments.append(nueva_matricula)
    data["enrollments"] = enrollments
    save_data(data)

    print(f"✅ Camper {camper_seleccionado['nombre']} matriculado en {ruta_asignada['nombre']} "
          f"con el trainer {trainer_seleccionado['nombre']} en el salón {salon}")


# ================== LISTAR MATRÍCULAS ==================
def list_M():
    data = load_data()
    enrollments = data.get("enrollments", [])
    routes = data.get("routes", [])

    if not enrollments:
        print("⚠️ No hay matrículas registradas aún.")
        return

    print("\n--- Lista de Matrículas por Ruta ---")

    # Agrupar por ruta
    rutas = {}
    for e in enrollments:
        rutas.setdefault(e["route_nombre"], []).append(e)

    # Mostrar rutas y campers
    for ruta, lista in rutas.items():
        detalles = next((r for r in routes if r["nombre"] == ruta), None)

        if detalles:
            print(f"\n📚 Ruta: {detalles['nombre']} | Duración: {detalles['duracion']}")
            print("   📘 Módulos:", ", ".join(detalles["modulos"]))
        else:
            print(f"\n📚 Ruta: {ruta}")

        for e in lista:
            print(f"   👨‍🎓 Camper: {e['camper_nombre']} | Trainer: {e.get('trainer_nombre', 'No asignado')} | "
                  f"Salón: {e.get('salon', 'No asignado')}")
