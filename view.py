class View:
    def display_expenses(self, expenses):
        """Exibe as despesas na tela."""
        print("Despesas:")
        for expense in expenses:
            print(f"{expense[1]}: {expense[2]} ({expense[3]})")

    def display_incomes(self, incomes):
        """Exibe as receitas na tela."""
        print("Receitas:")
        for income in incomes:
            print(f"{income[1]}: {income[2]} ({income[3]})")

    def get_expense_input(self):
        """Recebe a descrição, o valor e a data da despesa do usuário."""
        description = input("Descrição da despesa: ")
        amount = input("Valor da despesa: ")
        date = input("Data da despesa: ")
        return description, amount, date

    def get_income_input(self):
        """Recebe a descrição, o valor e a data da receita do usuário."""
        description = input("Descrição da receita: ")
        amount = input("Valor da receita: ")
        date = input("Data da receita: ")
        return description, amount, date

    def display_options(self):
        """Exibe as opções da aplicação para o usuário."""
        print("Opções:")
        print("1 - Adicionar despesa")
        print("2 - Adicionar receita")
        print("3 - Ver despesas")
        print("4 - Ver receitas")
        print("5 - Ver relatório")
        print("6 - Sair")
        
#create report function in the view
    def create_report(self, expenses, incomes):        
        print("Relatório:")
        print("Despesas:")
        for expense in expenses:
            print(f"{expense[1]}: {expense[2]} ({expense[3]})")
        print("Receitas:")
        for income in incomes:
            print(f"{income[1]}: {income[2]} ({income[3]})")
        print("Saldo: R$ {}".format(self.get_balance(expenses, incomes)))

