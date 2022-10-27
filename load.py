import pandas as pd
from transform import transform


def load(data_to_load):
    data_to_load.to_csv("bank_market_cap_eur.csv", index=False)