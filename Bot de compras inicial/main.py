from dataclasses import dataclass

@dataclass
class ComprasInteligentes:
    punto_reorden: int
    costo_total: float

    PUNTO_REORDEN_UMBRAL = 100
    COSTO_ALMACENAMIENTO_UMBRAL = 100000

    def resumen_decisiones(self) -> str:
        if self.punto_reorden < self.PUNTO_REORDEN_UMBRAL:
            return "🔔 Recomendación: Considera pedido urgente"
        elif self.costo_total > self.COSTO_ALMACENAMIENTO_UMBRAL:
            return "💡 Sugerencia: Revisa costos de almacenamiento"
        return "✅ Situación óptima"

    @staticmethod
    def calcular_punto_reorden(demanda_diaria: int, tiempo_entrega: int, stock_seguro: int) -> int:
        if any(val <= 0 for val in [demanda_diaria, tiempo_entrega, stock_seguro]):
            raise ValueError("Los valores deben ser mayores a 0.")
        return demanda_diaria * tiempo_entrega + stock_seguro

    @staticmethod
    def calcular_costo_total(costo_pedido: float, costo_mantenimiento: float) -> float:
        if any(val < 0 for val in [costo_pedido, costo_mantenimiento]):
            raise ValueError("Los costos no pueden ser negativos.")
        return costo_pedido + costo_mantenimiento

    @staticmethod
    def calcular_descuento(precio_unitario: float, cantidad: int, descuento: float) -> float:
        if any(val <= 0 for val in [precio_unitario, cantidad]) or not (0 <= descuento <= 1):
            raise ValueError("Valores inválidos para descuento.")
        return precio_unitario * cantidad * (1 - descuento)
