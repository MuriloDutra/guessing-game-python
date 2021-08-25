import random

print("********************************")
print("BEM-VINDO AO JOGO DE ADIVINHAÇÃO")
print("********************************")

secret_number = random.randrange(1, 101)
maximum_of_attempts = 0
score = 1000

print("(1) Fácil (2) Médio (3) Difícil")
difficulty_level = int(input("Qual o nível de dificuldade?"))

if(difficulty_level == 1):
    maximum_of_attempts = 20
elif(difficulty_level == 2):
    maximum_of_attempts = 10
else:
    maximum_of_attempts = 5

for round in range(1, maximum_of_attempts + 1):
    print("\n")
    print(f"# Tentativa {round} de {maximum_of_attempts}") #equivalent print("Tentativa {} de {}".format(round, maximum_of_attempts))

    user_attempt = int(input("Digite um número entre 1 e 100: "))

    if(user_attempt < 1 or user_attempt > 100):
        print("Número inválido, digite um número entre 1 e 100.")
        continue

    user_won = (user_attempt == secret_number)
    user_attempt_is_bigger = (user_attempt > secret_number)
    user_attempt_is_smaller = (user_attempt < secret_number)

    if(user_won):
        print(f"Você acertou! Seu resultado: {score} pontos.")
        break
    else:
        if(user_attempt_is_bigger):
            print("Você errou. Seu chute foi MAIOR que o número secreto")
        elif(user_attempt_is_smaller):
            print("Você errou. Seu chute foi MENOR que o número secreto")
        lost_points = abs(secret_number - user_attempt)
        score = score - lost_points
