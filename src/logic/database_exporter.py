# src/logic/database_exporter.py

import mysql.connector
from src.utils.i18n import gettext_gettext  # ✅ Import translation

def export_to_database(results, file_name, date):
    """ ✅ Exports validation results to MySQL database. """
    try:
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
            INSERT INTO validation_reports (file_name, date, segment_id, source_text, target_text, qa_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        # ✅ Insert the validation results into the database
        for segment_id, source_text, target_text, qa_status in results:
            cursor.execute(insert_query, (file_name, date, segment_id, source_text, target_text, qa_status))

        # ✅ Commit the transaction
        conn.commit()

        # ✅ Close the connection
        cursor.close()
        conn.close()

        print(gettext_gettext("Validation results exported to database successfully."))

    except mysql.connector.Error as e:
        print(gettext_gettext(f"Error: {e}"))
