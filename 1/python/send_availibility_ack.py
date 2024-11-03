# Нужно внести не достающие данные вместо ххх

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
import platform

def ping_host(host):
    """Вспомогательная функция для пинга хоста."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = f"ping {param} 1 {host}"
    response = os.system(command)
    return response == 0

def send_email(host):
    """Отправка уведомления на почту."""
    sender_email = "minecraft-railcraft050@mail.ru"  # Ваш email
    receiver_email = "skobelevarik@gmail.com"  # Email получателя
    password = "3p9vgPei0pkxbMaeRXiW"  # Ваш пароль

    subject = f"Хост {host} доступен"
    body = f"Хост {host} доступен для подключения."

    # Создаем сообщение
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Отправка сообщения
    try:
        with smtplib.SMTP('smtp.bk.ru', 587) as server:
            server.starttls()  # Используем TLS
            server.login(sender_email, password)  # Вход в почтовый ящик
            server.send_message(msg)  # Отправка сообщения
        print(f"Уведомление отправлено на {receiver_email} о доступности {host}.")
    except Exception as e:
        print(f"Не удалось отправить уведомление: {e}")

def monitor_hosts():
    """Мониторинг доступности указанных хостов."""
    # Запрашиваем у пользователя адреса хостов для мониторинга
    hosts = input("Введите адреса хостов для мониторинга (через запятую): ")
    hosts = [host.strip() for host in hosts.split(',')]  # Убираем пробелы

    while True:  # Бесконечный цикл для постоянного мониторинга
        for host in hosts:
            # Проверяем доступность каждого хоста
            if ping_host(host):
                print(f"{host} доступен.")
                send_email(host)  # Отправка уведомления
            else:
                print(f"{host} недоступен.")
        time.sleep(5)  # Интервал 5 секунд между проверками

monitor_hosts()
