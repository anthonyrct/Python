# Arquivo jogo.py

import random
from Perguntas import questions

# Função para apresentar perguntas ao usuário
def ask_question(question, answer):
    user_answer = input(question + "\nSua resposta: ")
    if user_answer.lower() == answer.lower():
        print("Resposta correta!")
        return True
    else:
        print("Resposta incorreta. A resposta correta é:", answer)
        return False

# Função para a ajuda do "Telefone de um Amigo"
def phone_a_friend(question, answer):
    print("Chamando um amigo...")
    # Simulação de uma resposta do amigo (poderia ser mais elaborada)
    friend_answer = random.choice(["Acho que é " + answer, "Não tenho certeza, mas acho que é " + answer, "Não tenho ideia"])
    print("Seu amigo diz:", friend_answer)

# Função para a ajuda do "50/50"
def fifty_fifty(question, answer):
    print("Eliminando duas opções incorretas...")
    options = list(questions.values())
    options.remove(answer)
    options_to_remove = random.sample(options, 2)
    for option in options_to_remove:
        print("Opção eliminada:", option)

# Função para pular a pergunta atual
def skip_question():
    print("Pulando a pergunta atual...")

# Função para jogar o jogo
def play_game():
    score = 0
    for i, (question, answer) in enumerate(random.sample(list(questions.items()), k=5), start=1):  # Seleciona 5 perguntas aleatórias
        print("\nQuestão", i)
        print("-----------")
        if ask_question(question, answer):
            score += 1
        # Lógica para usar ajudas
        if i < 9:  # Permite usar ajudas até a questão 9
            help_choice = input("Você quer usar uma ajuda? (Pressione '1' para usar o telefone de um amigo, '2' para usar a ajuda do 50/50, '3' para pular a pergunta atual, ou 'n' para continuar sem ajuda): ")
            if help_choice == "1":
                phone_a_friend(question, answer)
            elif help_choice == "2":
                fifty_fifty(question, answer)
            elif help_choice == "3":
                skip_question()
        elif i == 9:
            print("Não é permitido usar ajudas na última questão!")

    if score == 5:  # Se o jogador acertar todas as 5 perguntas, exibe a mensagem de vitória
        print("\nParabéns! Você acertou todas as perguntas e ganhou o jogo!")

# Iniciar o jogo
if __name__ == "__main__":
    play_game()
