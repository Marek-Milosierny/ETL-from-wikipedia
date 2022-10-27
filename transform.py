from extract import extract, extract_currency


def transform(data_to_transform, exchange_rate):
    data_to_transform.iloc[0,2] = data_to_transform.iloc[0,2][:6]
    data_to_transform["Market cap (US$ billion)"] = round(data_to_transform["Market cap (US$ billion)"].astype(float) * exchange_rate, 3)
    df_transformed = data_to_transform.rename(columns={"Market cap (US$ billion)": "Market Cap (EUR Billion)"})
    return df_transformed

