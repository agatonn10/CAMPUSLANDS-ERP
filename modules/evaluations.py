from modules.utils import save_data, load_data

def menu():
    while True:
        print("======= GESTION DE EVALUACIONES =======")
        print("1) Registrar evaluación")
        print("2) Listar evaluaciones")
        print("0) Volver")
        print("=======================================")

        opcion = input("👉 Ingrese una opción: ")

        match opcion:
            case "1":
                register_evaluations()
            case "2":
                list_evaluations()
            case "0":
                print("👋 Volviendo al menú principal...")
                return
            case _:
                print("❌ Selecciona una opción válida.")

def register_evaluations():
    data = load_data()
    enrollments = data.get("enrollments", [])
    evaluations = data.get("evaluations", [])
    campers = data.get("campers", [])

    if not enrollments:
        print("⚠️ No hay matrículas para evaluar.")
        return
    
    print("\n📋 Campers matriculados:")
    for e in enrollments:
        print(f"{e['camper_id']} - {e['camper_nombre']} (Ruta: {e['route_nombre']})")
    
    try:
        camper_id = int(input("👉 Ingresa el ID del camper a evaluar: "))
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        return

    # Buscar matrícula
    enrollment = next((e for e in enrollments if e["camper_id"] == camper_id), None)

    if not enrollment:
        print("❌ El camper no está matriculado.")
        return

    # Verificar si ya tiene evaluación
    for ev in evaluations:
        if ev["camper_id"] == camper_id and ev["route_nombre"] == enrollment["route_nombre"]:
            print(f"⚠️ El camper {enrollment['camper_nombre']} ya tiene evaluación registrada en {enrollment['route_nombre']}.")
            return

    try:
        nota_teorica = float(input("📝 Ingresa la nota teórica: "))
        nota_practica = float(input("📝 Ingresa la nota práctica: "))

        if not (0 <= nota_teorica <= 100 and 0 <= nota_practica <= 100):
            print("❌ Las notas deben estar entre 0 y 100.")
            return

        promedio = (nota_teorica + nota_practica) / 2
    
        # Definir estado y riesgo
        if promedio >= 60:
            estado = "Aprobado"
            riesgo = "Sin riesgo"
        elif promedio >= 40:
            estado = "En riesgo"
            riesgo = "Medio"
        else:
            estado = "Reprobado"
            riesgo = "Alto"

        # Actualizar camper en la base de datos
        for c in campers:
            if c["id"] == camper_id:
                c["Estado"] = estado
                c["Riesgo"] = riesgo
                break

        evaluation = {
            "camper_id": camper_id,
            "camper_nombre": enrollment["camper_nombre"],
            "route_nombre": enrollment["route_nombre"],
            "nota_teorica": nota_teorica,
            "nota_practica": nota_practica,
            "promedio": promedio,
            "estado": estado,
            "riesgo": riesgo
        }

        evaluations.append(evaluation)
        data["evaluations"] = evaluations
        save_data(data)

        print(f"✅ Evaluación registrada para {enrollment['camper_nombre']} "
              f"(Promedio: {promedio}, Estado: {estado}, Riesgo: {riesgo})")

    except ValueError:
        print("❌ Entrada inválida, debes ingresar números.")

def list_evaluations():
    data = load_data()
    evaluations = data.get("evaluations", [])

    if not evaluations:
        print("⚠️ No hay evaluaciones registradas aún.")
        return

    # Agrupar evaluaciones por ruta
    evaluaciones_por_ruta = {}
    for ev in evaluations:
        ruta = ev["route_nombre"]
        if ruta not in evaluaciones_por_ruta:
            evaluaciones_por_ruta[ruta] = []
        evaluaciones_por_ruta[ruta].append(ev)

    # Mostrar evaluaciones agrupadas
    for ruta, lista in evaluaciones_por_ruta.items():
        print(f"\n📚 Ruta: {ruta}")
        print("-" * 50)
        for ev in lista:
            print(f"👨‍🎓 {ev['camper_id']} - {ev['camper_nombre']} | "
                  f"Teórica: {ev['nota_teorica']} | "
                  f"Práctica: {ev['nota_practica']} | "
                  f"Promedio: {ev['promedio']} | "
                  f"Estado: {ev['estado']} | "
                  f"Riesgo: {ev['riesgo']}")
