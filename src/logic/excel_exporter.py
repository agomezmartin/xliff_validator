import pandas as pd
from PySide6.QtWidgets import QFileDialog
import gettext

# Initialize gettext for translations
gettext.bindtextdomain("messages", "locale")
gettext.textdomain("messages")
translation = gettext.translation("messages", "locale", fallback=True)
gettext_gettext = translation.gettext

def export_to_excel(validation_results, parent_window):
    """
    ✅ Exports validation results to an Excel (.xlsx) file.
    """
    # User selects save location
    file_path, _ = QFileDialog.getSaveFileName(
        parent_window,
        gettext_gettext("Save Excel File"),
        "",
        gettext_gettext("Excel Files (*.xlsx)")
    )

    if not file_path:
        return  # User cancelled

    # Convert validation results into DataFrame
    df = pd.DataFrame(validation_results, columns=[
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
        table_range = f"A1:D{num_rows + 1}"  # Adjust for headers
        worksheet.add_table(table_range, {
            "columns": [{"header": col} for col in df.columns],
            "style": "TableStyleMedium9"
        })

        # Freeze first row (headers)
        worksheet.freeze_panes(1, 0)

    print(gettext_gettext("Excel export completed successfully!"))
