from address import Address


class Mailing:
    def __init__(
            self, to_address: Address,
            from_address: Address, cost: int, track: str
            ):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.from_address.pc}, "
                f"{self.from_address.ci}, {self.from_address.st}, "
                f"{self.from_address.ho} - {self.from_address.fl} в "
                f"{self.to_address.pc}, {self.to_address.ci}, "
                f"{self.to_address.st}, {self.to_address.ho} - "
                f"{self.to_address.fl}. Стоимость {self.cost} рублей."
                )
