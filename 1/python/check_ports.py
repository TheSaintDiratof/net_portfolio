def check_open_ports():
    """Проверка открытых портов на указанном хосте."""
    import socket  # Для работы с сетевыми соединениями

    # Запрашиваем адрес хоста у пользователя
    host = input("Введите адрес хоста: ")
    # Запрашиваем порты для проверки и преобразуем их в список целых чисел
    ports = list(map(int, input("Введите порты (через запятую): ").split(',')))

    open_ports = []  # Список для хранения открытых портов
    # Проходим по каждому порту и проверяем его доступность
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Устанавливаем таймаут на 1 секунду
            # Проверяем, открыт ли порт
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)  # Добавляем открытый порт в список

    # Выводим результаты проверки
    if open_ports:
        print(f"Открытые порты на {host}: {open_ports}")
    else:
        print(f"Нет открытых портов на {host}.")

check_open_ports()
