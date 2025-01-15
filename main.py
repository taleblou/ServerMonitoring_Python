import pandas as pd
import requests
import time
import datetime
import os
from requests.exceptions import RequestException
import ping3
from urllib.parse import urlparse

# Define the URL to monitor
url = 'https://www.taleblou.ir/'

# Set the CSV file name
csv_file = 'url_reports.csv'

# Check if the CSV file exists to decide whether to write headers
if os.path.exists(csv_file):
    write_headers = False
else:
    write_headers = True

# Infinite loop to check the URL every 30 seconds
while True:
    try:
        # Parse the URL to get the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        # Ping the server
        ping_time = ping3.ping(hostname) * 1000  # in milliseconds
    except Exception as e:
        ping_time = float('nan')  # Use NaN for missing ping time

    try:
        # Record the start time
        start_time = time.time()

        # Make the HTTP request
        response = requests.get(url)

        # Calculate loading time
        loading_time = time.time() - start_time

        # Get content length
        content_length = response.headers.get('Content-Length')
        if content_length is None:
            response_size = float('nan')
        else:
            response_size = int(content_length)

        # Get status code
        status_code = response.status_code

        # No error message if successful
        error_message = ''

    except RequestException as e:
        # Record error if request fails
        loading_time = time.time() - start_time
        status_code = None
        error_message = str(e)
        response_size = float('nan')

    # Get current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create a dictionary with the data
    data = {
        'Date': [current_time],
        'Ping Time (ms)': [ping_time],
        'Loading Time (s)': [loading_time],
        'Response Size (bytes)': [response_size],
        'Status Code': [status_code],
        'Error Message': [error_message]
    }

    # Create a DataFrame
    df = pd.DataFrame(data,
                      columns=['Date', 'Ping Time (ms)', 'Loading Time (s)', 'Response Size (bytes)', 'Status Code',
                               'Error Message'])

    # Append the DataFrame to the CSV file
    if write_headers:
        df.to_csv(csv_file, mode='w', index=False)
    else:
        df.to_csv(csv_file, mode='a', index=False, header=False)

    # Only write headers once
    if write_headers:
        write_headers = False

    # Wait for 30 seconds
    time.sleep(30)