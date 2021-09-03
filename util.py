"""
    This file is for general functions that are used across multiple modules.
"""

from tkinter.filedialog import askopenfilenames, askopenfilename
from common import constants as const
from datetime import datetime
from nptdms import TdmsFile
import tkinter as tk
import pandas as pd
import numpy as np
import time
import h5py
import os
import re


def currentTime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def bytesSizeConversion(totalBytes, converTo="mb"):
    converTo = converTo.lower()

    if converTo == "mb" or converTo == "megabytes":
        return totalBytes / 1048576
        
        
def convertEpochTimeList(time_list):
    """
        Converts millisecond epoch time to human readable
    """
    dates_times_list = [datetime.fromtimestamp(item / 1e3) for item in time_list]

    return dates_times_list


def convertEpochTime(df, timeColumnName="Datetime"):
    """
        Converts millisecond epoch time to human readable
    """
    convert = lambda x: datetime.fromtimestamp(x / 1e3)
    dfTime = df[timeColumnName].apply(convert)

    df[timeColumnName] = dfTime

    return df


def extractTimeFromFileName(strg):
    """
    @param Takes in string containing date time formatted as "%Y-%m-%d_%H-%M-%S"
    @return Total seconds date time in file name
    """
    try:
        # Get date time from string
        timeString = re.findall(const.REGX["datetime"], strg)[0]
        dt = datetime.strptime(timeString, "%Y-%m-%d_%H-%M-%S")
        totalSeconds = dt.timestamp()
    except:
        try:
            # Get date time from string (different format)
            timeString = re.findall(const.REGX["datetime"], strg)[0]
            dt = datetime.strptime(timeString, "%Y-%m-%d_%H_%M_%S")
            totalSeconds = dt.timestamp()
        except:
            totalSeconds = time.time()  # Current time

    return totalSeconds


def decimateDfBySecond(df, timeColumnName="Timestamp"):
    """
        @param Takes pandas dataframe and time column name (time column has to be in ms)
        @return Pandas dataframe with new DateTime column
    """
    # Add new column with human readable time
    df["DateTime"] = df[timeColumnName] 
    df = convertEpochTime(df, "DateTime")

    # Remove microseconds and drop duplicate rows by DateTime column (decimating data)
    df['DateTime'] = df['DateTime'].values.astype('datetime64[s]')
    df = df.drop_duplicates(subset=['DateTime'])
    df = df.sort_values(by="DateTime")
    df = df.reset_index(drop=True)

    return df


# This function merges multiple HDF5 files together and sorts them by Timestamp
def mergeHdfFiveFilesToDataFrame(files):
    df = pd.DataFrame()

    for file in files:
        fileSize = os.path.getsize(file) 
        fileSizeconverted = round(bytesSizeConversion(fileSize), 2)  # Convert from bytes to megabytes

        print(f"Processing {files.index(file)+1}/{len(files)} Size({fileSizeconverted}MB) - {file}")
        try:
            tempDf = hdfFiveToDataFrame(file)
            df = df.append(tempDf, ignore_index = True)
        except KeyError:
            print(f"FILE ERROR, skipping: {files.index(file)+1}/{len(files)} - {file}")
            continue

    if not df.empty:
        # Delete rows with timestamp = 0
        # Get indexes where Time column has value 0
        indexTimes = df[df["Timestamp"] == 0].index
        # Delete these row indexes from dataFrame
        df.drop(indexTimes, inplace=True)
        
        df = df.sort_values(by="Timestamp")
        df = df.reset_index(drop=True)

    return df


# This functions takes a TDMS telemetry file and returns it as a pandas DataFrame
def tdmsFileAsDataframe(fileName):
    df = TdmsFile(fileName).as_dataframe(time_index=False, absolute_time=False)
    return df


# This function merges multiple TDMS telemetry files together and sorts them by Time
def mergeTdmsFilesToDatafarame(files):
    df = pd.DataFrame()

    for file in files:
        fileSize = os.path.getsize(file) 
        fileSizeconverted = round(bytesSizeConversion(fileSize), 2)  # Convert from bytes to megabytes

        print(f"Processing {files.index(file)+1}/{len(files)} Size({fileSizeconverted}MB) - {file}")
        try:
            tempDf = tdmsFileAsDataframe(file)
            df = df.append(tempDf, ignore_index = True)
        except KeyError:
            print(f"FILE ERROR, skipping: {files.index(file)+1}/{len(files)} - {file}")
            continue

    if not df.empty:
        # Changing columns names to only include the last part of the name after "/"
        oldColumnNames = list(df.columns.values)
        df.columns = [i.split("/")[-1].replace("'", "") for i in oldColumnNames]
        
        df["timestamp"] = df["timestamp"].fillna(0)
        
        # Delete rows with timestamp = 0
        # Get indexes where Time column has value 0
        indexTimes = df[df["timestamp"] == 0].index
        # Delete these row indexes from dataFrame
        df.drop(indexTimes, inplace=True)
        
        df = df.sort_values(by="timestamp")
        df = df.reset_index(drop=True)

    return df


# Function saves DataFrame to CSV file
def dfToCSV(fileName, df):
    with open(fileName, 'w', newline='') as csvfile:
        df.to_csv(csvfile, header=True) 


def dataFrameResolution(df, hertz):
    """
        Changing data resolution (get every nth row).
        This is done because data is sampled at n Hertz
    """
    if hertz > 0:
        skip = hertz * 100  # Skip is milliseconds for every nth row.
        df = df.iloc[::skip]

    return df


def getFiles():
    """
        Uses tkinter to open a file dialog box and allows user selection of
        multiple files. 
        @return List of files.
    """
    root = tk.Tk()
    files = askopenfilenames(parent=root, title="Select files to join.")
    root.quit()
    root.destroy()
    files = list(files)

    return (files)


def getFile():
    """
        Uses tkinter to open a file dialog box and allows user selection of
        a file.
        @return File path.
    """
    root = tk.Tk()
    file = askopenfilename(parent=root, title="Select file")
    root.quit()
    root.destroy()

    return file


def getFileName(filePath):
    """
        @param Takes a file path as input.
        @return File name only without extension.
    """
    return os.path.splitext(os.path.basename(filePath))[0]


def timeSliceDataframe(df, start, end, timeColumn):
    """
        Slice dataframe using time column.
        @param Dataframe, start time, end time, time column name.
        @return Sliced dataframe.
    """
    return df[(df[timeColumn] >= start) & (df[timeColumn] <= end)]


def directoryName(filePath):
    """
        @param Takes a file path.
        @return Directory where file is located.
    """
    return f"{os.path.dirname(filePath)}"
