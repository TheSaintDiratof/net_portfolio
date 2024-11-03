import os
import platform

def ping(host):
    # Определяем команду для пинга в зависимости от операционной системы
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = f"ping {param} 4 {host}"

    response = os.system(command)
    return response == 0

if __name__ == "__main__":
    host = input("Введите адрес хоста для пинга: ")
    if ping(host):
        print(f"{host} доступен.")
    else:
        print(f"{host} недоступен.")

