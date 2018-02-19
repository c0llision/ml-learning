#!/usr/bin/env python3
import pandas as pd
import quandl as Quandl

df = Quandl.get("WIKI/GOOGL")

print(df.head())
