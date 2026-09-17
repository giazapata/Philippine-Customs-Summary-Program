import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any

class DataProcessor:
    """Class to process, aggregate, and visualize Philippine Customs data."""
    
    def __init__(self, df: pd.DataFrame, config: Any) -> None:
        self.df = df.copy()
        self.config = config

    def create_derived_columns(self) -> None:
        """Create one numerical and one categorical/flag derived column."""
        self.df["dutiable_value_k"] = self.df[self.config.NUM_COL] / 1000.0
        median_val = self.df[self.config.NUM_COL].median()
        self.df["value_flag"] = np.where(self.df[self.config.NUM_COL] > median_val, "HIGH", "LOW")

    def generate_summary_tables(self) -> Dict[str, pd.DataFrame]:
        """Generate summary tables."""
        cat1 = self.config.CAT_COL_1
        cat2 = self.config.CAT_COL_2
        num_col = self.config.NUM_COL

        grouped = self.df.groupby(cat1, dropna=False).agg(
            row_count=(num_col, "size"),
            valid_measure_count=(num_col, "count"),
            sum=(num_col, "sum"),
            mean=(num_col, "mean")
        ).reset_index()

        grouped_two = self.df.groupby([cat1, cat2], dropna=False).agg(
            row_count=(num_col, "size"),
            measure_sum=(num_col, "sum")
        ).reset_index()

        pivot = pd.pivot_table(
            self.df,
            values=num_col,
            index=cat1,
            columns=cat2,
            aggfunc="sum",
            margins=True,
            dropna=False
        )

        top10 = grouped.sort_values(by="sum", ascending=False).head(10)

        return {
            "grouped": grouped,
            "grouped_two": grouped_two,
            "pivot": pivot,
            "top10": top10
        }

    def export_plots(self, top10_df: pd.DataFrame, pivot_df: pd.DataFrame) -> None:
        """Generate and save bar chart and heatmap."""
        out_dir = self.config.OUTPUT_DIR
        cat1 = self.config.CAT_COL_1
        
        plt.figure(figsize=(10, 6))
        plt.bar(top10_df[cat1].astype(str), top10_df["sum"])
        plt.title("Top 10 Categories by Dutiable Value Sum (PHP)")
        plt.xlabel(cat1)
        plt.ylabel("Total Dutiable Value (PHP)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "bar.png"))
        plt.close()

        pivot_no_margins = pivot_df.drop(index="All", columns="All", errors="ignore")
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_no_margins, annot=True, fmt=".0f", cmap="Blues")
        plt.title("Dutiable Value Sum Across Categories")
        plt.xlabel(self.config.CAT_COL_2)
        plt.ylabel(cat1)
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "heatmap.png"))
        plt.close()