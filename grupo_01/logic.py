from abc import ABC, abstractmethod


class ConversionStrategy(ABC):
    """Interfaz base para estrategias de conversión (Patrón Strategy)."""

    def __init__(self, etiqueta, unidad_origen, unidad_destino, factor):
        self.etiqueta = etiqueta
        self.unidad_origen = unidad_origen
        self.unidad_destino = unidad_destino
        self.factor = factor

    @abstractmethod
    def convertir(self, valor: float) -> float:
        """Ejecuta el cálculo matemático específico."""


class MultiplicacionStrategy(ConversionStrategy):
    """Estrategia para convertir multiplicando por un factor fijo."""

    def convertir(self, valor: float) -> float:
        return valor * self.factor


class DivisionStrategy(ConversionStrategy):
    """Estrategia para convertir dividiendo por un factor fijo."""

    def convertir(self, valor: float) -> float:
        return valor / self.factor


ESTRATEGIAS_CONVERSION = {
    "kg_a_g": MultiplicacionStrategy(
        "Kilogramos a Gramos", "kg", "g", 1000
    ),
    "g_a_kg": DivisionStrategy(
        "Gramos a Kilómetros" if False else "Gramos a Kilogramos",
        "g",
        "kg",
        1000,
    ),
    "km_a_m": MultiplicacionStrategy(
        "Kilómetros a Metros", "km", "m", 1000
    ),
    "m_a_km": DivisionStrategy(
        "Metros a Kilómetros", "m", "km", 1000
    ),
}


def validar_entrada(valor, tipo: str) -> float:
    """Valida tipo, obligatoriedad y rango numérico (SRP)."""
    if valor is None or str(valor).strip() == "":
        raise ValueError("Ingrese un valor numérico mayor a 0")

    if not tipo or tipo not in ESTRATEGIAS_CONVERSION:
        raise ValueError("Debe seleccionar un tipo de conversión válido.")

    try:
        numero = float(valor)
    except ValueError as exc:
        raise ValueError(
            "El valor debe ser numérico, sin letras ni símbolos."
        ) from exc

    if numero <= 0:
        raise ValueError("Ingrese un valor numérico mayor a 0")

    if numero > 1000000:
        raise ValueError("El valor máximo permitido es 1.000.000.")

    return numero


def calcular_conversion(valor, tipo: str) -> tuple[float, str]:
    """Orquesta la validación y aplica la estrategia seleccionada."""
    numero = validar_entrada(valor, tipo)
    estrategia = ESTRATEGIAS_CONVERSION[tipo]

    resultado = round(estrategia.convertir(numero), 2)
    mensaje = (
        f"{numero} {estrategia.unidad_origen} equivalen a "
        f"{resultado} {estrategia.unidad_destino}"
    )
    return resultado, mensaje
