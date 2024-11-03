import grpc
from concurrent import futures
import session_pb2
import session_pb2_grpc

# Реализация сервиса SessionManager
class SessionManager(session_pb2_grpc.SessionManagerServicer):
    # Реализация метода StartSession
    def StartSession(self, request, context):
        # Возвращаем сообщение о том, что сессия запущена
        return session_pb2.SessionResponse(message=f"Сессия {request.session_id} запущена.")

    # Реализация метода EndSession
    def EndSession(self, request, context):
        # Возвращаем сообщение о том, что сессия завершена
        return session_pb2.SessionResponse(message=f"Сессия {request.session_id} завершена.")

# Функция для запуска сервера
def serve():
    # Создаем gRPC сервер с многопоточностью
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Регистрируем сервис SessionManager на сервере
    session_pb2_grpc.add_SessionManagerServicer_to_server(SessionManager(), server)
    # Указываем порт, на котором будет работать сервер
    server.add_insecure_port('[::]:50051')
    server.start()  # Запускаем сервер
    print("gRPC сервер запущен на порту 50051...")
    server.wait_for_termination()  # Ожидаем завершения работы сервера

# Запуск сервера
serve()
