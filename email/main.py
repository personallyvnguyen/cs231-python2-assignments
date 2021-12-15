# main.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Assignment: Email this Class


from mail import Message, Mailbox



class Email_Application():
    'User interface for interacting with mailbox and reading messages'

    def __init__(self) -> None:
        'Initializes the instance variables'
        self._running = True


    def execute(self) -> None:
        'Runs the code to start the application'
        self._setup()
        
        while self._running:
            self._print_menu()

            selection = int(input('Enter a number between 1 and 7: '))

            if selection == 1:
                self._compose_selection()
            elif selection == 2:
                self._display_selection()
            elif selection == 3:
                self._delete_selection()
            elif selection == 4:
                self._filter_selection()
            elif selection == 5:
                self._view_selection()
            elif selection == 6:
                self._print_selection()
            elif selection == 7:
                self._quit_selection()

    
    def _setup(self) -> None:
        'Sets up the mailbox of the user'

        print('\nWe need to set up your mailbox!')
        self._owner = input('Enter your email address: ')

        default_sent = [
            Message('me@xyz.com', 'f@xyz.com'),
            Message('me@xyz.com', 'd@xyz.com'),
            Message('me@xyz.com', 'c@xyz.com'),
            Message('me@xyz.com', 'i@xyz.com'),
            Message('me@xyz.com', 'i@xyz.com'),
        ]

        default_received = [
            Message('h@xyz.com', 'me@xyz.com'),
            Message('k@xyz.com', 'me@xyz.com'),
            Message('d@xyz.com', 'me@xyz.com'),
            Message('g@xyz.com', 'me@xyz.com'),
            Message('d@xyz.com', 'me@xyz.com'),
        ]

        for msg in default_sent:
            msg.add_line('Lorem Ipsum')

        for msg in default_received:
            msg.add_line('Lorem Ipsum')

        self._mailbox = Mailbox(self._owner, default_sent, default_received)
        self._inbox_size = len(default_sent)
        self._outbox_size = len(default_received)


    def _print_menu(self) -> None:
        'Prints the menu options'
        print(
            '\n\n'
            '1. COMPOSE\n'
            '2. DISPLAY\n'
            '3. DELETE\n'
            '4. FILTER\n'
            '5. VIEW\n'
            '6. PRINT\n'
            '7. QUIT\n'
        )


    def _compose_selection(self) -> None:
        'Compose a message'

        recipient = input("Enter recipient's email address: ")
        print('Begin entering the message')
        print('Enter two blank lines in a row to stop composing')
        
        message = Message(self._owner, recipient)
        blank_line_count = 0
        
        while blank_line_count < 2:
            line = input()
            message.add_line(line)

            if line.strip() == '':
                blank_line_count += 1
            else:
                blank_line_count = 0

        self._mailbox.add_message(message)
        self._outbox_size += 1


    def _display_selection(self) -> None:
        'Display the mailbox contents'
        self._mailbox.display()


    def _delete_selection(self) -> None:
        'Delete a message'

        incoming = input('Delete (I)ncoming or (O)utgoing message? ').lower()
        idx = 0

        if incoming == 'i':
            while idx < 1 or idx > self._inbox_size:
                idx = input(
                    f'Enter a number between 1 and {self._inbox_size}: ')
                idx = int(idx)
            
            incoming = True
            self._inbox_size -= 1
        elif incoming == 'o':
            while idx < 1 or idx > self._outbox_size:
                idx = input(
                    f'Enter a number between 1 and {self._outbox_size}: ')
                idx = int(idx)

            incoming = False
            self.__size -= 1

        self._mailbox.delete(idx, incoming)


    def _filter_selection(self) -> None:
        'Filter the messages'

        recipient = input(
            'Enter the recipient’s address to filter on, or enter to skip: ')
        sender = input(
            'Enter the sender’s address to filter on, or enter to skip: ')

        if sender.strip() == '':
            sender = self._owner

        print('Messages matching your query:')

        filtered = self._mailbox.filter(sender, recipient)

        for msg in filtered:
            print(msg)
        

    def _view_selection(self) -> None:
        'View a particular message'

        incoming = input('View (I)ncoming or (O)utgoing message? ').lower()
        idx = 0

        if incoming == 'i':
            incoming = True

            while idx < 1 or idx > self._inbox_size:
                idx = input(
                    f'Enter a number between 1 and {self._inbox_size}: ')
                idx = int(idx)
        elif incoming == 'o':
            incoming = False

            while idx < 1 or idx > self._outbox_size:
                idx = input(
                    f'Enter a number between 1 and {self._outbox_size}: ')
                idx = int(idx)

        print(self._mailbox.get_message(idx, incoming).show())


    def _print_selection(self) -> None:
        'Print a message to file'

        file_name = input('Enter the name of the file to print to: ')
        incoming = input('Print (I)ncoming or (O)utgoing message? ').lower()
        idx = 0

        if incoming == 'i':
            incoming = True

            while idx < 1 or idx > self._inbox_size:
                idx = input(
                    f'Enter a number between 1 and {self._inbox_size}: ')
                idx = int(idx)
        elif incoming == 'o':
            incoming = False

            while idx < 1 or idx > self._outbox_size:
                idx = input(
                    f'Enter a number between 1 and {self._outbox_size}: ')
                idx = int(idx)

        self._mailbox.get_message(idx, incoming).write(file_name)


    def _quit_selection(self) -> None:
        'Quit application'
        self._running = False
        print('Bye!')

    

if __name__ == '__main__':
    Email_Application().execute()

