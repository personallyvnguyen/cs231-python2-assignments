# credit_card.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Project 3 unittest suite


class Credit_Card():
    'Models a credit card'

    def __init__(
            self, balance: float = 0, 
            limit: float = 1200, 
            rate: float = 0.07) -> None:
        self.__balance = balance
        self.__credit_limit = limit
        self.__interest_rate = rate


    def adjust_limit(self, limit: float) -> None:
        'Changes the credit limit'
        if limit >= 0:
            self.__credit_limit = limit


    def adjust_interest_rate(self, rate: float) -> None:
        'Changes the interest rate'
        if rate >= 0:
            self.__interest_rate = rate

    
    def get_balance(self) -> float:
        'Returns the credit card balance'
        return self.__balance

    
    def make_payment(self, amount: float) -> None:
        'Subtracts payment from balance'
        self.__balance -= amount

    
    def add_charge(self, amount: float) -> bool:
        'Adds charge if new balance is under credit limit'
        if amount + self.__balance > self.__credit_limit:
            return False
        else:
            self.__balance += amount
            return True


    def compute_bill(self, interest: bool) -> float:
        'Returns the bill amount with or without interest'
        calc_interest = 1 + self.__interest_rate if interest else 1
        new_balance = round(self.__balance * calc_interest)
        self.__balance = new_balance
        return new_balance

    
    def __str__(self) -> str:
        return (
            f'Balance: {self.__balance}\n'
            f'Interest Rate: {self.__interest_rate}\n'
            f'Credit Limit: {self.__credit_limit}'
        )

