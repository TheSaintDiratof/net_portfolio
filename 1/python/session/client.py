import grpc
import session_pb2
import session_pb2_grpc

# Функция для запуска клиента
def run():
    # Создаем соединение с gRPC сервером
    with grpc.insecure_channel('localhost:50051') as channel:
        # Создаем "stub" для общения с сервисом SessionManager
        stub = session_pb2_grpc.SessionManagerStub(channel)
        session_id = "12345"  # Идентификатор сессии

        # Отправляем запрос на запуск сессии
        start_response = stub.StartSession(session_pb2.SessionRequest(session_id=session_id))
        # Выводим ответ о запуске сессии
        print(start_response.message)

        # Отправляем запрос на завершение сессии
        end_response = stub.EndSession(session_pb2.SessionRequest(session_id=session_id))
        # Выводим ответ о завершении сессии
        print(end_response.message)

# Запуск клиента
run()
