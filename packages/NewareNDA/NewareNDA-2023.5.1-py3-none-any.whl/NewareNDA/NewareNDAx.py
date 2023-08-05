# © 2023 Copyright SES AI
# Author: Daniel Cogswell
# Email: danielcogswell@ses.ai

import mmap
import struct
import zipfile
import logging
from datetime import datetime
import pandas as pd

from NewareNDA.dictionaries import *


def read(file):
    zf = zipfile.PyZipFile(file)
    zf.extract('data_Aux.ndc')
    data_file = zf.extract('data.ndc')

    data_df = read_ndc(data_file)

    # # Join temperature data
    # aux_df = pd.DataFrame(aux, columns=aux_columns)
    # aux_df.drop_duplicates(inplace=True)
    # if not aux_df.empty:
    #     pvt_df = aux_df.pivot(index='Index', columns='Aux', values='T')
    #     for k in pvt_df.keys():
    #         pvt_df.rename(columns={k: f"T{k}"}, inplace=True)
    #     df = df.join(pvt_df, on='Index')

    return data_df


def read_ndc(file):
    """
    Function read electrochemical data from a Neware ndc binary file.

    Args:
        file (str): Name of a .ndc file to read
    Returns:
        df (pd.DataFrame): DataFrame containing all records in the file
    """
    with open(file, 'rb') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        # Identify the beginning of the data section
        record_len = 94
        identifier = b'\x55\x01\x02\x00\xC6\x06\x00\xA8'
        header = mm.find(identifier)
        if header == -1:
            raise EOFError(f"File {file} does not contain any valid records.")
        mm.seek(header)

        # Read data records
        output = []
        # aux = []
        while header != -1:
            mm.seek(header)
            bytes = mm.read(record_len)
            output.append(_bytes_to_list_ndc(bytes[6:]))
            header = mm.find(identifier, header + 8)

    # Create DataFrame and sort by Index
    df = pd.DataFrame(output, columns=rec_columns)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    if not df['Index'].is_monotonic_increasing:
        df.sort_values('Index', inplace=True)

    df.reset_index(drop=True, inplace=True)

    # Postprocessing
    df['Step'] = _count_changes(df['Step'])
    df['Cycle'] = _generate_cycle_number(df)
    df = df.astype(dtype=dtype_dict)
    return df


def _bytes_to_list_ndc(bytes):
    """Helper function for interpreting a byte string"""

    # Extract fields from byte string
    [Index, Cycle] = struct.unpack('<II', bytes[2:10])

    [Step] = struct.unpack('<I', bytes[10:14])
    # [Status, Jump, Time] = struct.unpack('<BBQ', bytes[12:22])

    [Status] = struct.unpack('<B', bytes[11:12])
    [Time] = struct.unpack('<Q', bytes[17:25])
    [Voltage, Current] = struct.unpack('<ii', bytes[25:33])
    [Charge_capacity, Discharge_capacity] = struct.unpack('<qq', bytes[37:53])
    [Charge_energy, Discharge_energy] = struct.unpack('<qq', bytes[53:69])
    [Y, M, D, h, m, s] = struct.unpack('<HBBBBB', bytes[69:76])
    [Range] = struct.unpack('<i', bytes[76:80])

    multiplier = multiplier_dict[Range]

    # Create a record
    list = [
        Index,
        Cycle + 1,
        Step,
        state_dict[Status],
        Time/1000,
        Voltage/10000,
        Current*multiplier,
        Charge_capacity*multiplier/3600,
        Discharge_capacity*multiplier/3600,
        Charge_energy*multiplier/3600,
        Discharge_energy*multiplier/3600,
        datetime(Y, M, D, h, m, s)
    ]
    return list


def _aux_bytes_to_list(bytes):
    """Helper function for intepreting auxiliary records"""
    [Aux, Index] = struct.unpack('<BI', bytes[1:6])
    [T] = struct.unpack('<h', bytes[34:36])

    return [Index, Aux, T/10]


def _generate_cycle_number(df):
    """
    Generate a cycle number to match Neware. A new cycle starts with a charge
    step after there has previously been a discharge.
    """

    # Identify the beginning of charge steps
    chg = (df.Status == 'CCCV_Chg') | (df.Status == 'CC_Chg')
    chg = (chg - chg.shift()).clip(0)
    chg.iat[0] = 1

    # Convert to numpy arrays
    chg = chg.values
    status = df.Status.values

    # Increment the cycle at a charge step after there has been a discharge
    cyc = 1
    dchg = False
    for n in range(len(chg)):
        if chg[n] & dchg:
            cyc += 1
            dchg = False
        elif 'DChg' in status[n] or status[n] == 'SIM':
            dchg = True
        chg[n] = cyc

    return chg


def _count_changes(series):
    """Enumerate the number of value changes in a series"""
    a = series.diff()
    a.iloc[0] = 1
    a.iloc[-1] = 0
    return (abs(a) > 0).cumsum()
