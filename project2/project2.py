# project2.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Project 2 File systems a project adapted from A. Thornton


from pathlib import Path
import os
import shutil



class File_Crawler():
    'Queries, filters, and acts on filtered results'

    @staticmethod
    def get_first_line(path: Path) -> str:
        'Returns the first line of a file'
        try:
            with path.open('r') as f:
                return f.readline().rstrip('\r\n')
        except:
            return('NOT TEXT')


    def execute(self) -> None:
        'Executes the application logic'
        query = self._query()
        self._print_paths(query)

        filtered_query = self._filter(query)
        self._print_paths(filtered_query)

        self._action(filtered_query)
            

    def _query(self) -> list[Path]:
        'Queries the contents of a directory and returns the results'
        cmd = path = None
        valid_input = False

        while not valid_input:
            input_args = input().split()

            try:
                cmd, path = input_args[0], Path(input_args[1])

                if (len(input_args) != 2 or
                    not cmd in 'DR' or
                    not path.is_dir()):
                    raise Exception
            except:
                print('ERROR')
                cmd = path = None
            else:
                valid_input = True
            
        query = None

        if cmd == 'D':
            query = self._crawl(path)
        elif cmd == 'R':
            query = self._crawl(path, True)

        return query


    def _crawl(self, path: Path, recursive: bool = False) -> list[Path]:
        'Recursively crawls through file system'
        if not recursive:
            return sorted(
                [item for item in list(path.iterdir()) if item.is_file()])
        else:
            files = []
            directories = []

            for item in path.iterdir():
                if item.is_dir():
                    directories = directories + self._crawl(item, True)
                elif item.is_file():
                    files.append(item)
                    
            return sorted(files) + sorted(directories)


    def _filter(self, paths: list[str]) -> list[str]:
        'Filters a list of paths and returns the filtered results'
        if not paths:
            return []

        cmd = cmd_arg = None
        valid_input = False

        while not valid_input:
            input_args = input().split()

            try:
                cmd = input_args[0]

                if cmd in 'A':
                    if len(input_args) != 1:
                        raise Exception
                elif cmd in 'NE':
                    cmd_arg = input_args[1]

                    if len(input_args) != 2:
                        raise Exception
                elif cmd in 'T':
                    cmd_arg = ' '.join(input_args[1:])

                    if len(input_args) < 3:
                        raise Exception
                elif cmd in '<>':
                    cmd_arg = int(input_args[1])

                    if len(input_args) != 2 or cmd_arg < 0:
                        raise Exception
            except:
                print('ERROR')
                cmd = cmd_arg = None
            else:
                valid_input = True
            
        filtered_paths = []
        
        if cmd == 'A':
            filtered_paths = paths
        elif cmd == 'N':
            filtered_paths = [path for path in paths if path.name == cmd_arg]
        elif cmd == 'E':
            cmd_arg = cmd_arg if cmd_arg[0] == '.' else f'.{cmd_arg}'
            filtered_paths = [path for path in paths if path.suffix == cmd_arg]
        elif cmd == 'T':
            for path in paths:
                try:
                    with path.open('r') as f:
                        if f.read().find(cmd_arg) != -1:
                            filtered_paths.append(path)
                except:
                    pass
        elif cmd == '<':
            filtered_paths = [
                path for path in paths if path.stat().st_size < cmd_arg] 
        elif cmd == '>':
            filtered_paths = [
                path for path in paths if path.stat().st_size > cmd_arg] 

        return filtered_paths


    
    def _action(self, paths: list[str]) -> None:
        'Acts on a list of paths'
        if not paths:
            return

        cmd = None
        valid_input = False

        while not valid_input:
            input_args = input().split()

            try:
                cmd = input_args[0]

                if not cmd in 'FDT' or len(input_args) != 1:
                    raise Exception
            except:
                print('ERROR')
                cmd = None
            else:
                valid_input = True

        if cmd == 'F':
            for path in paths:
                print(self.get_first_line(path))
        elif cmd == 'D':
            for path in paths:
                shutil.copy(path, f'{str(path)}.dup')
        elif cmd == 'T':
            for path in paths:
                os.utime(path, times=None)


    def _print_paths(self, paths: list[Path]) -> None:
        'Prints out a list of paths'
        for path in paths:
            print(path)



def testing() -> None:
    'Tests the File_Crawler.get_first_line method'

    for i in range(1, 4):
        f = open(f'testfile{i}.txt', 'w')
        f.write(f'Sample Text {i}')
        f.close()

    print('Running tests...')

    try:
        assert File_Crawler.get_first_line(Path('testfile1.txt')) == 'Sample Text 1'
        assert File_Crawler.get_first_line(Path('testfile2.txt')) == 'Sample Text 2'
        assert File_Crawler.get_first_line(Path('testfile3.txt')) == 'Sample Text 3'
    except AssertionError:
        print('A test for File_Crawler.get_first_line failed.')
    else:
        print('All tests passed.')



if __name__ == '__main__':
    testing()
    # File_Crawler().execute()

