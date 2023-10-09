import numpy as np
import pandas as pd
from scipy.signal import find_peaks


def main():
    # Read the data from the original Excel file
    data = pd.read_excel('2023_1.xlsx', header=None, index_col=None)

    # Find the first peaks in each row
    first_peaks = find_first_peaks(data)

    # Append the first peaks as a new column 'Peak'
    data['Peak'] = first_peaks

    # Save the modified DataFrame to a new Excel file
    data.to_excel("2023_1_1.xlsx", index=False)


def find_first_peaks(data):
    first_peaks = []
    for row in data.values:
        peaks = find_all_peaks(row)
        if len(peaks) > 0:
            first_peaks.append(peaks[0])
        else:
            first_peaks.append(np.nan)
    return first_peaks


def find_all_peaks(y_axis):
    peaks, _ = find_peaks(y_axis, height=y_axis, distance=1000)
    return peaks

if __name__ == '__main__':
    main()
