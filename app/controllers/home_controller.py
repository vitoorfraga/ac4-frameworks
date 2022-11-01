class HomeController:
    def index(self):
        return "Olá, você está na homepage!"

    def show(self, name):
        return f"Olá {name}"