class Config:
    def __init__(self):
        self.db_url = "sqlite:///database.sqlite3"
        self.base_url = "http://127.0.0.1:8000/"
        pass

    def get_db_url(self):
        # if self.db_url:
        return self.db_url
        # else:
        #     print("Database URL has not been set")

    def get_base_url(self):
        # if self.base_url:
        return self.base_url
        # else:
        #     print("Base URL has not been set")
