#!/bin/env python
"""Module to generate pandas profiling on the data set"""
import pandas as pd
import pandas_profiling

filename = "data/census.csv"
df = pd.read_csv(filename)

pandas_profiling.ProfileReport(df).to_file("data/census.html")
