import os

DATA_PATH = "2015.csv"
OUTPUT_DIR = "outputs"

REQUIRED_COLUMNS = {"countryorigin_iso3", "tq", "dutiablevaluephp"}

CAT_COL_1 = "countryorigin_iso3"
CAT_COL_2 = "tq"
NUM_COL = "dutiablevaluephp"

FILTER_CAT_1 = "CHN"
FILTER_CAT_2 = "KG"

REF_ROWS = 2236612
REF_DUTIABLE_TOTAL = 3587267375257.0