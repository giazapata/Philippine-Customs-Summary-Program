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