import json
import logging
from database import Database, DatabaseConnectionError
from sqlite3 import Error as SQLiteError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    with Database() as connection:
        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Execute the query to retrieve data
            cursor.execute('SELECT * FROM Locations')

            # Open the file with correct encoding
            with open('where.js', 'w', encoding="utf-8") as file:
                file.write("myData = [\n")
                count = 0
                for row in cursor:
                    data = row[1]  # Assuming this is already a string
                    try:
                        js = json.loads(data)
                        logging.debug(f"Parsed JSON: {js}")
                    except json.JSONDecodeError:
                        logging.warning("JSON decoding failed for data: %s", data)
                        continue

                    if not ('status' in js and js['status'] == 'OK'): 
                        continue

                    # Extract latitude and longitude
                    try:
                        lat = js["results"][0]["geometry"]["location"]["lat"]
                        lng = js["results"][0]["geometry"]["location"]["lng"]
                        where = js['results'][0]['formatted_address']
                        if lat == 0 or lng == 0: 
                            continue
                        where = where.replace("'", "")

                        # Write to the file in the correct format
                        count += 1
                        if count > 1: 
                            file.write(",\n")
                        output = f"[{lat}, {lng}, '{where}']"
                        logging.info(f"[{lat}, {lng}, '{where}']")
                        file.write(output)
                    except KeyError as e:
                        logging.warning("KeyError: %s in JSON data: %s", e, js)
                        continue
                    except Exception as e:
                        logging.error("Unexpected error writing output: %s", e)
                        continue

                file.write("\n];\n")         
                logging.info(f"{count} records written to where.js")
                logging.info("Open where.html to view the data in a browser")

        except SQLiteError as e:
            logging.error("Error creating cursor: %s", e)

        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
                logging.info("Cursor closed.")

except DatabaseConnectionError as e:
    logging.error("Error: %s", e)

finally:
    if 'connection' in locals() and connection:
        connection.close()
