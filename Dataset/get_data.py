
from fredapi import Fred
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import file_io

env_path = Path(os.getcwd()) / "api.env"
load_dotenv(dotenv_path=env_path)


# Define the series codes
series_codes = {
    'GS10': '10-Year Yield',
    'DGS2': '2-Year Yield',
    'DGS3MO': '3-Month Yield'#,
    #'UNRATE': 'UnemploymentRate'
}


# Now read it:
# get api key from fred and save in api.env
FRED_API_KEY = os.getenv("MY_API_KEY")

if not FRED_API_KEY:
    sys.exit("Error: MY_API_KEY not found in environment or .env file.")

fred = Fred(api_key=FRED_API_KEY)


# Fetch data and store in a dictionary
data = {}
for code, name1 in series_codes.items():
    try:
        data[code] = fred.get_series(code)
    except Exception as e:
        print(f"Error fetching {name1}: {e}")

# Combine all into a single DataFrame
df = pd.DataFrame(data)

#Export to CSV
file_io.output_csv(dataframe=df, flag = True, file_name = 'data_raw')