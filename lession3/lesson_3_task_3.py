from address import Address
from mailing import Mailing


to_address = Address(623280, "Ревда", "Мира", 31, 39)
from_address = Address(620078, "Екатеринбург", "Библиотечная", 45, 499)
track = "666585445214452 - Письмо"
cost = 95

mailing = Mailing(from_address, to_address, cost, track)

print(mailing)
