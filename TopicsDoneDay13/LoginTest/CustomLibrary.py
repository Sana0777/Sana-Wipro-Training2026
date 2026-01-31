from robot.api.logger import info


# ---------------- Dummy Backend ----------------

class TestObject:

    def __init__(self, ip):
        self.ip = ip
        info(f"Connected to server {ip}")

    def authenticate(self, login, password):

        if password == "1234567890":
            return f"session_{login}"

        # IMPORTANT: Raise error clearly
        raise Exception("Invalid Password")

    def get_version(self, token):
        return "1.0"

    def get_user_name(self, token):
        return "Tony Stark"

    def logout(self, token):
        info("Logged out")


# ---------------- Robot Library ----------------

class CustomLibrary:

    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self):
        self._connection = None
        self._session = None

    def connect(self, ip):
        self._connection = TestObject(ip)

    def disconnect(self):
        self._connection = None
        self._session = None

    def login_user_keyword(self, login, password):
        """
        This keyword does login and raises error if password is wrong
        """
        self._session = self._connection.authenticate(login, password)

    def get_server_version(self):

        if not self._session:
            raise Exception("Not Logged In")

        return self._connection.get_version(self._session)

    def get_user_name(self):

        if not self._session:
            raise Exception("Not Logged In")

        return self._connection.get_user_name(self._session)
