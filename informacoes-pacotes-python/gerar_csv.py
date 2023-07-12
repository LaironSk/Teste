from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

def ler_csv():
    pacotes = []

    with open("pacotes.csv", "r") as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)
        for linha in reader:
            pacotes.append(linha)

    return pacotes

@app.route("/pacotes", methods=["GET"])
def get_pacotes():
    pacotes = ler_csv()
    pacotes_ordenados = sorted(pacotes, key=lambda x: x["Nome"])

    return jsonify(pacotes_ordenados)

@app.route("/pacotes/nome", methods=["GET"])
def buscar_por_nome():
    nome = request.args.get("nome")
    pacotes = ler_csv()
    resultado = [p for p in pacotes if p["Nome"] == nome]

    return jsonify(resultado)

@app.route("/pacotes/versao_python", methods=["GET"])
def buscar_por_versao_python():
    versao_python = request.args.get("versao_python")
    pacotes = ler_csv()
    resultado = [p for p in pacotes if p["Versão do Python"] == versao_python]

    return jsonify(resultado)

if __name__ == "__main__":
    app.run()
