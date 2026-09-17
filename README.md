# 2015 Philippine Customs Data Analysis Pipeline

A modular Python-based pipeline designed to load, validate, clean, analyze, and visualize the 2015 Philippine Customs dataset.

## Project Structure
Philippine-Customs-Summary-Program-1/
│
├── config.py             # Global configurations, file paths, filter parameters
├── main.py               # Core orchestrator script executing the pipeline
├── README.md             # Project documentation
├── data/
│   └── 2015.csv          # Raw 2015 Philippine Customs dataset
├── outputs/              # Generated output tables, audit logs, and heatmaps
└── src/
├── init.py
├── data_loader.py    # File I/O, column validation, encoding handling, filtering
└── processor.py     # Metric transformations, summary table generation, plotting

## Features

- **Robust File Validation**: Pre-validates schema and column requirements before running heavy computations.
- **Encoding Error Bypass**: Utilizes `latin1` decoding to smoothly handle non-standard text characters in customs descriptions.
- **Data Filtering & Aggregation**: Dynamically filters dataset entries based on entry periods and currency types configured in `config.py`.
- **Automated Summary Tables**: Outputs grouped summary metrics and pivot tables directly to the `outputs/` folder as `.csv` files.
- **Data Visualization**: Generates Seaborn heatmaps summarizing customs valuation distributions while handling empty or zero-value filter results gracefully without crashing.

## Prerequisites & Installation

Ensure you have Python 3.10+ installed along with the required libraries:

```bash
pip install pandas matplotlib seaborn

## How to Run
Configure Parameters: Open config.py and set your desired category filters (CAT_COL_1, FILTER_CAT_1, CAT_COL_2, FILTER_CAT_2).

Execute Pipeline: Run main.py from the project root directory:
python main.py

View Results: Check the generated outputs inside the outputs/ directory:
audit_log.csv: Log tracking raw vs. filtered row counts.
grouped.csv & grouped_two.csv: Category-wise numerical metric summaries.
summary_heatmap.png: Exported Seaborn heatmaps.