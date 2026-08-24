from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    peso = float(request.form["peso"])
    arrobas = peso / 15

    return render_template(
        "resultado.html",
        peso=peso,
        arrobas=round(arrobas, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)