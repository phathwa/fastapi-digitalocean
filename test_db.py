from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Corrected Database configuration
DATABASE_URL = "mysql+pymysql://asandeon_test_user:_Phtmer%26010@asande.online:3306/asandeon_test_db"

# Create an engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

def test_connection():
    try:
        # Connect to the database
        with engine.connect() as connection:
            # Perform a simple query to test the connection using text()
            result = connection.execute(text("SELECT 1"))
            if result.scalar() == 1:
                print("Database connection successful!")
            else:
                print("Unexpected result from the database.")
    except OperationalError as e:
        print("Database connection failed!")
        print(f"Error: {e}")
    except Exception as e:
        print("An error occurred!")
        print(f"Error: {e}")

# Run the test
if __name__ == "__main__":
    test_connection()
