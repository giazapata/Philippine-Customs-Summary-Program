import os
import pandas as pd
import config
from src.data_loader import check_file_and_columns, load_and_filter_csv
from src.processor import DataProcessor

def main() -> None:
    print("--- Starting Customs Data Pipeline ---")
    
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)

    check_file_and_columns(config.DATA_PATH, config.REQUIRED_COLUMNS)

    df_raw, df_filtered, audit_records = load_and_filter_csv(
        config.DATA_PATH,
        config.CAT_COL_1, config.FILTER_CAT_1,
        config.CAT_COL_2, config.FILTER_CAT_2
    )

    processor = DataProcessor(df_filtered, config)
    processor.create_derived_columns()
    tables = processor.generate_summary_tables()

    tables["grouped"].to_csv(os.path.join(config.OUTPUT_DIR, "grouped.csv"), index=False)
    tables["grouped_two"].to_csv(os.path.join(config.OUTPUT_DIR, "grouped_two.csv"), index=False)
    tables["pivot"].to_csv(os.path.join(config.OUTPUT_DIR, "pivot.csv"))
    tables["top10"].to_csv(os.path.join(config.OUTPUT_DIR, "top10.csv"), index=False)

    pd.DataFrame(audit_records).to_csv(os.path.join(config.OUTPUT_DIR, "audit_log.csv"), index=False)

    processor.export_plots(tables["top10"], tables["pivot"])

    print("--- Pipeline execution complete! Check outputs/ folder. ---")

if __name__ == "__main__":
    main()

import os
import csv
import pandas as pd
import numpy as np

# Ensure outputs directory exists
os.makedirs('outputs', exist_ok=True)

# 1. Compute unit prices and valuation metrics
df['declared_unit_price'] = df['declared_value_php'] / df['quantity']
df['valuation_gap_pct'] = ((df['declared_unit_price'] - df['benchmark_unit_price']) / df['benchmark_unit_price']) * 100

# 2. Flag under-valued shipments (e.g., unit price > 30% below benchmark)
df['is_undervalued'] = np.where(df['valuation_gap_pct'] < -30, 1, 0)

# 3. Select validation columns
validation_cols = [
    'entry_id', 'importer_id', 'hs_code', 'declared_value_php',
    'quantity', 'declared_unit_price', 'benchmark_unit_price',
    'valuation_gap_pct', 'is_undervalued'
]

validation_df = df[validation_cols]

# 4. Save to outputs folder with safe quoting options
validation_df.to_csv(
    'outputs/validation.csv',
    index=False,
    quoting=csv.QUOTE_MINIMAL,
    encoding='utf-8'
)

print("Case 2 validation.csv successfully generated in outputs/ folder.")