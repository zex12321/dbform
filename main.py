import sqlite3
from nicegui import ui

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY,
            date TEXT,
            source TEXT,
            organization TEXT,
            incident_type TEXT,
            attack_ip TEXT,
            attack_methods TEXT,
            consequences TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Функция для сохранения данных в базе данных
def save_incident(date, source, organization, incident_type, attack_ip, attack_methods, consequences):
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO incidents (date, source, organization, incident_type, attack_ip, attack_methods, consequences)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (date, source, organization, incident_type, attack_ip, attack_methods, consequences))
    conn.commit()
    conn.close()

# Создание формы
ui.label('Введите данные об инциденте безопасности')

date_field = ui.input('Дата сообщения', placeholder='ДД.ММ.ГГГГ')
source_field = ui.input('Источник сообщения', placeholder='Введите источник')
organization_field = ui.input('Название организации', placeholder='Введите название')
incident_type_field = ui.input('Тип инцидента', placeholder='Введите тип инцидента')
attack_ip_field = ui.input('Атакуемые IP-адреса', placeholder='Введите IP-адреса')
attack_methods_field = ui.input('Используемые методы атаки', placeholder='Введите методы атаки')
consequences_field = ui.input('Возможные последствия', placeholder='Введите последствия')

def submit_form():
    save_incident(
        date_field.value,
        source_field.value,
        organization_field.value,
        incident_type_field.value,
        attack_ip_field.value,
        attack_methods_field.value,
        consequences_field.value
    )
    ui.notify('Информация об инциденте сохранена!')
    # Очистить поля после отправки
    date_field.clear()
    source_field.clear()
    organization_field.clear()
    incident_type_field.clear()
    attack_ip_field.clear()
    attack_methods_field.clear()
    consequences_field.clear()

ui.button('Отправить', on_click=submit_form)

ui.run(port=8082)