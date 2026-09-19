

**Dataset Used:** Philippine Customs 2015 (`2015.csv`)


## Contributions

### **Patricia Ann Mae Pascual** — Data Prep & NumPy
* **Assigned Features:** NumPy arrays, boolean masking, vectorized calculations.
* **Core Functions & Modules:**
  * `src/prep.py` -> `apply_loc_filter(df)`: Filters rows using `.loc` and adds two new columns.
  * `src/prep.py` -> `compute_numpy_benchmarks(array_data)`: Runs vectorized calculations and compares speed against standard loops.
* **Deliverables:** Filtered dataset and baseline total sum for validation checks.

### Commits
* ‘80e9937086f1d1d1a11b1a290dfbf6e9213d050a’ - Add data filtering module

### **Patrick Raphael Lista** — Grouped Summaries
* **Assigned Features:** Classes, methods, and project directory structure (`src/`).
* **Core Functions & Modules:**
  * `src/summaries.py` -> `GroupedSummaryGenerator`: Class that sets up table grouping logic.
  * `src/summaries.py` -> `generate_primary_summary()` & `generate_two_factor_summary()`: Runs grouped summary tables and keeps empty categories using `dropna=False`.
* **Deliverables:** `grouped.csv` and `grouped_two.csv`.

### Commits
* ‘0ec114dc8c1d184359e8053b0ad332c281ed2ef2’ - feat: add DataSummarizer class
* ‘6889854043214b78a4cf3157623db49102035584’ - Merge branch 'main' of https://github.com/giazapata/Philippine-Customs-Summary-Program into feature/classes-patrick

### **Maureen Joi Cruz** — Aggregation & Data Flow
* **Assigned Features:** Loops, conditional statements, dictionaries.
* **Core Functions & Modules:**
  * `src/pivot_builder.py` -> `build_pivot_table(df)`: Builds pivot tables and extracts top 10 rows.
  * `main.py` -> `record_audit_step()`: Logs row counts and operations as the script runs.
* **Deliverables:** `pivot.csv`, `top10.csv`, and `audit_log.csv`.

### Commits
* ‘5e0cefce374bd84e95a5ae51487d15dbdccd707e’ - refactor(processor): integrate pivot and top10 CSV generation into DataProcessor
* ‘97cdc1ffad6d32c2989213e8359cfe0b8190aefa’ - refactor: update pipeline to use unified DataProcessor methods and audit logging
* ‘E422ede13baa6a922c1b8c3e47cdeee15bbee92e’ - Remove stray processor file without extention

### **Audrey Paulynne Olaybar** — Data Visualization
* **Assigned Features:** Reusable functions with default parameters.
* **Core Functions & Modules:**
  * `src/visualizer.py` -> `plot_bar_chart(df)`: Saves a bar chart with axis labels and units.
  * `src/visualizer.py` -> `plot_heatmap(df)`: Saves a heatmap excluding row and column totals.
* **Deliverables:** `bar.png` and `heatmap.png`.
* **Final Editing** edited main.py, config.py, requirements.txt, analysis.ipynb, and analysis.html
  
### Commits
* ‘0dbff8cb3a7703473976525c2e9a368b78624c67’ - Added Visualizations.py
* ‘dd1e21a17ae5740b55b0ce67e05b2ad2e2c48fcd‘ - Add contributions section with Member 1
* ‘A83a26faa4afcc78209448081017874ee36a3272’ - Revise contributions documentation with member details 
* ‘055f74a0e0629e1f2a945d2af9cbdbf5da7d535d’ - Update contributions.md header format
* ‘30e5a7c97be13e3591d32ac74c22e97afdd5f3dd’ - final editing
* ‘Cf69e9d6bcc88f90d78fca9ea328969d02d59529‘ - Update contributions with final editing details


### **Gianela Zapata** — QA & Documentation
* **Assigned Features:** Type hinting, docstrings, code cleanup.
* **Core Functions & Modules:**
  * `src/validator.py` -> `DataValidator`: Checks if raw and grouped sums match, saves results, and stops the program if checks fail.
  * `main.py` & `src/`: Added type hints and docstrings across all Python files.
* **Deliverables:** `validation.csv` and `README.md`.

### Commits
* ‘0c68c5eb06593bf768878b71b9d1329b9ca2d852’ - fix: place imports at the top
* ‘3a4d41aa157576d4e75eab9413bfa84ece033938’ - fix: place imports at the top
* ‘7386282ad29cf67da7389fbed9947c4c4e6c905c’ - fix: validation.csv
* ‘2d656f6355d84af6a09c712d70f1c354f67db2df’ - Merge branch 'main' of https://github.com/giazapata/Philippine-Customs-Summary-Program
* ‘4b60f883fa449d15b14fd58164e73e6a7e5f1db6’ - feat: create validation.csv
* ‘53119fdaa11573d2095a400fdff85225621019af’ - Merge pull request #5 from giazapata/feature/classes-patrick
* ‘D578f44b037b949b0592609ecd464ac1ea2a4ce2’ - Merge pull request #2 from giazapata/feature/data_filtering-patricia
* ‘3240ed44dd8bf90c27c1626d08c9442cf88a2848’ - Merge pull request #3 from giazapata/feature/visualization-audrey
* ‘3b0dcfcf30906accff7bbb3d639184ec4f47d60c’ - Merge pull request #1 from giazapata/feature/pivot-audit-maureen
* ‘A4fccac95917673ef4ed2988182e77e1f3222a46’ - fix: updating data_loader and config.py to solve zero rows issue
* ‘B898d84b9aaf1a71e2d77e3e628155ad587b5e3a’ - fix: updating data_loader so it automatically strips formatting and safely converts numeric/string representations
* ‘E07586f03c233cb86243fb3e20b9fd42c1df3267’ - fix: resolve zero-row filtering by matching config criteria with raw dataset values
* ‘082ad2102ddbfc5927b6ec941c0863d09eb0ac5f’ - init: fix errors, set up project structure, config, and data processing pipeline
* ‘C5b5338a22851422cd8a23f708e42a2e9b2e7dae’ - init: set up project structure, config, and data processing pipeline
* ‘1ced4f8d379369fd5fb0a85190ed83b50d32947e’ - init: set up project structure, config, and data processing pipeline
* ‘2542189073b5e64764e8a7d0b56f6d46eecda0fb’ - Update analysis.ipynb
* ‘6acbbe6b09c1a7dcf5021ba5bb12a0a99f4f843c’ - Add files via upload
* ‘Dd1e21a17ae5740b55b0ce67e05b2ad2e2c48fcd’ - Add contributions section with Member 1
* ‘A83a26faa4afcc78209448081017874ee36a3272’ - Revise contributions documentation with member details
* ‘055f74a0e0629e1f2a945d2af9cbdbf5da7d535d’ - Update contributions.md header format
* ‘0f2d4601b3284ade8a3b961a2904389da16e4fd4’ - Merge branch 'main' of https://github.com/giazapata/Philippine-Customs-Summary-Program
* ‘Fa482647ff56c165f7ced5eb63a98f79bb79959e’ - fix: place imports at the top
* ‘A785f5c5a68d47a42357c4b3230748f7b8263958’ - Upload the CSV file using single direct download and Git LFS
* ‘641c23edbb520c08b0d4915e0c24c2e71af399c3’ - docs: update README with project overview, setup, and usage instructions
* ‘A801ada4ab86d96a88111d3205a8eff5ba6921c9’ - fix: update config.py
