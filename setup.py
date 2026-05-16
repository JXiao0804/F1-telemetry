import pandas as pd
import fastf1
import os

CACHE_DIR = "/Users/jackxiao/Desktop/F1 telemetry/fastf1_cache"
os.makedirs(CACHE_DIR, exist_ok=True)
fastf1.Cache.enable_cache(CACHE_DIR)