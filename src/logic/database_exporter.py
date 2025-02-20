from src.utils.i18n import gettext_gettext  # ✅ Import translation
from src.utils.logs_config import logging

# Ensure MySQL modules are found
try:
    import mysql.connector
    # import MySQLdb

except ImportError as e:
    print(gettext_gettext(f"MySQL import error: {e}"))
    
def export_to_database(results, file_name, date_validated):
    """ ✅ Exports validation results to MySQL database. """
    try:
        message = "" # message

        # ✅ Establish a connection to the MySQL database
        conn = mysql.connector.connect(
            host="127.0.0.1",        # Your MySQL host
            user="root",             # Your MySQL username
            password="root",     # Your MySQL password
            database="xliff_validation"  # Database name
        )
        cursor = conn.cursor()

        # ✅ Prepare the insert query with placeholders for the data
        insert_query = """
            INSERT INTO validation_reports (file_name, date_validated, segment_id, source_text, target_text, qa_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        # ✅ Prepare a list of all rows to be inserted
        data_to_insert = [(file_name, date_validated, segment_id, source_text, target_text, qa_status) for segment_id, source_text, target_text, qa_status in results]

        # ✅ Execute the insert query in bulk using executemany()
        cursor.executemany(insert_query, data_to_insert)

        # ✅ Commit the transaction
        conn.commit()

        # ✅ Close the connection
        cursor.close()
        conn.close()

        print(gettext_gettext("Validation results exported to database successfully."))
        logging.info(gettext_gettext("Validation results exported to database successfully."))

        message = gettext_gettext("Validation results exported to database successfully.")

        return True, message

    except mysql.connector.Error as e:
        print(gettext_gettext(f"Connector error: {e}"))
        logging.error(gettext_gettext(f"Connector error: {e}"))
        
        message = gettext_gettext(f"Connector error: {e}")

        return False, message

    except Exception as e:
        print(gettext_gettext(f"Generic error in database exporter file: {e}"))
        logging.error(gettext_gettext(f"Generic error in database exporter file: {e}"))

        message = gettext_gettext(f"Generic error in database exporter file: {e}")

        return False, message
