# Trabajo Campuslands - ERP

## 🚀 Descripción del Proyecto

El objetivo de este sistema es simplificar la gestión de calificaciones de los *trainers*, *campers* y *coordinadores*. La idea es automatizar los cálculos y generar los estados correspondientes (como *riesgo* o *matriculado*) para que no sea necesario realizar procesos manuales. 

Los usuarios solo deben ingresar la calificación de cada *camper* y el sistema se encarga de todo lo demás.

---

## 🛠️ Tecnologías Utilizadas

- **Visual Studio**: IDE de desarrollo.
- **Python**: Lenguaje de programación principal.
- **JSON**: Almacenamiento de datos persistente.
- **Diccionarios, Condicionales, Fórmulas y Cálculos**: Se emplearon para automatizar el proceso de asignación de estado de los *campers*.

---

## ⚙️ Estructura del Proyecto

- El sistema se inicia con el archivo `main.py`.
- Los datos se almacenan en un archivo `json.data` para persistencia y fácil acceso.

---

## 🔄 Funcionamiento

1. **Ingreso de Calificaciones**: 
   Los *trainers* y *coordinadores* ingresan las calificaciones de los *campers*.

2. **Análisis Automático**: 
   El sistema asigna automáticamente el estado del *camper* (si está en riesgo o matriculado) según la calificación ingresada.

3. **Generación de Reportes**: 
   El sistema genera reportes detallados con la información de calificaciones y estado de los *campers*.

---

## 🐞 Errores Iniciales

Durante el desarrollo, se identificaron los siguientes errores:

- **No registro del *camper***: El sistema no registraba correctamente a los *campers*.
- **Problemas en la *evaluations* y *coordination***: Las calificaciones y la coordinación no se guardaban correctamente.
- **Generación de Reportes**: Los reportes no se generaban adecuadamente.
- **Error en el módulo `utils`**: Impedía el guardado correcto de datos en el archivo `json.data`.

---

## 🔧 Actualizaciones y Correcciones

Las siguientes correcciones fueron implementadas:

- Se solucionó el **registro de *campers***.
- El error en el módulo `utils` fue corregido, permitiendo el guardado adecuado de los datos.
- Se arregló el manejo de **evaluations** y **coordination**.
- Los **reportes** ahora se generan correctamente, mostrando toda la información relevante.

---

## 📝 Instrucciones de Uso
- Se ejectua desde el main.py 

