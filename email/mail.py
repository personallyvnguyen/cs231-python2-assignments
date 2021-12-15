# mail.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Assignment: Email this Class


class Message():
    'Models an e-mail message'

    def __init__(self, sender: str, recipient: str) -> None:
        'Initializes the instance variables'
        self._sender = sender
        self._receipient = recipient
        self._message = ""


    def add_line(self, text: str) -> None:
        'Appends line of text to the message body'
        self._message += '\n' + text

    
    def show(self) -> str:
        'Shows the sender, recipient, and message'
        return (
            f'TO: {self._receipient}\n'
            f'FROM: {self._sender}\n\n'
            f'{self._message}'
        )

    
    def write(self, file_name: str) -> None:
        'Writes message to file'
        f = open(file_name, 'w')
        f.write(self.show())
        f.close()


    def __str__(self) -> str:
        'Returns string containing summary of message'
        
        message = self._message.replace("\r", "").replace("\n", "")[0:25]

        return (
            f'TO: {self._receipient} '
            f'FROM: {self._sender}: '
            f'{message}'
        )

    
    def get_sender(self) -> str:
        'Returns address of the sender'
        return self._sender

    
    def get_recipient(self) -> str:
        'Returns address of the recipient'
        return self._receipient

    

class Mailbox():
    'Stores email messages using the Message class'

    def __init__(self, owner: str, sent: list[Message], 
                 received: list[Message]) -> None:
        'Initializes the instance variables'
        self.__owner = owner
        self.__sent = sent
        self.__received = received


    def add_message(self, msg: Message) -> None:
        'Adds the message to the end of the mailbox'
        if msg.get_sender() == self.__owner:
            self.__sent.append(msg)
        if msg.get_recipient() == self.__owner:
            self.__received.append(msg)

    
    def display(self) -> None:
        'Prints a numbered summary of the messages'
        
        print('INBOX:')
        for idx, msg in enumerate(self.__received, 1):
            print(f'{idx}. {msg}')

        print('\nSENT:')
        for idx, msg in enumerate(self.__sent, 1):
            print(f'{idx}. {msg}')


    def get_message(self, idx: int, incoming: bool) -> Message:
        'Retrieves message from inbox or outbox'
        if incoming:
            return self.__received[idx - 1]
        else:
            return self.__sent[idx - 1]


    def delete(self, idx: int, incoming: bool) -> Message:
        'Deletes message from inbox or outbox'
        if incoming:
            return self.__received.pop(idx)
        else:
            return self.__sent.pop(idx)

    
    def filter(self, sender: str, recipient: str) -> list[Message]:
        '''
        Returns a list of Message objects that match the filter 
        criteria
        '''

        filtered = []

        for msg in self.__received:
            if msg.get_sender() == sender and msg.get_recipient() == recipient:
                filtered.append(msg)
        
        for msg in self.__sent:
            if msg.get_sender() == sender and msg.get_recipient() == recipient:
                filtered.append(msg)

        return filtered


    def __str__(self) -> str:
        'Returns a summary of the mailbox'
        return (
            f"{self.__owner}'s Mailbox – contains "
            f"{len(self.__received) + len(self.__sent)} messages"
        )

