import random
import os

options = ["direita", "esquerda"];

ways = [];
current_way = 0;

def next_way():
    global current_way;
    current_way += 1;
    return current_way;

def show_infos(current_way, lifes):
    print("caminhos restantes: " + str(len(ways) - current_way));
    print("\n");
    print("vidas: " + str(lifes));
    print("\n");

def lose_game():
    os.system("cls");
    print("Voce morreu! Fim de jogo.");
    exit();

def win_game():
    os.system("cls");
    input("Voce ganhou!");
    exit();

number_of_generations = input("digite o numero de caminhos: \n");

while not number_of_generations.isdigit() or int(number_of_generations) < 1:
    os.system("cls");
    number_of_generations = input("digite um numero valido! \n");

number_of_generations = int(number_of_generations);

print("gerando caminhos...");

in_game = True;
lifes = 3;

for i in range(number_of_generations):
    random_number = random.randint(0, len(options) - 1);
    random_way = options[random_number];
    ways.append(random_way);3

os.system("cls");

while in_game:

    if current_way == len(ways):
        win_game();

    show_infos(current_way, lifes);

    answer = input("Quer ir para direita ou esquerda? \n");

    while answer not in options:
        os.system("cls");
        show_infos(current_way, lifes);
        answer = input("Quer ir para direita ou esquerda? \n");

    if answer == ways[current_way]:
        current_way = next_way();
        os.system("cls");

        if random.randint(0, 100) < 10:
            lifes += 1;
            print("Você acertou! E ganhou uma vida! \n");
        else:
            print("Você acertou! \n");
    else:
        lifes -= 1;
        os.system("cls");
        print("Você errou! E perdeu uma vida! \n");
        if lifes == 0:
            lose_game();