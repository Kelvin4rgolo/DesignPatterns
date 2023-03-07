from action import Action
from command import Command


class Account:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def process(self, command: Command):
        command.check_success()
        if command.action == Action.DEPOSIT:
            self.balance += command.amount

        elif command.action == Action.WITHDRAW and (self.balance - command.amount >= 0) and command.success == True:
            self.balance -= command.amount
            print(f'Success! Your actual account-balance is ${self.balance}')
            
        else:
            print(f'Fail in withdraw. Your account-balance is ${self.balance}. Try again a new value.')
            command.success = False

    def __str__(self) -> str:
        return f'The account-balance is ${self.balance}'