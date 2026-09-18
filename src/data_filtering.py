import os
import sys
import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import DATA_PATH, REQUIRED_COLUMNS


def inspect_dataset(
    df: pd.DataFrame,
    required_columns: set[str]
) -> dict:
    """Inspect dataset size, data types, and missing values."""

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    inspection = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "data_types": (
            df[list(required_columns)]
            .dtypes
            .astype(str)
            .to_dict()
        ),
        "missing_values": (
            df[list(required_columns)]
            .isna()
            .sum()
            .to_dict()
        )
    }

    return inspection


def load_and_filter_csv(
    file_path: str,
    filter_quarters: list[str],
    value_quantile: float = 0.50
) -> tuple[pd.DataFrame, pd.DataFrame, float]:
    """Load the dataset and filter Q1/Q2 values above the median."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    df_raw = pd.read_csv(
        file_path,
        low_memory=False,
        encoding="latin1"
    )

    df_raw.columns = df_raw.columns.str.strip()

    median_value = (
        df_raw["dutiablevaluephp"]
        .quantile(value_quantile)
    )

    # Dual-condition filter using .loc
    condition = (
        df_raw["tq"].isin(filter_quarters)
        &
        (
            df_raw["dutiablevaluephp"] > median_value
        )
    )

    df_filtered = df_raw.loc[condition].copy()

    if df_filtered.empty:
        raise ValueError(
            "The filter returned no rows. "
            "Check the selected quarters and median threshold."
        )

    return (
        df_raw,
        df_filtered,
        float(median_value)
    )


def create_derived_columns(
    df: pd.DataFrame,
    value_flag_threshold: float = 1_000_000
) -> pd.DataFrame:
    """Create one numerical and one categorical derived column."""

    df = df.copy()

    # Numerical derived column
    df["dutiable_value_k"] = (
        df["dutiablevaluephp"] / 1_000
    )

    # Categorical derived column
    df["value_flag"] = np.where(
        df["dutiablevaluephp"] >= value_flag_threshold,
        "HIGH",
        "LOW"
    )

    return df


if __name__ == "__main__":

    FILTER_QUARTERS = [
        "2015q1",
        "2015q2"
    ]

    # Load and filter
    df_raw, df_filtered, median_value = load_and_filter_csv(
        DATA_PATH,
        FILTER_QUARTERS
    )

    # Inspect dataset
    inspection = inspect_dataset(
        df_raw,
        set(REQUIRED_COLUMNS)
    )

    # Create derived columns
    df_filtered = create_derived_columns(
        df_filtered
    )

    print("\nDataset Inspection")
    print("------------------")
    print("Rows:", inspection["row_count"])
    print("Columns:", inspection["column_count"])

    print("\nData Types:")
    for column, data_type in inspection["data_types"].items():
        print(f"{column}: {data_type}")

    print("\nMissing Values:")
    for column, missing_count in inspection["missing_values"].items():
        print(f"{column}: {missing_count}")

    print("\nFiltering Results")
    print("-----------------")
    print("Selected quarters:", FILTER_QUARTERS)
    print(f"Median dutiable value: PHP {median_value:,.2f}")
    print("Rows before filtering:", len(df_raw))
    print("Rows after filtering:", len(df_filtered))

    print("\nFiltered Data with Derived Columns")
    print("----------------------------------")

    print(
        df_filtered[
            [
                "countryorigin_iso3",
                "tq",
                "dutiablevaluephp",
                "dutiable_value_k",
                "value_flag"
            ]
        ].head(10)
    )