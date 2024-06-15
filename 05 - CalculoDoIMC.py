def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0 or peso <= 0:
        raise ValueError("Altura e peso devem ser maiores que zero.")

    imc = peso / (altura * altura)
    return imc

def interpretar_imc(imc: float) -> str:
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade grau I"
    elif 35 <= imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return classificacao

def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))

        imc = calcular_imc(peso, altura)
        classificacao = interpretar_imc(imc)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError as error:
        print(f"Erro: {error}")

if __name__ == "__main__":
    main()
