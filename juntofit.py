class Aluno:
    def _init_(self, nome):
        self.nome = nome
        self.frequencia = 0
        self.faltou = False

    def passar_catraca(self):
        if self.faltou:
            self.frequencia = 1
            self.faltou = False
            print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
        else:
            self.frequencia += 1
            print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
            if self.frequencia == 21:
                print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
                self.frequencia = 0

    def faltar(self):
        self.faltou = True


def main():
    nome_aluno = input("Digite o nome do aluno: ")
    aluno = Aluno(nome_aluno)

    while True:
        acao = input("\nDigite 'P' para passar na catraca, 'F' para registrar falta, ou 'S' para sair: ").upper()
        
        if acao == 'P':
            aluno.passar_catraca()
        elif acao == 'F':
            aluno.faltar()
        elif acao == 'S':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if _name_ == "_main_":
    main()