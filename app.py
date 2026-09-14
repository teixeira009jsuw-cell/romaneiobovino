
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        brinco = request.form["brinco"]
        peso = float(request.form["peso"])

        if peso <= 0:
            return render_template(
                "resultado.html",
                erro="O peso deve ser maior que zero."
            )

        arrobas = peso / 15

        return render_template(
            "resultado.html",
            brinco=brinco,
            peso=peso,
            arrobas=round(arrobas, 2)
        )

    except ValueError:
        return render_template(
            "resultado.html",
            erro="Digite um peso válido."
        )


if __name__ == "__main__":
    app.run(debug=True)