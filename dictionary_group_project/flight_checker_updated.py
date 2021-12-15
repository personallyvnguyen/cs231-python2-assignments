# flight_checker.py
#
# A231 Python 2 Spring 2021
# Credit: 
#   - Huang, Yitian
#   - Hyman, Adam
#   - Nguyen, Van
# IN-CLASS ACTIVITY dictionary group project


import ast
import sys


class Flight_Checker:
    'Runs the flight checker application'

    WELCOME_MSG = (
        'Welcome to our flight checker application.\n\n'
        'Written by:\n'
        '- Huang, Yitian\n'
        '- Hyman, Adam\n'
        '- Nguyen, Van\n'
    )

    SMALL_DATA = 'small_flightdict.txt'
    FULL_DATA = 'full_flightdict.txt'
    
    
    def __init__(self, DEBUG: bool = True) -> None:
        'Initializes the instance variables'
        self._file_name = self.SMALL_DATA if DEBUG else self.FULL_DATA


    def execute(self) -> None:
        'Executes the flight check application'
        self._load_flight_data()
        print(self.WELCOME_MSG)
        print('-'*40, '\n')

        self._print_orig_codes()
        orig_code = self._get_orig_input()

        dest_flights = self._flights[orig_code][1:]
        self._print_dest_codes(dest_flights)

        dest_flights = self._get_dest_inputs(dest_flights)
        self._print_dest_prices(orig_code, dest_flights)


    def _load_flight_data(self) -> None:
        'Loads the data into the program'
        try:
            with open(self._file_name, "r") as file:
                self._flights = ast.literal_eval(file.read())
        except FileNotFoundError:
            print('Unable to access flight data.')
            sys.exit()


    def _get_orig_input(self) -> str:
        'Gets the originating airport code from the user'
        while True:
            try:
                code = input('\nEnter a starting airport code: ')

                if not code in self._flights:
                    raise KeyError
                else:
                    return code
            except KeyError:
                print('Invalid input. Please enter a valid originating code.')

    
    def _get_dest_inputs(self, dest_flights: list) -> list:
        'Gets a valid destination airports from the user'
        print ('\nEnter destination airport code(s) one at a time:')
        dests = []

        while True:
            try:
                code = input()

                if not code:
                    if not dests:
                        raise KeyError('Please enter at least one valid destination code.')
                    else:
                        break
                elif not code in [data[0] for data in dest_flights]:
                    raise KeyError('Please enter a valid destination code.')
                elif code in [dest[0] for dest in dests]:
                    raise KeyError('That destination has already been entered.')
                else:
                    matched_dest = next(data for data in dest_flights if data[0] == code)
                    dests.append((matched_dest[0], float(matched_dest[2])))
            except KeyError as e:
                print('Invalid input:', e)

        return sorted(dests, key=lambda x: x[1])


    def _print_orig_codes(self) -> None:
        'Prints the originating codes'
        print('Available originating airports:')
            
        for code, data in self._flights.items():
            print(f'{code} - {data[0]}')


    def _print_dest_codes(self, dest_flights: list) -> None:
        'Prints the destination data'
        print('\nAvailable destination airports:')

        for dest in dest_flights:
            code, name = dest[0], dest[1]
            try:
                price = '{:.2f}'.format(float(dest[2]))
            except:
                price = 'N/A'

            print(f'{code} - {name} - ${price}')


    def _print_dest_prices(self, orig_code: str, dest_flights: list) -> None:
        'Prints the destination prices'
        print (
            f'Selected destination flights from {orig_code} sorted from '
            'low to high:')

        for dest in dest_flights:
            code = dest[0]
            try:
                price = '{:.2f}'.format(float(dest[1]))
            except:
                price = 'N/A'

            print(f'{code} - ${price}')
    

if __name__ == '__main__':
    Flight_Checker(DEBUG=False).execute()
    
