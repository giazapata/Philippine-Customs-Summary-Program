import importlib
import os

plt = importlib.import_module("matplotlib.pyplot")
pd = importlib.import_module("pandas")
sns = importlib.import_module("seaborn")

# Ensure outputs directory exists
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================================
# 1. STANDALONE PLOTTING FUNCTIONS
# =====================================================================


def create_bar_chart(
    data,
    x_col,
    y_col,
    title="Bar Chart",
    x_label=None,
    y_label=None,
    unit_annotation="USD",
    output_filename="bar.png",
):
    """Generates a bar plot, formats annotations with units, and saves to outputs/."""
    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=data, x=x_col, y=y_col, hue=x_col, palette="Blues_d", legend=False
    )

    ax.ticklabel_format(style="plain", axis="y")
    plt.ylim(0, data[y_col].max() * 1.18)

    plt.title(title, fontsize=14, pad=15)
    plt.xlabel(x_label if x_label else x_col, fontsize=12)
    plt.ylabel(
        f"{y_label if y_label else y_col} ({unit_annotation})", fontsize=12
    )

    for p in ax.patches:
        height = p.get_height()
        if not pd.isna(height) and height > 0:
            ax.annotate(
                f"{height:,.0f} {unit_annotation}",
                (p.get_x() + p.get_width() / 2.0, height),
                ha="center",
                va="bottom",
                xytext=(0, 5),
                textcoords="offset points",
                fontsize=8,
            )

    plt.xticks(rotation=45)
    plt.tight_layout()

    save_path = os.path.join(OUTPUT_DIR, output_filename)
    plt.savefig(save_path, dpi=300)
    plt.close()

    print(f"Bar chart successfully saved to: {save_path}")
    return save_path


def create_heatmap(
    data_matrix,
    title="Correlation Heatmap",
    x_label="Variables",
    y_label="Variables",
    unit_annotation="Correlation (r)",
    cmap="YlGnBu",
    output_filename="heatmap.png",
):
    """Generates a clean, spacious heatmap and saves to outputs/."""
    plt.figure(figsize=(8, 6))

    ax = sns.heatmap(
        data_matrix,
        annot=True,
        fmt=".2f",
        cmap=cmap,
        cbar=True,
        linewidths=1.5,
        linecolor="white",
        square=True,
        annot_kws={"size": 10, "weight": "bold"},
    )

    plt.title(title, fontsize=14, pad=15)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)

    cbar = ax.collections[0].colorbar
    cbar.set_label(unit_annotation, fontsize=10)

    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(rotation=0, fontsize=10)
    plt.tight_layout()

    save_path = os.path.join(OUTPUT_DIR, output_filename)
    plt.savefig(save_path, dpi=300)
    plt.close()

    print(f"Heatmap successfully saved to: {save_path}")
    return save_path


# =====================================================================
# 2. DATA PROCESSING & EXECUTION
# =====================================================================

if __name__ == "__main__":
    # Updated CSV path to look inside the data/ folder
    df = pd.read_csv(
        "data/2015.csv", encoding="latin1", on_bad_lines="skip", engine="python"
    )
    df.columns = df.columns.str.strip().str.lower()

    # --- Plot 1: Bar Chart ---
    top_goods = (
        df.groupby("goodsdescription")["m_fob"].sum().nlargest(5).reset_index()
    )

    bar_path = create_bar_chart(
        data=top_goods,
        x_col="goodsdescription",
        y_col="m_fob",
        title="Top 5 Goods by FOB Value",
        x_label="Goods Description",
        y_label="FOB Value",
        unit_annotation="USD",
        output_filename="bar.png",
    )

    # --- Plot 2: Heatmap ---
    selected_metrics = [
        "m_fob",
        "m_cif",
        "fx_usd",
        "dutiablevalueforeign",
        "dutiestaxes",
    ]

    valid_cols = [c for c in selected_metrics if c in df.columns]
    heatmap_matrix = df[valid_cols].apply(pd.to_numeric, errors="coerce").corr()

    heatmap_path = create_heatmap(
        data_matrix=heatmap_matrix,
        title="Trade Metric Correlations",
        x_label="Trade Metrics",
        y_label="Trade Metrics",
        unit_annotation="Correlation Coefficient (r)",
        output_filename="heatmap.png",
    )
    print("FINISHED_SUCCESSFULLY")