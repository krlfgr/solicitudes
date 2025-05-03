from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def inicio():
    return "Pagina de inicio"

# ruta parametros por URL
@app.route("/consulta")
def ruta_consulta():
    producto = request.args.get("product")
    talla = request.args.get("talla")
    if producto and talla is None:
        return f"Se esta consultando solo el producto {producto}"
    if talla is None and producto:
        return f"Por favor ingrese el producto a buscar {talla}"
    if producto is None and talla is None:
        return "Bienvenido a la pagina de ropa"
    return f"Se esta consultando el producto {producto} y la talla {talla}"

# ruta para capturar datos por el body
@app.route("/registro", methods=["GET"])
def ruta_registro():
    return render_template("formulario.html")

@app.route("/registro", methods=["POST"])
def procesar_registro():
    nombre=request.form.get("Nombre")
    correo=request.form.get("Correo")
    return f"El estudiante a registrar es {nombre} y el correo a registrar es {correo}"

if __name__=="__main__":
    app.run(debug=True)