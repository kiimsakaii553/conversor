def metros_para_centimetros(valor):
    return valor * 100




def centimetros_para_metros(valor):
    return valor / 100




def quilometros_para_metros(valor):
    return valor * 1000




def metros_para_quilometros(valor):
    return valor / 1000




def celsius_para_fahrenheit(valor):
    return valor * 9 / 5 + 32




def fahrenheit_para_celsius(valor):
    return (valor - 32) * 5 / 9




def quilogramas_para_gramas(valor):
    return valor * 1000




def gramas_para_quilogramas(valor):
    return valor / 1000




def mostrar_menu():
    print("1. Metros para centímetros")
    print("2. Centímetros para metros")
    print("3. Quilômetros para metros")
    print("4. Metros para quilômetros")
    print("5. Celsius para Fahrenheit")
    print("6. Fahrenheit para Celsius")
    print("7. Quilogramas para gramas")
    print("8. Gramas para quilogramas")
    print("0. Sair")




def main():
    conversoes = {
        "1": (metros_para_centimetros, "cm"),
        "2": (centimetros_para_metros, "m"),
        "3": (quilometros_para_metros, "m"),
        "4": (metros_para_quilometros, "km"),
        "5": (celsius_para_fahrenheit, "°F"),
        "6": (fahrenheit_para_celsius, "°C"),
        "7": (quilogramas_para_gramas, "g"),
        "8": (gramas_para_quilogramas, "kg"),
    }


    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()


        if opcao == "0":
            print("Programa encerrado.")
            break


        if opcao not in conversoes:
            print("Opção inválida.")
            continue


        try:
            valor = float(input("Digite o valor: ").replace(",", "."))
        except ValueError:
            print("Valor inválido.")
            continue


        funcao, unidade = conversoes[opcao]
        resultado = funcao(valor)
        print(f"Resultado: {resultado:.2f} {unidade}\n")




if __name__ == "__main__":
    main()
