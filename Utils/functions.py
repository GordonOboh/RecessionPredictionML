import matplotlib.pyplot as plt
import seaborn as sns

def series_codes_update(dataframe, dict):
    for key in dataframe.keys():
        dict[key] = key

def vis_missing_data(data, color_space='rocket'):
    """Simple heatmaap to visualize missing data"""
    """Handle both DataFrames and Series"""
    if isinstance(data, pd.Series):
        # Convert Series to DataFrame
        data = data.to_frame()
    
    sns.heatmap(data.isnull(), cbar=False, cmap=color_space, yticklabels=False)
    plt.title("Missing Data Heatmap")
    plt.show()


def line_plot(dataframe, labels, plot_title, hlines = None):
    fig, ax = plt.subplots(figsize=(20,5))

    for col_name, col_data in dataframe.items():
        time = col_data.index
        ax.plot(time, col_data, label=labels[col_name])

    ax.set(xlabel='Years', ylabel='Yield (%)',
       title=plot_title)

    # Draw horizontal lines
    #print(type(hlines))
    if hlines is not None:
        for y, col in hlines.items():
            plt.axhline(y=y, color='red', linestyle='--', linewidth=1.3)

    if recessions is not None:
        for start, end, color, label_rec in recessions:
            ax.axvspan(start, end, color=color, alpha=0.2, label=label_rec)


    ax.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()  # Prevent label clipping
    plt.show()

    return plt, fig
    

