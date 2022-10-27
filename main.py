from locale import currency
from extract import extract, extract_currency
from transform import transform
from load import load
from log import log

def etl():
    log("ETL process started")
    log("Extract phase strted")
    exchange_rate = extract_currency("EUR")
    extracted_data = extract()
    log("Extract phase ended")
    log("Transform phase started")
    transformed_data = transform(extracted_data, exchange_rate)
    log("Transform phase ended")
    log("Load phase sterted")
    load(transformed_data)
    log("Load phase ended")
    log("ETL process ended")


def main():
    etl()


if __name__ == '__main__':
    main()


