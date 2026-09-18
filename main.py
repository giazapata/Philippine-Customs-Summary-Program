import os
import pandas as pd
import csv
import numpy as np
import config
from src.data_loader import check_file_and_columns, load_and_filter_csv
from src.processor import DataProcessor


def main() -> None:
    print("--- Starting Customs Data Pipeline ---")

    # Ensure output directory exists
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)

    # Step 1: Input Validation
    check_file_and_columns(config.DATA_PATH, config.REQUIRED_COLUMNS)

    # Step 2: Data Loading & Filtering (with initial audit log generation)
    df_raw, df_filtered, audit_records = load_and_filter_csv(
        config.DATA_PATH,
        config.CAT_COL_1,
        config.FILTER_CAT_1,
        config.CAT_COL_2,
        config.FILTER_CAT_2,
    )

    # Zero-row safeguard check
    if df_filtered.empty:
        raise ValueError("[ERROR] Filter criteria returned 0 rows. Aborting execution.")

    # Step 3: Process Data with DataProcessor
    processor = DataProcessor(df_filtered, config)
    processor.create_derived_columns()

    # Step 4: Generate Summary Tables
    tables = processor.generate_summary_tables(export_csv=True)

    # Export Grouped Datasets to CSV
    tables["grouped"].to_csv(
        os.path.join(config.OUTPUT_DIR, "grouped.csv"), index=False
    )
    tables["grouped_two"].to_csv(
        os.path.join(config.OUTPUT_DIR, "grouped_two.csv"), index=False
    )

    # Step 5: Format Audit Log & Append Data Processing Step
    audit_log = [audit_records] if isinstance(audit_records, dict) else list(audit_records)

    audit_log.append(
        {
            "step": 3,
            "operation": "Data Summarization",
            "rule": "Generated pivot, top 10, and grouped metrics",
            "rows_before": len(df_filtered),
            "rows_after": len(tables["top10"]),
        }
    )

    pd.DataFrame(audit_log).to_csv(
        os.path.join(config.OUTPUT_DIR, "audit_log.csv"), index=False
    )

    # Step 6: Export Visualizations
    processor.export_plots(tables["top10"], tables["pivot"])

    # Step 7: Export Validation CSV
    # Note: Using df_filtered or derivation from processor outputs
    df_filtered.to_csv(
        os.path.join(config.OUTPUT_DIR, "validation.csv"),
        index=False,
        quoting=csv.QUOTE_MINIMAL,
        encoding="utf-8"
    )

    print("--- Pipeline execution complete! Check outputs/ folder. ---")


if __name__ == "__main__":
    main()