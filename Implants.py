

class Implants:
    def __init__(self,implants: list ):
        """Класс для хранения и управления имплантами персонажа."""
        self.implants = implants
        self.dict_implants = {'cyber arm': False,
                 'sandevistan': False,
                 'cyber legs': False,
                 'cyber face': False,
                 }

        for implant in implants:
            if implant in self.dict_implants:
                self.dict_implants[implant] = True
    def get_implants(self):
        """Возвращает список надетых имплантов."""
        return [implant for implant, active in self.dict_implants.items() if active]
