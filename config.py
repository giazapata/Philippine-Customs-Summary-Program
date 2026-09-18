# config.py

DATA_PATH = "data/2015.csv"
OUTPUT_DIR = "outputs"
NUM_COL = "dutiablevaluephp"

REQUIRED_COLUMNS = [
    "entry",
    "tm",
    "currency",
    "dutiablevaluephp",
    "m_fob",
    "m_cif",
    "goodsdescription"
]

# Set CAT_COL_1 to 'tm' so '2015m1' matches the month column directly
CAT_COL_1 = "tm"
FILTER_CAT_1 = "2015m1"

CAT_COL_2 = "currency"
FILTER_CAT_2 = "USD"