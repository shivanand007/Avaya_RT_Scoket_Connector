from sockets import start_csplit_socket, start_cvdn_socket
import threading



if __name__ == "__main__":

    listener_thread1 = threading.Thread(target=start_csplit_socket)
    listener_thread2 = threading.Thread(target=start_cvdn_socket)

    listener_thread2.start()
    listener_thread1.start()

    listener_thread2.join()
    listener_thread1.join()




