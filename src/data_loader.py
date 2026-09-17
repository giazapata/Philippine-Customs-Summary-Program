import os
import pandas as pd

def check_file_and_columns(file_path, required_cols):
    if not os.path.exists(file_path):
        return False, f"File not found at path: {file_path}"
    try:
        df_head = pd.read_csv(file_path, nrows=0, encoding='latin1', low_memory=False)
        df_head.columns = df_head.columns.str.strip()
        missing = [col for col in required_cols if col not in df_head.columns]
        if missing:
            return False, f"Missing required columns in dataset: {missing}"
        return True, "File and schema validation successful."
    except Exception as e:
        return False, f"Error validating schema: {str(e)}"


def load_and_filter_csv(file_path, cat1_col, cat1_val, cat2_col, cat2_val):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")
        
    df_raw = pd.read_csv(file_path, low_memory=False, encoding='latin1')
    df_raw.columns = df_raw.columns.str.strip()
    
    # Clean string representations
    col1_series = df_raw[cat1_col].astype(str).str.strip().str.lower()
    col2_series = df_raw[cat2_col].astype(str).str.strip().str.lower()
    
    val1_str = str(cat1_val).strip().lower()
    val2_str = str(cat2_val).strip().lower()

    # Match exact or partial string (e.g. '2015m1' within '2015m1')
    cond1 = col1_series.str.contains(val1_str, regex=False, na=False)
    cond2 = col2_series == val2_str

    df_filtered = df_raw.loc[cond1 & cond2].copy()
    
    # Fallback only if no matches are found
    if df_filtered.empty:
        print(f"[INFO] Primary filter ({val1_str} & {val2_str}) returned 0 rows. Falling back to currency='{val2_str}'.")
        df_filtered = df_raw.loc[cond2].copy()

    audit_records = {
        "total_rows": [len(df_raw)],
        "filtered_rows": [len(df_filtered)]
    }
    
    return df_raw, df_filtered, audit_records