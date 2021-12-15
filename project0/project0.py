# project0.py
#
# A231 Python 2 Spring 2021
# Credit: Van Nguyen, C02699930
# Project 0: David Kay's Design Recipe in action


def downward_diagonal() -> None:
    '''Take a positive integer n and print a diagonal block diagonal 
    of size n.'''
    val = int(input())

    for x in range(val):
        if x == 0:
            print('+-+')
            print('| |')
        else: 
            print((' ' * (x - 1) * 2) + '+-+-+')
            print((' ' * (x - 1) * 2) + '  ' + '| |')

        if x == val - 1:
            if x == 0:
                print('+-+')
            else:
                print((' ' * (x - 1) * 2) + '  ' + '+-+')


downward_diagonal()

