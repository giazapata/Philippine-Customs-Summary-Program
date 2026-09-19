# Project Contributions & Git Audit Trail

**Dataset Used:** Philippine Customs 2015 (`2015.csv`)


## Contributions

### **Patricia Ann Mae Pascual** — Data Prep & NumPy
* **Assigned Features:** NumPy arrays, boolean masking, vectorized calculations.
* **Core Functions & Modules:**
  * `src/prep.py` -> `apply_loc_filter(df)`: Filters rows using `.loc` and adds two new columns.
  * `src/prep.py` -> `compute_numpy_benchmarks(array_data)`: Runs vectorized calculations and compares speed against standard loops.
* **Deliverables:** Filtered dataset and baseline total sum for validation checks.

### **Patrick Raphael Lista** — Grouped Summaries
* **Assigned Features:** Classes, methods, and project directory structure (`src/`).
* **Core Functions & Modules:**
  * `src/summaries.py` -> `GroupedSummaryGenerator`: Class that sets up table grouping logic.
  * `src/summaries.py` -> `generate_primary_summary()` & `generate_two_factor_summary()`: Runs grouped summary tables and keeps empty categories using `dropna=False`.
* **Deliverables:** `grouped.csv` and `grouped_two.csv`.

### **Maureen Joi Cruz** — Aggregation & Data Flow
* **Assigned Features:** Loops, conditional statements, dictionaries.
* **Core Functions & Modules:**
  * `src/pivot_builder.py` -> `build_pivot_table(df)`: Builds pivot tables and extracts top 10 rows.
  * `main.py` -> `record_audit_step()`: Logs row counts and operations as the script runs.
* **Deliverables:** `pivot.csv`, `top10.csv`, and `audit_log.csv`.

### **Audrey Paulynne Olaybar** — Data Visualization
* **Assigned Features:** Reusable functions with default parameters.
* **Core Functions & Modules:**
  * `src/visualizer.py` -> `plot_bar_chart(df)`: Saves a bar chart with axis labels and units.
  * `src/visualizer.py` -> `plot_heatmap(df)`: Saves a heatmap excluding row and column totals.
* **Deliverables:** `bar.png` and `heatmap.png`.

### **Gianela Zapata** — QA & Documentation
* **Assigned Features:** Type hinting, docstrings, code cleanup.
* **Core Functions & Modules:**
  * `src/validator.py` -> `DataValidator`: Checks if raw and grouped sums match, saves results, and stops the program if checks fail.
  * `main.py` & `src/`: Added type hints and docstrings across all Python files.
* **Deliverables:** `validation.csv` and `README.md`.
