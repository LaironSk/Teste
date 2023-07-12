import csv

def ler_referencia():
    referencia = {}

    with open("reference.txt", "r") as arquivo_referencia:
        linhas = arquivo_referencia.readlines()
        for linha in linhas:
            if ":" in linha:
                chave, valor = linha.split(":")
                chave = chave.strip()
                valor = valor.strip()
                referencia[chave] = valor

    return referencia

def ler_dados():
    dados = []

    with open("data.csv", "r") as arquivo_dados:
        reader = csv.DictReader(arquivo_dados)
        for linha in reader:
            dados.append(linha)

    return dados

def calcular_porcentagem_colesterol_alto(dados, referencia):
    total_pessoas = len(dados)
    total_colesterol_alto = 0

    for pessoa in dados:
        idade = int(pessoa["age"])
        colesterol = int(pessoa["chol"])
        colesterol_limite = int(referencia["An ideal total cholesterol level is lower than 200 mg/dL."].split(" ")[5])

        if idade > 40 and colesterol > colesterol_limite:
            total_colesterol_alto += 1

    porcentagem = (total_colesterol_alto / total_pessoas) * 100
    return porcentagem

def calcular_porcentagem_colesterol_açucar(dados, referencia):
    total_pessoas_acima_40 = 0
    total_pessoas_colesterol_alto = 0
    total_pessoas_colesterol_açucar = 0

    for pessoa in dados:
        idade = int(pessoa["age"])
        colesterol = int(pessoa["chol"])
        açucar_sangue = int(referencia["(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)"].split(" ")[6])

        if idade > 40:
            total_pessoas_acima_40 += 1
            if colesterol > int(referencia["An ideal total cholesterol level is lower than 200 mg/dL."].split(" ")[5]):
                total_pessoas_colesterol_alto += 1
                if açucar_sangue == 1:
                    total_pessoas_colesterol_açucar += 1

    porcentagem = (total_pessoas_colesterol_açucar / total_pessoas_colesterol_alto) * 100
    return porcentagem

def relacionar_colesterol_açucar_hipertrofia(dados, referencia):
    total_pessoas_colesterol_açucar = 0
    total_pessoas_hipertrofia = 0

    for pessoa in dados:
        colesterol = int(pessoa["chol"])
        açucar_sangue = int(referencia["(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)"].split(" ")[6])
        hipertrofia = int(referencia["-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria"])

        if colesterol > int(referencia["An ideal total cholesterol level is lower than 200 mg/dL."].split(" ")[5]):
            total_pessoas_colesterol_açucar += 1
            if açucar_sangue == 1 and hipertrofia == 1:
                total_pessoas_hipertrofia += 1

    if total_pessoas_colesterol_açucar > 0:
        porcentagem = (total_pessoas_hipertrofia / total_pessoas_colesterol_açucar) * 100
    else:
        porcentagem = 0

    return porcentagem

if __name__ == "__main__":
    referencia = ler_referencia()
    dados = ler_dados()

    porcentagem_colesterol_alto = calcular_porcentagem_colesterol_alto(dados, referencia)
    porcentagem_colesterol_açucar = calcular_porcentagem_colesterol_açucar(dados, referencia)
    porcentagem_relacionamento = relacionar_colesterol_açucar_hipertrofia(dados, referencia)

    print(f"1) Porcentagem de pessoas acima de 40 anos com colesterol alto: {porcentagem_colesterol_alto}%")
    print(f"2) Porcentagem de pessoas acima de 40 anos com colesterol alto e alto teor de açúcar no sangue: {porcentagem_colesterol_açucar}%")
    print(f"3) Porcentagem de pessoas com colesterol alto e alto teor de açúcar relacionadas à hipertrofia: {porcentagem_relacionamento}%")
