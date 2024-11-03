def get_provider_info():
    """Получение информации о провайдере по IP-адресу."""
    import requests  # Для выполнения HTTP-запросов

    # Запрашиваем у пользователя IP-адрес
    ip = input("Введите IP-адрес: ")
    # Выполняем запрос к сервису ipinfo.io для получения информации о провайдере
    response = requests.get(f"https://ipinfo.io/{ip}/json")

    if response.status_code == 200:
        # Если запрос успешен, выводим информацию
        info = response.json()
        print(f"Провайдер: {info.get('org', 'Неизвестно')}")
        print(f"Город: {info.get('city', 'Неизвестно')}")
        print(f"Штат: {info.get('region', 'Неизвестно')}")
        print(f"Страна: {info.get('country', 'Неизвестно')}")
    else:
        print("Не удалось получить информацию.")  # Обработка ошибок
get_provider_info()
