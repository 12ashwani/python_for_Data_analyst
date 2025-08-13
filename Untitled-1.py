for row in range(8):
    for col in range(9):
        if (row == 0 and col % 2 != 0) or (row == 1 and col % 4 == 0) or (row == 2 and col % 8 == 0):
            print('\u2764\ufe0f', end='')
        elif row == 3 and col == 0:
            print('\u2764\ufe0f', end='')
        elif row == 3 and col == 4:
            print('ABC', end='')
        elif row == 3 and col == 8:
            print('\u2764\ufe0f', end='')
        elif row == 4 and (col == 1 or col == 7):
            print('\u2764\ufe0f', end=' ')
        elif row == 5 and (col == 2 or col == 6):
            print('\u2764\ufe0f', end=' ')
        elif row == 6 and (col == 3 or col == 5):
            print('\u2764\ufe0f', end=' ')
        elif row == 7 and col == 4:
            print(' \u2764\ufe0f', end='')
        else:
            print(' ', end=' ')
    print()
