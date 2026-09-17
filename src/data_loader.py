import os
import sys
import pandas as pd
from typing import Tuple, Dict, List, Any

def check_file_and_columns(file_path: str, required_cols: set) -> None:
    """Validate that target file exists and contains all required columns."""
    if not os.path.exists(file_path):
        print(f"Error: Missing file at path '{file_path}'. Exiting.")
        sys.exit(1)
        
    sample_df = pd.read_csv(file_path, nrows=1)
    missing_cols = required_cols - set(sample_df.columns)
    if missing_cols:
        print(f"Error: Missing required column(s): {missing_cols}. Exiting.")
        sys.exit(1)

def load_and_filter_csv(
    file_path: str, 
    cat1_col: str, 
    cat1_val: str, 
    cat2_col: str, 
    cat2_val: str
) -> Tuple[pd.DataFrame, pd.DataFrame, List[Dict[str, Any]]]:
    """Load raw dataset and apply two-condition filter."""
    audit_log = []
    
    df_raw = pd.read_csv(file_path, low_memory=False)
    raw_rows = len(df_raw)
    
    audit_log.append({
        "step": 1,
        "operation": "Load Raw File",
        "rule": "Read 2015.csv",
        "rows_before": raw_rows,
        "rows_after": raw_rows
    })

    condition = (df_raw[cat1_col] == cat1_val) & (df_raw[cat2_col] == cat2_val)
    df_filtered = df_raw.loc[condition].copy()
    filtered_rows = len(df_filtered)

    if filtered_rows == 0:
        print(f"Error: Filter ({cat1_col}=='{cat1_val}' & {cat2_col}=='{cat2_val}') returned 0 rows. Exiting.")
        sys.exit(1)

    audit_log.append({
        "step": 2,
        "operation": "Apply 2-Condition Filter",
        "rule": f"{cat1_col} == '{cat1_val}' AND {cat2_col} == '{cat2_val}'",
        "rows_before": raw_rows,
        "rows_after": filtered_rows
    })

    return df_raw, df_filtered, audit_log