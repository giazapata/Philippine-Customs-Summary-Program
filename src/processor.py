import os
import matplotlib.pyplot as plt
import seaborn as sns

class DataProcessor:
    def __init__(self, df, config):
        self.df = df
        self.config = config

    def create_derived_columns(self):
        """Creates derived scaled numeric metrics if the numeric column exists."""
        if self.config.NUM_COL in self.df.columns:
            # Convert column to numeric in case values are strings
            self.df[self.config.NUM_COL] = pd.to_numeric(self.df[self.config.NUM_COL], errors="coerce").fillna(0)
            self.df["dutiable_value_k"] = self.df[self.config.NUM_COL] / 1000.0

    def generate_summary_tables(self):
        """Generates all summary table keys expected by main.py."""
        if self.df.empty:
            print("[NOTICE] Filtered dataset is empty. Returning empty DataFrames.")
            return {"grouped": self.df, "grouped_two": self.df, "pivot": self.df, "top10": self.df}

        # Table 1: Grouped by CAT_COL_1
        grouped = self.df.groupby(self.config.CAT_COL_1)[self.config.NUM_COL].sum().reset_index()

        # Table 2: Grouped by CAT_COL_2
        grouped_two = self.df.groupby(self.config.CAT_COL_2)[self.config.NUM_COL].sum().reset_index()

        # Table 3: Pivot Table across both categories
        pivot = self.df.pivot_table(
            index=self.config.CAT_COL_1,
            columns=self.config.CAT_COL_2,
            values=self.config.NUM_COL,
            aggfunc="sum",
            fill_value=0
        )

        top10 = self.df.head(10)

        return {
            "grouped": grouped,
            "grouped_two": grouped_two,
            "pivot": pivot,
            "top10": top10
        }

    def export_plots(self, *args, **kwargs):
        """Exports heatmap plots safely without crashing on empty data arrays."""
        if self.df.empty:
            print("[NOTICE] Skipping heatmap generation: Filtered dataset contains 0 rows.")
            return

        pivot_clean = self.df.pivot_table(
            index=self.config.CAT_COL_1,
            columns=self.config.CAT_COL_2,
            values=self.config.NUM_COL,
            aggfunc="sum",
            fill_value=0
        ).dropna()

        if pivot_clean.empty or (pivot_clean.values == 0).all():
            print("[NOTICE] Pivot table has no non-zero numeric data to plot.")
            return

        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_clean, annot=True, fmt=".0f", cmap="Blues")
        plt.title("Customs Valuation Summary Heatmap")
        
        output_path = os.path.join(self.config.OUTPUT_DIR, "summary_heatmap.png")
        plt.savefig(output_path, bbox_inches="tight")
        plt.close()
        print(f"Heatmap successfully exported to: {output_path}")