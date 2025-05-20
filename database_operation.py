from sqlalchemy import text
from database import get_db_session

session  = next(get_db_session())

def get_patients_from_database(self):
    try: 
        query = text("""Select name_surname, year_of_birth, address, phone_number FROM patients """)
        result = session.execute(query).fetchall()
        return result
    finally:
        session.close()