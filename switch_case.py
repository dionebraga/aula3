
time = input("Digite seu time: ")

match time:
    case "Corinthians":
        print("Você é um Timão")
    case "Bahia":
        print("Você é Esquadrão")
    case "Grêmio":
        print("Você é imortal")
    case _:
        print("Quem não é não se mete")
