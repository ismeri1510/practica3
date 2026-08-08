from flask import Flask, render_template, request##importa flask

app = Flask(__name__) # crea la app

@app.route("/") #define la ruta
def perfil():
    return render_template("perfil.html")

@app.route("/firma")
def firma():
    return render_template("firma.html")

@app.route("/guardar-firma" , methods=["POST"])
def guardar():
    
    nombre = request.form["nombre"] #obtiene el nombre del formulario
    mensaje = request.form["mensaje"] #obtiene el mensaje del formulario
    
    return render_template("gracias.html", nombre=nombre, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True) #inicia el servidor
    