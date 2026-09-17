# config.py

DATA_PATH = "data/2015.csv"
OUTPUT_DIR = "outputs"
NUM_COL = "dutiablevaluephp"

REQUIRED_COLUMNS = [
    "entry",
    "currency",
    "dutiablevaluephp",
    "fob_n_cif",
    "goodsdescription"
]

# Match exact column types in 2015.csv
CAT_COL_1 = "entry"
FILTER_CAT_1 = 201501  # Integer matching line 2 of 2015.csv

CAT_COL_2 = "currency"
FILTER_CAT_2 = "USD"