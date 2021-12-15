# messaging.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Quiz: 2


import re


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

    

class TextMessage(Message):
    'Models a text message'

    def add_line(self, text: str) -> bool:
        'Appends line of text to the message body'

        if (len(text) <= 140):
            self._message += '\n' + text
            return True
        else:
            return False


    def show(self) -> str:
        'Shows the sender, recipient, and message'
        return (
            f'FROM: {self._sender}'
            f'{self._message}'
        )

    
    def grandmafy(self) -> None:
        'Replaces "you" with "u" and replaces every "to" with "2"'
        self._message = re.sub(r'\byou\b', 'u', self._message)
        self._message = re.sub(r'\bto\b', '2', self._message)

