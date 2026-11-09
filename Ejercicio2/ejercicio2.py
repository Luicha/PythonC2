import json

class StockInvalidoError(Exception): 
    pass

class DispositivoEcologico:
    def __init__(self, modelo: str, precio: float, stock: int):
        self.modelo = modelo
        self.precio = precio
        self.set_stock(stock)

    def get_stock(self) -> int:
        return self.__stock

    def set_stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise StockInvalidoError(
                f"El stock de '{self.modelo}' no puede ser negativo ({nuevo_stock})."
            )
        self.__stock = nuevo_stock

    def obtener_ficha_tecnica(self) -> str:
        return f"Modelo: {self.modelo} | Precio: ${self.precio} | Stonk: {self.get_stock()}"

    def a_diccionario(self) -> dict:
        return {
            "tipo": "DispositivoEcologico",
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock()
        }

class PanelSolar(DispositivoEcologico):
    def __init__(self, modelo: str, precio: float, stock: int, eficiencia_watts: int):
        super().__init__(modelo, precio, stock)
        self.eficiencia_watts = eficiencia_watts

    def obtener_ficha_tecnica(self) -> str:
        ficha_base = super().obtener_ficha_tecnica()
        return f"{ficha_base} | Potencia: {self.eficiencia_watts}W (Dispositivo de Alta Eficiencia)"

    def a_diccionario(self) -> dict:
        datos = super().a_diccionario()
        datos["tipo"] = "PanelSolar"
        datos["eficiencia_watts"] = self.eficiencia_watts
        return datos


class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos: list, ruta_archivo: str):
        catalogo_serializable = [
            dispositivo.a_diccionario() for dispositivo in lista_dispositivos
        ]

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo_serializable, archivo, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    print("1. CREACIÓN DE PRODUCTOS VÁLIDOS")
    termostato = DispositivoEcologico("Termostato-Pro", 350.0, 8)
    panel_1 = PanelSolar("SolarMax-500", 1500.0, 10, 500)
    panel_2 = PanelSolar("Solar-Pro", 1200.0, 5, 400)

    catalogo_valido = [termostato, panel_1, panel_2]

    for producto in catalogo_valido:
        print(producto.obtener_ficha_tecnica())

    print("\n2. PRUEBA DE REGLA DE NEGOCIO")
    try:
        print("Intentando asignar stock -5 al Termostato-Pro...")
        termostato.set_stock(-5)
    except StockInvalidoError as error:
        print(f"[REGLA DE NEGOCIO MANEJADA]: {error}")

    try:
        print("Intentando crear un PanelSolar con stock inicial -10...")
        panel_fallido = PanelSolar("Solar-Fail", 900.0, -10, 300)
    except StockInvalidoError as error:
        print(f"[REGLA DE NEGOCIO MANEJADA]: {error}")

    print("\n3. PERSISTENCIA EN DISCO")
    gestor = GestorInventario()
    nombre_archivo = "catalogo_ecotech.json"

    gestor.guardar_catalogo_json(catalogo_valido, nombre_archivo)
    print(f"Catálogo exportado con éxito en '{nombre_archivo}'.")

    with open(nombre_archivo, "r", encoding="utf-8") as f:
        datos_recuperados = json.load(f)
    print(f"Total de cosos verificados en el JSON: {len(datos_recuperados)}")