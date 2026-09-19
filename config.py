import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Check if data/2015.csv exists in the current folder, otherwise look in the parent folder
local_data_path = os.path.join(BASE_DIR, "data", "2015.csv")
parent_data_path = os.path.join(os.path.dirname(BASE_DIR), "data", "2015.csv")

if os.path.exists(local_data_path):
    DATA_PATH = local_data_path
elif os.path.exists(parent_data_path):
    DATA_PATH = parent_data_path
else:
    # Fallback default
    DATA_PATH = local_data_path

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

NUM_COL = "dutiablevaluephp"

REQUIRED_COLUMNS = [
    "entry",
    "tm",
    "currency",
    "dutiablevaluephp",
    "m_fob",
    "m_cif",
    "goodsdescription",
]

CAT_COL_1 = "tm"
FILTER_CAT_1 = "2015m1"

CAT_COL_2 = "currency"
FILTER_CAT_2 = "USD"