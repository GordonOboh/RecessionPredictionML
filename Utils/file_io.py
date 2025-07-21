import os
import pandas as pd
from fredapi import Fred
import sys

def output_csv(dataframe, file_name, flag = False, report = True, include_index = True):
    if flag:
        # Check if folder exists, if not, create it
        if not os.path.exists('Dataset'):
            os.makedirs('Dataset')

        # Save DataFrame as CSV inside the folder
        csv_path = os.path.join('Dataset', f'{file_name}.csv')
        dataframe.to_csv(csv_path, index=include_index)
        if report:
            print(f"DataFrame saved to {csv_path}")

def input_csv(file_name, report=True):
    csv_path = os.path.join('Dataset', f'{file_name}.csv')
    
    if not os.path.exists(csv_path):
        if report:
            print(f"File {csv_path} not found.")
        return None
    
    df = pd.read_csv(csv_path, index_col = 0, parse_dates=True)
    if report:
        print(f"DataFrame loaded from {csv_path}")
    return df

def output_png(fig, file_name = None, flag = False, report = True):
    if file_name == None:
        try:
            file_name = fig.get_title()
        except AttributeError:
            try:
                file_name = fig.gca().get_title()
            except Exception:
                # Final fallback: use a default name
                file_name = "plot"

    file_name = file_name.replace(":", "").replace("/", "_").strip()

    if flag:
        # Check if folder exists, if not, create it
        if not os.path.exists('plot'):
            os.makedirs('plot')

        # Save Figure as png inside the folder
        png_path = os.path.join('plot', f'{file_name}.png')
        #png_path = png_path.replace(":", "")
        fig.savefig(png_path, bbox_inches='tight')
        if report:
            print(f"Plot saved to {png_path}")


def get_fred_data(series_codes: dict, FRED_API_KEY: str, output_csv_flag=True, filename='data_raw'):
    #FRED_API_KEY = os.getenv("MY_API_KEY")

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
    #if output_csv_flag == True:
    output_csv(dataframe=df, flag = output_csv_flag, file_name = filename)

    return df