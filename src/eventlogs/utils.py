from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
import pm4py
from numpy.typing import NDArray


def load_eventlog(eventlog_path: Path, sep: str = ",") -> pd.DataFrame:
    """
    Load an event log from a file path.

    This function supports loading event logs from XES and CSV file formats.
    For XES files, it uses pm4py's read_xes function. For CSV files, it uses
    pandas' read_csv function with a configurable separator.

    Args:
        eventlog_path (Path): The path to the event log file to be loaded.
            Must have either .xes or .csv extension.
        sep (str, optional): The delimiter to use when reading CSV files.
            Defaults to ",".

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded event log data.

    Raises:
        ValueError: If the file format is not supported (neither .xes nor .csv).

    Examples:
        >>> log_df = load_eventlog(Path("data/process_log.xes"))
        >>> log_df = load_eventlog(Path("data/process_log.csv"), sep=";")
    """
    if eventlog_path.suffix.lower() == ".xes":
        return pm4py.read_xes(str(eventlog_path))
    elif eventlog_path.suffix.lower() == ".csv":
        return pd.read_csv(str(eventlog_path), sep=sep)
    else:
        raise ValueError(
            f"Unsupported file format: {eventlog_path.suffix}. Only .xes and .csv files are supported."
        )


def one_hot_encode_activity_presence(
    event_log: pd.DataFrame,
    trace_id_column: str = "case:id",
    activity_column: str = "concept:name",
) -> pd.DataFrame:
    activities = event_log[activity_column].unique()
    trace_activity_presence = {}
    for case_id, group in event_log.groupby(trace_id_column):
        # Create a boolean vector for each activity
        presence = {
            activity: activity in group[activity_column].values
            for activity in activities
        }
        trace_activity_presence[case_id] = presence

    return pd.DataFrame.from_dict(trace_activity_presence, orient="index")


def convert_eventLog_to_sequences(
    eventlog: pd.DataFrame,
    trace_id_column: str = "case:id",
    timestamp_column: str = "time:timestamp",
    activity_column: str = "concept:name",
) -> Dict[str, NDArray]:
    """
    Convert an event log to sequences of activities per trace.

    Args:
        eventlog: Event log DataFrame
        trace_id_column: Column name for trace/case ID
        timestamp_column: Column name for timestamp
        activity_column: Column name for activity

    Returns:
        Dictionary mapping trace_id to sequence (NDArray of activities)
    """
    # Sort the eventlog by trace_id and timestamp
    sorted_log = eventlog.sort_values([trace_id_column, timestamp_column])

    # Group by trace_id and aggregate activities into sequences
    sequences = {}
    for trace_id, group in sorted_log.groupby(trace_id_column):
        sequences[trace_id] = group[activity_column].values

    return sequences
