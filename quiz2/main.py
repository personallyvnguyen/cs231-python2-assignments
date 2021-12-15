# main.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Quiz: 2


from messaging import TextMessage


def test_text_message() -> None:
    'Tests the TextMessage class'

    msg1 = TextMessage('Bob', 'Joe')
    msg2 = TextMessage('Bobby', 'Joel')
    msg3 = TextMessage('Bobbette', 'Joette')
    
    # add_line()
    assert msg1.add_line('i love you too') == True
    assert msg2.add_line('x' * 3) == True
    assert msg3.add_line('x' * 141) == False

    # show()
    assert msg1.show() == 'FROM: Bob\ni love you too'
    assert msg2.show() == 'FROM: Bobby\nxxx'
    assert msg3.show() == 'FROM: Bobbette'

    # get_sender()
    assert msg1.get_sender() == 'Bob'
    assert msg2.get_sender() == 'Bobby'
    assert msg3.get_sender() == 'Bobbette'

    # get_recipient()
    assert msg1.get_recipient() == 'Joe'
    assert msg2.get_recipient() == 'Joel'
    assert msg3.get_recipient() == 'Joette'

    # grandmafy()
    msg1.grandmafy()
    msg2.grandmafy()
    msg3.grandmafy()

    assert msg1.show() == 'FROM: Bob\ni love u too'
    assert msg2.show() == 'FROM: Bobby\nxxx'
    assert msg3.show() == 'FROM: Bobbette'

    print('All tests passed.\n')



if __name__ == '__main__':
    test_text_message()

