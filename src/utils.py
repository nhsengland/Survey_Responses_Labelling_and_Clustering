from typing import Dict, Optional
import pandas as pd

def normalise_column_names(
    df: pd.DataFrame,
    to_lower: bool = True,
    strip: bool = True,
    replace_values: Optional[Dict[str, str]] = None,
) -> pd.DataFrame:
    """
    Normalise the column names of a dataframe. By default:
        * The column names are cast to all lower case
        * Whitespace around the columns are remove
        * Punctuation and spaces are removed or replaced with underscores, "_".
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with messy column names
    to_lower : bool, optional
        Cast column names to lower case, by default True
    strip : bool, optional
        Strip whitespace from start and end of column names, by default True
    replace_values : Optional[Dict[str, str]], optional
        Dictionary of values to be replaces, by default {
        "-": "",
        "  ": " ",
        ",": "",
        "(": "",
        ")": "",
        "/": "_",
        ".": "_",
        " ": "_",
    }
    Returns
    -------
    pd.DataFrame
        Dataframe with cleaned column names
    """
    if to_lower:
        df.columns = df.columns.str.lower()

    if strip:
        df.columns = df.columns.str.strip()

    replace_values = (
        {
            "-": "",
            "  ": " ",
            ",": "",
            "(": "",
            ")": "",
            "/": "_",
            ".": "_",
            " ": "_",
        }
        if not replace_values
        else replace_values
    )

    for pat, repl in replace_values.items():
        df.columns = df.columns.map(lambda x, pat=pat, repl=repl: x.replace(pat, repl))

    return df