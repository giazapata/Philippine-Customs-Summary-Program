import os
import pandas as pd


class DataSummarizer:
    """Class to generate grouped summary tables from filtered dataset records."""

    def __init__(self, df: pd.DataFrame):
        """Initialize with the filtered DataFrame as an instance attribute."""
        self.df = df
        self.grouped_one_df: pd.DataFrame | None = None
        self.grouped_two_df: pd.DataFrame | None = None

    def generate_grouped_summary(
        self, cat_col: str, measure_col: str
    ) -> pd.DataFrame:
        """Group by first category; show row count, valid measure count, sum, and mean."""
        self.grouped_one_df = (
            self.df.groupby(cat_col, dropna=False)
            .agg(
                row_count=(cat_col, "size"),
                valid_measure_count=(measure_col, "count"),
                measure_sum=(measure_col, "sum"),
                measure_mean=(measure_col, "mean"),
            )
            .reset_index()
        )
        return self.grouped_one_df

    def generate_grouped_two_summary(
        self, cat1: str, cat2: str, measure_col: str
    ) -> pd.DataFrame:
        """Group by both categories; show row count and measure sum using named aggregations."""
        self.grouped_two_df = (
            self.df.groupby([cat1, cat2], dropna=False)
            .agg(
                row_count=(cat1, "size"),
                measure_sum=(measure_col, "sum"),
            )
            .reset_index()
        )
        return self.grouped_two_df

    def export_summaries(self, output_dir: str = "outputs") -> None:
        """Save the generated summary tables to CSV files in the specified directory."""
        os.makedirs(output_dir, exist_ok=True)

        if self.grouped_one_df is not None:
            self.grouped_one_df.to_csv(
                os.path.join(output_dir, "grouped.csv"), index=False
            )

        if self.grouped_two_df is not None:
            self.grouped_two_df.to_csv(
                os.path.join(output_dir, "grouped_two.csv"), index=False
            )