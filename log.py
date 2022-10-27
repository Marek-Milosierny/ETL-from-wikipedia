from datetime import datetime


def log(message):
    timestamp_format = "%d.%m.%Y %H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write(timestamp + "," + message + "\n")