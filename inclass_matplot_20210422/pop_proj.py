
from matplotlib import pyplot as plt


FILE_NAME = 'localpops.txt'



class Population_Projection():
    'User interface to project city population'


    def __init__(self) -> None:
        'Initializes the instance variables'
        self._running = True
        self._cities = []

    
    def execute(self) -> None:
        'Runs the code to start the application'
        self._setup()

        while self._running:
            selection = int(input('\nPlease select your city: ')) - 1
            city = self._cities[selection]

            population = years = -1

            while population < 0:
                population = int(input('Enter the starting population: '))

                if population < 0:
                    print('Invalid Input.\n')

            while years < 0:
                years = int(input('Enter number of years: '))
                
                if years < 0:
                    print('Invalid Input.\n')

            annual_change = city[2] + city[3] - city[1]

            years_x = range(1, years + 1)
            pop_y = [population + year*annual_change for year in years_x]

            plt.title(f'Population Projection for {city[0]}')
            plt.xlabel('Years')
            plt.ylabel('Population')
            plt.grid()

            plt.plot(years_x, pop_y, color='k', marker='o')
            plt.show()


    def _setup(self) -> None:
        'Prints the welcome message and populates the cities data'

        print('Population Projection by Van Nguyen')
        print('-' * 35)

        try:
            with open(FILE_NAME, 'r') as f:
                lines = f.readlines()

                for line in lines:
                    data = [value.strip() for value in line.split(',')]
                    self._cities.append((
                        data[0],
                        int(data[1]),
                        int(data[2]),
                        int(data[3]),
                    ))
        except:
            print(
                'Unable to open file \'localpops.txt\'.\n'
                'Please check the file again and run the program again'
            )
            quit()

        print('The cities in our available data set:\n')

        for i, city in enumerate(self._cities, 1):
            print(f'{i} - {city[0]}')



if __name__ == '__main__':
    Population_Projection().execute()

