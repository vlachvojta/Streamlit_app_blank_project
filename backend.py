from database import Database


class Backend():
    """Backend side of webpage and bussines logic."""

    db = None
    data = None

    def __init__(self) -> None:
        """Init connection with database"""
        print('BACKEND:\tinit()')
        self.db = Database()

    def load_data(self):
        """Loads data from database."""
        print('BACKEND:\tData loading.')
        self.data = self.db.load_data()
        return self.data
