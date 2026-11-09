from django.shortcuts import render

def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4) -> float:
    """Calcula emisiones estimadas. Eleva ValueError si el consumo es negativo."""
    if consumo_kwh < 0:
        raise ValueError("El consumo energético no puede ser negativo.")
    emisiones = consumo_kwh * factor_emision
    return round(emisiones, 2)

def obtener_metricas_consumo(registros: list) -> dict:
    if not registros:
        return {"total_emisiones": 0.0, "planta_top": "Sin registros"}

    total_emisiones = sum(
        calcular_emisiones_carbono(r["consumo_kwh"]) for r in registros
    )

    planta_mayor = max(registros, key=lambda r: r["consumo_kwh"])["planta"]

    return {
        "total_emisiones": round(total_emisiones, 2),
        "planta_top": planta_mayor
    }


def vista_panel_sustentabilidad(request):
 
    registros_consumo = [
        {"planta": "Planta Norte", "consumo_kwh": 1200.0},
        {"planta": "Planta Sur", "consumo_kwh": 850.0},
        {"planta": "Planta Norte", "consumo_kwh": 1400.0}
    ]

    metricas = obtener_metricas_consumo(registros_consumo)

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_top": metricas["planta_top"]
    }

    return render(request, "sustentabilidad/panel.html", contexto)