import pandas as pd
from PySide6.QtWidgets import QFileDialog
from src.utils.i18n import gettext_gettext  # ✅ Import translation

def export_to_excel(validation_results, parent_window):
    """
    ✅ Exports validation results to an Excel (.xlsx) file.
    """
    try:
        message = "" # message
        # User selects save location
        file_path, _ = QFileDialog.getSaveFileName(
            parent_window,
            gettext_gettext("Save Excel File"),
            "",
            gettext_gettext("Excel Files (*.xlsx)")
        )

        if not file_path:
            return  # User cancelled

        # Add segment number to the results (starting from 1)
        results_with_number = [
            (index + 1, *result)  # Adding segment number at the start of each tuple
            for index, result in enumerate(validation_results)
        ]

        # Convert validation results into DataFrame with the segment number
        df = pd.DataFrame(results_with_number, columns=[
            gettext_gettext("Segment Number"),
            gettext_gettext("Segment ID"),
            gettext_gettext("Source"),
            gettext_gettext("Target"),
            gettext_gettext("QA Status")
        ])

        # Save DataFrame to Excel with formatting
        with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name="QA Report", index=False)

            # Get workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets["QA Report"]

            # Define table format
            num_rows, num_cols = df.shape
            table_range = f"A1:E{num_rows + 1}"  # Adjust for headers (now 5 columns)
            worksheet.add_table(table_range, {
                "columns": [{"header": col} for col in df.columns],
                "style": "TableStyleLight19"
            })

            # Freeze first row (headers)
            worksheet.freeze_panes(1, 0)
            message = gettext_gettext("Excel export completed successfully!")
            
            return True, message
    
    except FileNotFoundError:
        message = gettext_gettext("❌ Error: File path not found.")
        return False, message

    except PermissionError:
        message = gettext_gettext("❌ Error: File is open. Please close it and try again.")
        return False, message

    except ValueError as ve:
        message = gettext_gettext(f"❌ Value Error: {ve}")
        return False, message

    except IOError:
        message = gettext_gettext("❌ IOError: Problem writing to file.")
        return False, message

    except Exception as e:
        message = gettext_gettext(f"❌ Unexpected Error: {e}")
        return False, message
