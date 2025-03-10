import socket
import threading

# Функция для получения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print("Соединение с сервером разорвано.")
                break
            print(message)  # Выводим сообщение от сервера
        except ConnectionResetError:
            print("Соединение с сервером разорвано.")
            break

# Основная функция клиента
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "5.252.155.62"  # Фиксированный IP-адрес сервера
    server_port = 12345  # Порт сервера

    try:
        # Подключаемся к серверу
        client_socket.connect((server_ip, server_port))
        print("Подключено к серверу. Можете отправлять сообщения.")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return

    # Запускаем поток для получения сообщений
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Отправляем сообщения
    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()