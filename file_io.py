import os
import pandas as pd

def output_csv(dataframe, file_name, flag = False, report = True):
    if flag:
        # Check if folder exists, if not, create it
        if not os.path.exists('Dataset'):
            os.makedirs('Dataset')

        # Save DataFrame as CSV inside the folder
        csv_path = os.path.join('Dataset', f'{file_name}.csv')
        dataframe.to_csv(csv_path, index=False)
        if report:
            print(f"DataFrame saved to {csv_path}")

def input_csv(file_name, report=True):
    csv_path = os.path.join('Dataset', f'{file_name}.csv')
    
    if not os.path.exists(csv_path):
        if report:
            print(f"File {csv_path} not found.")
        return None
    
    df = pd.read_csv(csv_path)
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
        fig.savefig(png_path)
        if report:
            print(f"Plot saved to {png_path}")