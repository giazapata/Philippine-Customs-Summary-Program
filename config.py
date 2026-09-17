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
# Set to match exact CSV values (2015m1, not 2015m01)
CAT_COL_1 = "entry"
FILTER_CAT_1 = "2015m1"

CAT_COL_2 = "currency"
FILTER_CAT_2 = "USD"