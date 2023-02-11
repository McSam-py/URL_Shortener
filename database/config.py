class Config:
    def __init__(self):
        self.db_url = ""
        self.base_url = ""
        pass

    def set_app_config(self, db_url="", base_url=""):
        self.db_url = db_url
        self.base_url = base_url

    def get_db_url(self):
        if self.db_url:
            return self.db_url
        else:
            print("Database URL has not been set")

    def get_base_url(self):
        if self.base_url:
            return self.base_url
        else:
            print("Base URL has not been set")
