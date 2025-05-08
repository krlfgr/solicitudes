from flask import Flask, request, render_template, make_response


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
    # listado=[{"nombre": "karol", "correo": "karolf@gmail.com"}]
    return render_template("formulario.html", listado=listado)

listado=[]

@app.route("/registro", methods=["POST"])
def procesar_registro():
    nombre=request.form.get("Nombre")
    correo=request.form.get("Correo")
    estudiante={"nombre":nombre, "correo":correo}
    listado.append(estudiante)
    # print(nombre)
    return f"El estudiante a registrar es {nombre} y el correo a registrar es {correo}"

# parametros en la ruta caso tres
@app.route("/estudiantes/<string:programa>/<int:grupo>")
def mostrar_estudiantes(programa,grupo):
    return f"programa de formacion consultado es {programa} y grupo consultado es {grupo}"

# encabezados mensaje salicitud tipo 4
@app.route("/ver-headers")
def ver_headers():
    agente_usuario = request.headers.get('User-Agent')
    return f"Tu navegador es: {agente_usuario}"

# gestion de las cookies
@app.route('/crear-cookie')
def crear_cookie():
    respuesta = make_response("Cookie creada!") # mensaje que se vera en el navegador
    respuesta.set_cookie('usuario_logueado', 'true', max_age=60*60*24, httponly=True) 
    return respuesta

@app.route('/leer-cookie')
def leer_cookie():
    valor = request.cookies.get('usuario_logueado')
    return f"Valor de la cookie: {valor}"



if __name__=="__main__":
    app.run(debug=True)