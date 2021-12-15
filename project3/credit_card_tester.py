# credit_card_tester.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Project 3 unittest suite


import unittest

from credit_card import Credit_Card



class TestCreditCardClass(unittest.TestCase):
    'Runs a test suite on the Credit Card class'

    def setUp(self) -> None:
        'Sets up the test suite environment'
        self.card = Credit_Card()


    def test_adjust_limit(self) -> None:
        'Tests the adjust_limit() function'
        self.card.adjust_limit(-1000)
        self.assertEqual(
            self.card.__str__(),
            'Balance: 0\nInterest Rate: 0.07\nCredit Limit: 1200'
        )

        self.card.adjust_limit(1400)
        self.assertEqual(
            self.card.__str__(),
            'Balance: 0\nInterest Rate: 0.07\nCredit Limit: 1400'
        )


    def test_adjust_interest_rate(self) -> None:
        'Tests the adjust_interest_rate() function'
        self.card.adjust_interest_rate(-0.1)
        self.assertEqual(
            self.card.__str__(),
            'Balance: 0\nInterest Rate: 0.07\nCredit Limit: 1200'
        )

        self.card.adjust_interest_rate(0.01)
        self.assertEqual(
            self.card.__str__(),
            'Balance: 0\nInterest Rate: 0.01\nCredit Limit: 1200'
        )


    def test_get_balance(self) -> None:
        'Tests the get_balance() function'
        self.assertEqual(self.card.get_balance(), 0)


    def test_add_charge(self) -> None:
        'Tests the add_charge() function'
        self.assertFalse(self.card.add_charge(1800))
        self.assertTrue(self.card.add_charge(1000))
        self.assertEqual(self.card.get_balance(), 1000)


    def test_compute_bill(self) -> None:
        'Tests the compute_bill() function'
        self.card.add_charge(1000)
        self.assertEqual(self.card.compute_bill(False), 1000)
        self.assertEqual(self.card.get_balance(), 1000)
        self.assertEqual(self.card.compute_bill(True), 1070)
        self.assertEqual(self.card.get_balance(), 1070)


    def test_str_method(self) -> None:
        'Tests the __str__() function'
        self.assertEqual(
            self.card.__str__(),
            'Balance: 0\nInterest Rate: 0.07\nCredit Limit: 1200'
        )



if __name__ == '__main__':
    unittest.main()

