import pytest
from grupo_01.logic import calcular_conversion


def test_conversion_valida_kg_a_g():
    """Caso válido del documento: 3.5 kg -> 3500.0 g."""
    resultado, mensaje = calcular_conversion("3.5", "kg_a_g")
    assert resultado == 3500.0
    assert mensaje == "3.5 kg equivalen a 3500.0 g"


def test_conversion_valida_g_a_kg_redondeo():
    """Verifica división y redondeo a 2 decimales."""
    resultado, mensaje = calcular_conversion("1234", "g_a_kg")
    assert resultado == 1.23
    assert mensaje == "1234.0 g equivalen a 1.23 kg"


def test_conversion_limite_maximo_m_a_km():
    """Caso límite del documento: 1000000 m -> 1000.0 km."""
    resultado, mensaje = calcular_conversion(1000000, "m_a_km")
    assert resultado == 1000.0
    assert mensaje == "1000000.0 m equivalen a 1000.0 km"


def test_conversion_invalida_negativo():
    """Caso inválido del documento: valor -20."""
    msg = "Ingrese un valor numérico mayor a 0"
    with pytest.raises(ValueError, match=msg):
        calcular_conversion("-20", "kg_a_g")


def test_conversion_invalida_vacio():
    """Caso inválido del documento: valor vacío."""
    msg = "Ingrese un valor numérico mayor a 0"
    with pytest.raises(ValueError, match=msg):
        calcular_conversion("", "kg_a_g")


def test_conversion_invalida_cero():
    """Valor igual a 0 debe ser rechazado."""
    msg = "Ingrese un valor numérico mayor a 0"
    with pytest.raises(ValueError, match=msg):
        calcular_conversion("0", "km_a_m")


def test_conversion_supera_limite():
    """Valor mayor a 1.000.000 debe ser rechazado."""
    with pytest.raises(ValueError, match="El valor máximo permitido"):
        calcular_conversion("1000001", "km_a_m")


def test_conversion_texto_o_simbolos():
    """No se aceptan letras ni símbolos especiales."""
    with pytest.raises(ValueError, match="El valor debe ser numérico"):
        calcular_conversion("12a$", "kg_a_g")


def test_opcion_invalida():
    """Opción fuera de la lista fija."""
    with pytest.raises(ValueError, match="tipo de conversión válido"):
        calcular_conversion("10", "millas_a_km")
