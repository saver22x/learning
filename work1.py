import random

player_hp = 100
boss_hp = 150

print('You are in a boss fight!')
print(f'Your HP is {player_hp}, Boss HP is {boss_hp}')

while player_hp > 0 and boss_hp > 0:
    print('\nPlayer turn!')
    print(f'Your HP: {player_hp} | Boss HP: {boss_hp}')
    print('Choose your action: attack, defend, heal')
    while True:
        choice = input('Whats your next move? (attack/ defend /heal): ')
        if choice == 'attack':
            print('You attack the boss!')
            boss_hp -= 20
            print(f'Boss HP is now {boss_hp}.')
            break
        elif choice == 'defend':
            print('You defend against the boss attack! Damage will be reduced.')
            break
        elif choice == 'heal':
            print('You heal yourself!')
            player_hp += 15
            print(f'Your HP is now {player_hp}.')
            break
        else:
            print('Invalid choice. Please choose attack, defend, or heal.')

    print('\nBoss turn!')
    boss_attack = random.randint(10, 30)
    if choice == 'attack' or choice == 'heal':
        print(f'The boss attacks you for {boss_attack} damage!')
        player_hp -= boss_attack
        print(f'Your HP is now {player_hp}.')
    elif choice == 'defend':
        print(f'The boss attacks you for {boss_attack} damage, but you defend!')
        player_hp -= boss_attack // 2
        print(f'Your HP is now {player_hp}.')

    if player_hp <= 0:
        print('You have been defeated by the boss!')
        print('Game over!')
        break
    if boss_hp <= 0:
        print('You have defeated the boss!')
        print('Congratulations! You win!')

        break
