from faker import Faker

fake = Faker()
for _ in range(10):
    # Rastgele bir isim oluştur
    name = fake.name()
    
    # Rastgele bir adres oluştur
    address = fake.address()
    
    # Rastgele bir metin paragrafı oluştur
    text = fake.text()
   
    # Rastgele bir doğum tarihi oluştur
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
   
    print("****************************************************************")

    print("Name:", name,"   ","Address:", address,"   ","Date of Birth:", date_of_birth,"   ","Text:", text)
