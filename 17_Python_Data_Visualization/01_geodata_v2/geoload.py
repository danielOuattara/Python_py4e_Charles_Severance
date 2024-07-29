import json
import sqlite3
import ssl
import urllib.parse
import urllib.request
import time
import logging
from database import Database, DatabaseConnectionError
from sqlite3 import Error as SQLiteError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# API configuration
api_key = False  # Change to your actual API key if available

if not api_key:
    api_key = 42  # Placeholder key for py4e example API
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

# SSL context for handling certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Function to process the geolocation
def process_geolocation(file_path: str):
    try:
        with Database() as connection:
            try:
                cursor = connection.cursor()

                # Create table if not exists
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

                with open(file_path, 'r') as file:
                    count = 0
                    for line in file:
                        if count > 200:
                            logging.info('Retrieved 200 locations, restart to retrieve more')
                            break

                        address = line.strip()
                        logging.info(f'Processing address: {address}')
                        cursor.execute("SELECT geodata FROM Locations WHERE address= ?",
                                       (memoryview(address.encode()),))

                        try:
                            data = cursor.fetchone()[0]
                            logging.info(f'Found in database: {address}')
                            continue
                        except TypeError:
                            pass  # No data found

                        params = {"address": address}
                        if api_key:
                            params['key'] = api_key
                        url = service_url + urllib.parse.urlencode(params)

                        logging.info(f'Retrieving URL: {url}')
                        uh = urllib.request.urlopen(url, context=ctx)
                        data = uh.read().decode()
                        logging.info(f'Retrieved {len(data)} characters')

                        try:
                            js = json.loads(data)
                        except json.JSONDecodeError as e:
                            logging.error(f'JSON decoding error: {e}')
                            continue

                        if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
                            logging.warning('Failure to Retrieve')
                            logging.debug(f'Error response data: {data}')
                            break

                        cursor.execute('''INSERT INTO Locations (address, geodata)
                                VALUES (?, ?)''', (memoryview(address.encode()), memoryview(data.encode())))
                        connection.commit()

                        # Uncomment the line below if you need to handle rate limits
                        if count % 10 == 0:
                            logging.info('Pausing for a bit...')
                            time.sleep(5)

                        count += 1

            except SQLiteError as e:
                logging.error(f"Database error: {e}")
            finally:
                if cursor:
                    cursor.close()
                    logging.info("Cursor closed.")

    except DatabaseConnectionError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()
            logging.info("Connection closed.")

    logging.info("Run geodump.py to read the data from the database so you can visualize it on a map.")


# Run the geolocation processing
if __name__ == "__main__":
    process_geolocation("locations.data")
