import socket

def run_udp_client():
    # Создаем UDP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Отправка датаграмм
    while True:
        message = input("Введите датаграмму (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break
        client_socket.sendto(message.encode(), ('localhost', 5000))

        # Получение ответа
        data, addr = client_socket.recvfrom(1024)
        print("Ответ от сервера:", data.decode())

    # Закрытие соединения
    client_socket.close()

# Запуск клиента
run_udp_client()

