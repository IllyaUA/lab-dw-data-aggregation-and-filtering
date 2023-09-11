import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Optional, Tuple

def scatter_plot(df: pd.DataFrame, x_col: str, y_col: str, hue_col: Optional[str] = None) -> Tuple[plt.Figure, plt.Axes]:
    '''
    Create a scatterplot of two columns from a Pandas DataFrame.

    Parameters:
    - df: Pandas DataFrame
        The DataFrame containing the data to be plotted.
    - x_col: str
        The name of the column to be used as the x-axis.
    - y_col: str
        The name of the column to be used as the y-axis.
    - hue_col: str (optional)
        The name of the column to be used for marker colors.

    Returns:
    - Tuple[plt.Figure, plt.Axes]
        Returns a tuple containing the Figure and Axes objects for the scatterplot.
    '''
    # Create the scatterplot
    fig, ax = plt.subplots(figsize=(10, 6))

    if hue_col is None:
        fig=sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
    else:
        fig=sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col, palette='Set2', ax=ax)

    # Set plot title and labels
    ax.set_title(f'Scatter Plot: {x_col} vs {y_col}')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    # Add legend
    plt.legend(title=hue_col, loc='upper right')

    # Show the plot
    plt.show()

    return fig, ax
