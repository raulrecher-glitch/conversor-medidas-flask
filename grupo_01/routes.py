from flask import Blueprint, render_template, request
from .logic import ESTRATEGIAS_CONVERSION, calcular_conversion

grupo_bp = Blueprint("grupo_01", __name__, url_prefix="/grupo_01")


@grupo_bp.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    mensaje_exito = None
    mensaje_error = None
    valor_ingresado = ""
    tipo_seleccionado = ""

    if request.method == "POST":
        valor_ingresado = request.form.get("valor", "")
        tipo_seleccionado = request.form.get("tipo_conversion", "")

        try:
            resultado, mensaje_exito = calcular_conversion(
                valor_ingresado, tipo_seleccionado
            )
        except ValueError as error:
            mensaje_error = str(error)

    return render_template(
        "grupo_01/index.html",
        opciones=ESTRATEGIAS_CONVERSION,
        resultado=resultado,
        mensaje_exito=mensaje_exito,
        mensaje_error=mensaje_error,
        valor_ingresado=valor_ingresado,
        tipo_seleccionado=tipo_seleccionado,
    )
