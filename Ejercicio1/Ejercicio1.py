    #Punto A
def limpiar_registro_sensor(registro_raw: dict) -> dict:

    id_crudo = registro_raw.get("sensor_id", "SIN-ID")
    sensor_id_limpio = id_crudo.strip()

    lectura_raw = str(registro_raw.get("temperatura", "0.0"))
    lectura_sin_espacios = lectura_raw.strip()

    lectura_sin_unidad = (
        lectura_sin_espacios.replace("°C", "")
        .replace("C", "")
        .replace("c", "")
        .strip()
    )

    temperatura_float = float(lectura_sin_unidad)

    ubicacion = registro_raw.get("ubicacion", "Narnia")

    if not ubicacion or not ubicacion.strip():
        ubicacion = "Narnia"
    else:
        ubicacion = ubicacion.strip()

    return {
        "sensor_id": sensor_id_limpio,
        "temperatura": temperatura_float,
        "ubicacion": ubicacion
    }


    # Punto B
def generar_resumen_sensores(lista_sensores_limpios: list, umbral_temperatura: float) -> tuple:
    
    if not lista_sensores_limpios:
        return ([], 0.0)

    sensores_filtrados = list(
        filter(lambda s: s["temperatura"] > umbral_temperatura, lista_sensores_limpios)
    )

    lista_sensores_alerta = list(
        map(lambda s: s["sensor_id"], sensores_filtrados)
    )

    suma_temperaturas = sum(s["temperatura"] for s in lista_sensores_limpios)
    promedio_temperatura = round(suma_temperaturas / len(lista_sensores_limpios), 2)

    return (lista_sensores_alerta, promedio_temperatura)

if __name__ == "__main__":

    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002  ", "temperatura": " 31.2C ", "ubicacion": "Sector Calderas"},
        {"sensor_id": "  SENSOR-003", "temperatura": "28.0C"}, 
        {"sensor_id": "SENSOR-004 ", "temperatura": "35.8C", "ubicacion": "Planta Sur"}
    ]

    umbral = 25.0

    sensores_limpios = list(map(limpiar_registro_sensor, registros_crudos))

    print("1. REGISTROS DE SENSORES SANITIZADOS")
    for sensor in sensores_limpios:
        print(
            f"Sensor ID: {sensor['sensor_id']} --- "
            f"Temp: {sensor['temperatura']}°C ({type(sensor['temperatura']).__name__}) --- "
            f"Ubicación: {sensor['ubicacion']}"
        )

    resultado_resumen = generar_resumen_sensores(sensores_limpios, umbral)
    ids_alerta, temp_promedio = resultado_resumen

    print("\n2. REPORTE CONSOLIDADO \033[9mECOMODAS\033[0m ECOTECH SOLUTIONS ---")
    print(f"Umbral configurado          : {umbral}°C")
    print(f"Promedio térmico global     : {temp_promedio}°C")
    print(f"Sensores en alerta          : {ids_alerta}")
    print(f"Estructura de retorno       : {resultado_resumen} -> Tipo: {type(resultado_resumen)}")