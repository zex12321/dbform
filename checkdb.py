import sqlite3
from prettytable import PrettyTable

def fetch_incidents():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM incidents')
    incidents = cursor.fetchall()
    conn.close()
    return incidents

def display_incidents():
    incidents = fetch_incidents()
    if not incidents:
        print("Нет записей в базе данных.")
        return

    # Используем PrettyTable для форматированного вывода
    table = PrettyTable()
    table.field_names = ["ID", "Дата", "Источник", "Организация", "Тип инцидента", "IP", "Методы атаки", "Последствия"]

    for incident in incidents:
        table.add_row(incident)

    print(table)

if __name__ == "__main__":
    display_incidents()
