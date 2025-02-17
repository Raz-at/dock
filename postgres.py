from sqlalchemy import create_engine, text
from faker import Faker

def get_db_connection():
    return create_engine('postgresql://user:password@postgres:5432/postgresDB')

while True:
    try:
        db_engine = get_db_connection().connect()
        print("Database connection successful!")
        break
    except Exception as e:
        print("Error..", e)
        continue

fake = Faker('en_US')

for i in range(10):
    print(f"Inserting record no {i + 1}")
    name = fake.name()
    insert_query = text("INSERT INTO dock.user_detail (name) VALUES (:name)")
    db_engine.execute(insert_query, {"name": name})
    print(f"Completed {i+1}")

db_engine.close()
