import os

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_expense(self):
        description, amount, date = self.view.get_expense_input()
        self.model.add_expense(description, amount, date)

    def add_income(self):
        description, amount, date = self.view.get_income_input()
        self.model.add_income(description, amount, date)

    def show_expenses(self):
        expenses = self.model.get_expenses()
        self.view.display_expenses(expenses)

    def show_incomes(self):
        incomes = self.model.get_incomes()
        self.view.display_incomes(incomes)

    def show_options(self):
        self.view.display_options()

    def start(self):
        while True:
            self.show_options()
            option = int(input("Selecione uma opção: "))
            if option == 1:
                os.system('cls') or None
                self.add_expense()                
            elif option == 2:
                os.system('cls') or None
                self.add_income()
            elif option == 3:
                os.system('cls') or None
                self.show_expenses()
            elif option == 4:
                os.system('cls') or None
                self.show_incomes()
            #criar uma função que mostra o relatório
            elif option == 5:
                os.system('cls') or None
                self.show_report()
            elif option == 6:
                break
           

