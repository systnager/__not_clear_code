import threading

class Authenticator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.username = "admin"
            self.password = "secret"

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            return "Authenticated successfully"
        else:
            return "Authentication failed"

def main():
    auth1 = Authenticator()
    auth2 = Authenticator()

    print(f"auth1 is auth2: {auth1 is auth2}")

    print(auth1.authenticate("admin", "secret"))
    print(auth2.authenticate("admin", "bghuvd"))

    def test_authenticator():
        auth = Authenticator()
        print(f"Authenticator in thread: {auth}")

    threads = []
    for i in range(5):
        thread = threading.Thread(target=test_authenticator)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
