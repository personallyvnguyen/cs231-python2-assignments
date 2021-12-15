# moduleA.py
#
# A231 Python 2 Spring 2021
# Credit: Van Nguyen (C02699930)
# Assignment: What's in a namespace


import moduleB



def main() -> None:
    'Prints a famous quote.'
    print('I think...')
    moduleB.main()
    


if __name__ == "__main__":
   main()


