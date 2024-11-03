# L2

from scapy.all import sniff, Ether
from scapy.all import sniff, IP, IPv6, ICMP

# Функция для обработки перехваченных кадров
def frame_handler(frame):
    # Проверяем наличие Ethernet слоя
    if frame.haslayer(Ether):
        eth_layer = frame[Ether]

        # Извлекаем поля Ethernet-фрейма
        src_mac = eth_layer.src
        dst_mac = eth_layer.dst
        eth_type = eth_layer.type
        payload = eth_layer.payload
        crc = b'\x00\x00\x00\x00'  # Пример контрольной суммы

        # Форматируем вывод Ethernet фрейма в виде таблицы
        print("\n=== Ethernet Frame ===")
        print("-" * 40)
        print(f"| {'MAC-адрес источника:':<30} | {src_mac} (6 байт) |")
        print(f"| {'MAC-адрес назначения:':<30} | {dst_mac} (6 байт) |")
        print(f"| {'Тип протокола:':<30} | {eth_type} (0x{eth_type:X}) (2 байта) |")
        print(f"| {'Поле данных:':<30} | {bytes(payload)} ({len(payload)} байт) |")
        print(f"| {'Контрольная сумма (CRC):':<30} | {crc} (4 байта) |")
        print(f"| {'Размер Ethernet заголовка:':<30} | {len(eth_layer)} байт |")
        print("-" * 40)

# Начинаем перехват кадров
print("Начинаем перехват кадров...\n")
sniff(prn=frame_handler, count=2)  # Перехватываем 2 кадра

# Функция для обработки перехваченных пакетов
def packet_handler(packet):
    # Проверяем наличие IP-слоя
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print("\n=== IPv4 Packet ===")
        print("-" * 40)
        print(f"| {'Версия:':<30} | {ip_layer.version} (IPv4) |")  # 4 бита
        print(f"| {'Длина заголовка:':<30} | {ip_layer.ihl * 4} байт |")  # 4 бита
        print(f"| {'Тип обслуживания:':<30} | {ip_layer.tos} |")  # 8 бит
        print(f"| {'Длина пакета:':<30} | {len(packet)} байт |")  # 16 бит
        print(f"| {'Идентификация:':<30} | {ip_layer.id} |")  # 16 бит
        print(f"| {'Флаги:':<30} | {ip_layer.flags} |")  # 3 бита
        print(f"| {'Смещение фрагмента:':<30} | {ip_layer.frag} |")  # 13 бит
        print(f"| {'TTL:':<30} | {ip_layer.ttl} |")  # 8 бит
        print(f"| {'Протокол:':<30} | {ip_layer.proto} (0x{ip_layer.proto:X}) |")  # 8 бит
        print(f"| {'Контрольная сумма:':<30} | {ip_layer.chksum} |")  # 16 бит
        print(f"| {'Источник IP:':<30} | {ip_layer.src} |")  # 32 бит
        print(f"| {'Назначение IP:':<30} | {ip_layer.dst} |")  # 32 бит
        print("-" * 40)

    # Проверяем наличие IPv6-слоя
    elif packet.haslayer(IPv6):
        ipv6_layer = packet[IPv6]
        print("\n=== IPv6 Packet ===")
        print("-" * 40)
        print(f"| {'Версия:':<30} | {ipv6_layer.version} (IPv6) |")  # 4 бита
        print(f"| {'Traffic Class:':<30} | {ipv6_layer.tc} |")  # 8 бит
        print(f"| {'Flow Label:':<30} | {ipv6_layer.fl} |")  # 20 бит
        print(f"| {'Длина полезной нагрузки:':<30} | {len(ipv6_layer.payload)} байт |")  # 16 бит
        print(f"| {'Следующий заголовок:':<30} | {ipv6_layer.nh} (0x{ipv6_layer.nh:X}) |")  # 8 бит
        print(f"| {'TTL:':<30} | {ipv6_layer.hlim} |")  # 8 бит
        print(f"| {'Источник IPv6:':<30} | {ipv6_layer.src} |")  # 128 бит
        print(f"| {'Назначение IPv6:':<30} | {ipv6_layer.dst} |")  # 128 бит
        print("-" * 40)

# Начинаем перехват пакетов
print("Начинаем перехват пакетов...\n")
sniff(prn=packet_handler, count=2)  # Перехватываем 2 пакета

