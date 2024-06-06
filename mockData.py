from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
import datetime




# Veritabanı oluşturun
engine = create_engine('sqlite:///example.db')
Base = declarative_base()


# Kullanıcı modeli
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    name = Column(String)  # name sütunu eklendi
    address = Column(Text)
    date_of_birth = Column(DateTime)

# Tabloları oluşturun
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# Faker nesnesini oluşturun
fake = Faker()
# Mock data oluşturma  ve veritabanına kaydetme
for _ in range(10):
    user = User(
        name=fake.name(),
        username=fake.user_name(),
        email=fake.email(),
        address=fake.address(),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=90)
    )
    session.add(user)
session.commit()

# Query yapın ve sonuçları yazdırın
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Name: {user.name}, Address: {user.address}, Date of Birth: {user.date_of_birth}")

session.close()
