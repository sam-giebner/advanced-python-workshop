import arcpy

def refresh_data(source_tbl, target_tbl):
    """
    Refreshes a table by truncating the records from the target tables and 
    then appends records from the source table to the target table.
    This function is often used to update a feature class from a SQL view.

    Parameters:
    source_tbl: (string) Path to table which will have it's records appended to the target table.
    target_tbl: (string) Path to table that will be refreshed.

    Returns:
    None
    """

    # Truncate target table
    arcpy.TruncateTable_management(
        in_table = target_tbl)
    
    # Append records from source to target table
    arcpy.Append_management(
        inputs = source_tbl,
        target = target_tbl,
        schema_type = "NO_TEST")