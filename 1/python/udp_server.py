import socket

def start_udp_server():
    # Создаем UDP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5000))
    print("UDP сервер запущен. Ожидание датаграмм...")

    # Получение и обработка датаграмм
    while True:
        data, addr = server_socket.recvfrom(1024)
        datagram = data.decode()
        print(f"Получена датаграмма от {addr}: {datagram}")
        response = f"Датаграмма '{datagram}' получена."
        server_socket.sendto(response.encode(), addr)

# Запуск сервера
start_udp_server()
