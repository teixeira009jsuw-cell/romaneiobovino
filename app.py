from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")

# Cálculo das arrobas
@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        brinco = request.form["brinco"]
        peso = float(request.form["peso"])

        # Validação
        if peso <= 0:
            return render_template(
                "resultado.html",
                erro="O peso deve ser maior que zero."
            )

        # 1 arroba = 15 kg
        arrobas = round(peso / 15, 2)

        # Data e hora do romaneio
        data = datetime.now().strftime("%d/%m/%Y às %H:%M")

        return render_template(
            "resultado.html",
            brinco=brinco,
            peso=peso,
            arrobas=arrobas,
            data=data
        )

    except ValueError:
        return render_template(
            "resultado.html",
            erro="Digite um peso válido."
        )

# Executar o servidor
if __name__ == "__main__":
    app.run(debug=True)