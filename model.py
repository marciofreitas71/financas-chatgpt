import sqlite3

class Model:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self._create_table()

    def _create_table(self):
        # Criar a tabela de despesas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            );
        ''')
        
        # Criar a tabela de receitas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS incomes (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            );
        ''')
        
        self.conn.commit()

    def add_expense(self, description, amount, date):
        self.cursor.execute('''
            INSERT INTO expenses (description, amount, date)
            VALUES (?, ?, ?);
        ''', (description, amount, date))
        self.conn.commit()

    def add_income(self, description, amount, date):
        self.cursor.execute('''
            INSERT INTO incomes (description, amount, date)
            VALUES (?, ?, ?);
        ''', (description, amount, date))
        self.conn.commit()

    def get_expenses(self):
        self.cursor.execute('''
            SELECT * FROM expenses;
        ''')
        return self.cursor.fetchall()

    def get_incomes(self):
        self.cursor.execute('''
            SELECT * FROM incomes;
        ''')
        return self.cursor.fetchall()
