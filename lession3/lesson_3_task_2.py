from smartphone import Smartphone


smartphone1 = Smartphone("Sony", "Xperia", "+79123456789")
smartphone2 = Smartphone("Simens", "A52", "+79234567891")
smartphone3 = Smartphone("Xiaomi", "Redmi15", "+79345678912")
smartphone4 = Smartphone("Samsung", "S25", "+79456789123")
smartphone5 = Smartphone("Nokia", "8800", "+79567891234")

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for smartphone in catalog:
    print(f"{smartphone.matel} - {smartphone.motel}. {smartphone.notel}")
