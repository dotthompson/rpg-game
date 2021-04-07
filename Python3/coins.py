print('You have 0 coins')
answer = input('Do you want another coin?   ')

coins = 0


while answer == 'yes':
    coins += 1
    print(f'You have {coins} coin.')
    answer = input('Do you want another coin?   ')
    answer = answer.lower()

while answer.lower() == 'no':
    print('Bye')
    break


