import time
import csv
import datetime
import re

from getpass import getpass
from scrapli import Scrapli
from scrapli.driver import GenericDriver
from scrapli.logging import enable_basic_logging

# Prompt for username and password
host = input("Enter firewall IP: ")
username = input("Enter username: ")
password = getpass("Enter password: ")

# repeat every X seconds (this is being doubled for some reason, 15 ends up being 30)
SLEEP = 60

# uncomment to enable logging
# enable_basic_logging(file=True, level="debug")

# Firewall data
panos_device = {
    "host": host,
    "auth_username": username,
    "auth_password": password,
    "auth_strict_key": False,
    "platform": "paloalto_panos",
    "channel_log": False,
}

# output file
csv_file = "throughput_data.csv"

# print column names to terminal for real time tracking
print ("Time","\t","Throughput (kbps)")

# Open the CSV file in append mode to ensure existing data is not overwritten
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Throughput"])

    while True:
        with Scrapli(**panos_device) as pan_conn:
            result = pan_conn.send_command("show session info | match Throughput")

            # Extract the throughput value using regex
            throughput = re.search(r"Throughput:\s+(\d+)", result.result)
            if throughput:
                throughput_value = throughput.group(1)
            else:
                throughput_value = "Not found"

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Write the timestamp and throughput to the CSV file
            writer.writerow([timestamp, throughput_value])
            print (timestamp,"\t",throughput_value)

            # Sleep
            time.sleep(SLEEP)