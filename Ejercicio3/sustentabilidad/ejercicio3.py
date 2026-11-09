import unittest

try:
    from django.shortcuts import render
except ImportError:
    def render(request, template_name: str, context: dict) -> dict:
        return {
            "status": "200 OK (Render Simulado)",
            "template": template_name,
            "context": context
        }
    
class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_correcto_factor_por_defecto(self):
        resultado = calcular_emisiones_carbono(100.0)
        self.assertEqual(resultado, 40.0)

    def test_calculo_correcto_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(250.0, 0.5)
        self.assertEqual(resultado, 125.0)

    def test_calculo_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0.0)
        self.assertEqual(resultado, 0.0)

    def test_consumo_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)


if __name__ == "__main__":
    print("1. DEMOSTRACIÓN DE MÉTRICAS Y VISTA WEB (PUNTO B)")
    respuesta_web = vista_panel_sustentabilidad(request="GET /sustentabilidad/panel/")
    print(f"Respuesta de la vista Django: {respuesta_web}\n")

    print("2. EJECUCIÓN DE AUDITORÍA CON UNITTEST (PUNTO A)")
    unittest.main(verbosity=2, exit=False)