import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class DataProcessor:

    def __init__(self, df: pd.DataFrame, config):
        self.df = df
        self.config = config

    def create_derived_columns(self):
        """Creates derived scaled numeric metrics if the numeric column exists."""
        if self.config.NUM_COL in self.df.columns:
            self.df[self.config.NUM_COL] = pd.to_numeric(
                self.df[self.config.NUM_COL], errors="coerce"
            ).fillna(0)
            self.df["dutiable_value_k"] = self.df[self.config.NUM_COL] / 1000.0

    def generate_pivot_csv(
        self,
        cat1: str = None,
        cat2: str = None,
        measure: str = None,
        output_dir: str = None,
    ) -> pd.DataFrame:
        """Generates pivot.csv showing measure sum across two categories with totals (margins)."""
        cat1 = cat1 or self.config.CAT_COL_1
        cat2 = cat2 or self.config.CAT_COL_2
        measure = measure or self.config.NUM_COL
        output_dir = output_dir or self.config.OUTPUT_DIR

        pivot_df = pd.pivot_table(
            self.df,
            values=measure,
            index=cat1,
            columns=cat2,
            aggfunc="sum",
            margins=True,
            margins_name="Total",
            dropna=False,
        )
        os.makedirs(output_dir, exist_ok=True)
        pivot_df.to_csv(os.path.join(output_dir, "pivot.csv"))
        return pivot_df

    def generate_top10_csv(
        self,
        grouped_df: pd.DataFrame = None,
        measure_sum_col: str = None,
        output_dir: str = None,
    ) -> pd.DataFrame:
        """Sorts the grouped summary by measure sum and exports top10.csv."""
        measure_sum_col = measure_sum_col or self.config.NUM_COL
        output_dir = output_dir or self.config.OUTPUT_DIR

        if grouped_df is None:
            grouped_df = (
                self.df.groupby(self.config.CAT_COL_1)[measure_sum_col]
                .sum()
                .reset_index()
            )

        top10_df = grouped_df.sort_values(
            by=measure_sum_col, ascending=False
        ).head(10)

        os.makedirs(output_dir, exist_ok=True)
        top10_df.to_csv(os.path.join(output_dir, "top10.csv"), index=True)
        return top10_df

    def generate_summary_tables(self, export_csv: bool = True):
        """Generates summary table dictionary expected by main.py, integrating sorted Top 10 and Pivot with margins."""
        if self.df.empty:
            print(
                "[NOTICE] Filtered dataset is empty. Returning empty DataFrames."
            )
            empty_df = pd.DataFrame()
            return {
                "grouped": empty_df,
                "grouped_two": empty_df,
                "pivot": empty_df,
                "top10": empty_df,
            }

        # Table 1: Grouped by CAT_COL_1
        grouped = (
            self.df.groupby(self.config.CAT_COL_1)[self.config.NUM_COL]
            .sum()
            .reset_index()
        )

        # Table 2: Grouped by CAT_COL_2
        grouped_two = (
            self.df.groupby(self.config.CAT_COL_2)[self.config.NUM_COL]
            .sum()
            .reset_index()
        )

        # Table 3 & 4: Pivot Table and Sorted Top 10
        if export_csv:
            pivot = self.generate_pivot_csv()
            top10 = self.generate_top10_csv(grouped_df=grouped)
        else:
            pivot = pd.pivot_table(
                self.df,
                values=self.config.NUM_COL,
                index=self.config.CAT_COL_1,
                columns=self.config.CAT_COL_2,
                aggfunc="sum",
                margins=True,
                margins_name="Total",
                dropna=False,
            )
            top10 = grouped.sort_values(
                by=self.config.NUM_COL, ascending=False
            ).head(10)

        return {
            "grouped": grouped,
            "grouped_two": grouped_two,
            "pivot": pivot,
            "top10": top10,
        }

    def export_plots(self, *args, **kwargs):
        """Exports heatmap plots safely without crashing on empty data arrays."""
        if self.df.empty:
            print(
                "[NOTICE] Skipping heatmap generation: Filtered dataset contains 0 rows."
            )
            return

        pivot_clean = self.df.pivot_table(
            index=self.config.CAT_COL_1,
            columns=self.config.CAT_COL_2,
            values=self.config.NUM_COL,
            aggfunc="sum",
            fill_value=0,
        ).dropna()

        if pivot_clean.empty or (pivot_clean.values == 0).all():
            print(
                "[NOTICE] Pivot table has no non-zero numeric data to plot."
            )
            return

        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_clean, annot=True, fmt=".0f", cmap="Blues")
        plt.title("Customs Valuation Summary Heatmap")

        os.makedirs(self.config.OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(
            self.config.OUTPUT_DIR, "summary_heatmap.png"
        )
        plt.savefig(output_path, bbox_inches="tight")
        plt.close()
        print(f"Heatmap successfully exported to: {output_path}")