import socket

def resolve_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error:
        return None

domain = input("Введите доменное имя: ")
ip = resolve_dns(domain)
if ip:
    print(f"IP-адрес {domain}: {ip}")
else:
    print(f"Не удалось разрешить доменное имя {domain}.")
