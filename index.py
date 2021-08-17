print("********************************")
print("BEM-VINDO AO JOGO DE ADIVINHAÇÃO")
print("********************************")

secret_number = 42
maximum_of_attempts = 3
round = 1;

while(round <= maximum_of_attempts):
    print(f"Tentativa {round} de {maximum_of_attempts}")
    #print("Tentativa {} de {}".format(round, maximum_of_attempts))
    user_attempt = int(input("Digite um número: "))

    user_won = (user_attempt == secret_number)
    user_attempt_is_bigger = (user_attempt > secret_number)
    user_attempt_is_smaller = (user_attempt < secret_number)

    if(user_won):
        print("Você acertou!")
    else:
        if(user_attempt_is_bigger):
            print("Você errou. Seu chute foi MAIOR que o número secreto")
        elif(user_attempt_is_smaller):
            print("Você errou. Seu chute foi MENOR que o número secreto")

    round = round + 1