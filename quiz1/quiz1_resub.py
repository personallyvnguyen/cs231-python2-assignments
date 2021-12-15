# quiz1.py
#
# A231 Python 2 Spring 2021
# Credit: Van Nguyen, C02699930
# Quiz 1 Resubmission.


def count_lines_in_file(file_path: str) -> int:
    '''
    Given the path to a file, returns the number of lines of text in
    that file, or raises exceptions in a couple of different
    circumstances:

    * An OSError if the file could not be opened successfully.
    * A ValueError if the file could not be read (e.g., it was not
      a text file, but was instead something else).
    '''

    the_file = None

    try:
        the_file = open(file_path, 'r')
        line_count = 0

        for line in the_file:
            line_count += 1

        return line_count

    finally:
        if the_file != None:
            the_file.close()



def run_user_interface() -> None:
    '''
    Repeatedly asks the user to specify a file; each time, the number of
    lines of text in the file are printed, unless the file could not be
    opened, in which case a brief error message is displayed instead.
    '''

    print('Welcome to my Fancy Line Counting Module. Version 1 by A.\n'
        'Thorton, and Version 2 is brought to you by Van Nguyen, a\n'
        'student in CS231 of Spring 2021.\n')

    while True:
        file_path = input('What file? ').strip()

        if file_path == '':
            break

        try:
            lines_in_file = count_lines_in_file(file_path)

            if lines_in_file < 64:
                print(f'There are less than 64 lines in {file_path}')
            elif lines_in_file == 64:
                print(f'There are exactly 64 lines in {file_path}')
            elif lines_in_file >= 65 and lines_in_file <= 256:
                print(f'There are between 65 and 256 lines in {file_path}')
            else:
                print(f'There are more than 256 lines in {file_path}')
        except OSError:
            print('Failed to open the file successfully')
        except ValueError:
            print('Failed to read from the file successfully; '
                  'it is not a text file')



def test_count_lines() -> None:
    'Tests the function count_lines_in_file()'
    f = open('testfile.txt', 'w')

    for i in range(10):
        f.write(f'Line {i} \n')
    f.close()

    assert count_lines_in_file('testfile.txt') == 10
    print('All tests passed.\n')
    print('-'*20, '\n')



if __name__ == '__main__':
    test_count_lines()
    run_user_interface()

