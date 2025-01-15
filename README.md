## **How It Works**

1. The script monitors a URL specified in the `url` variable.  
   * Default: `https://www.taleblou.ir/`  
2. It runs in an infinite loop, collecting data every 30 seconds.  
3. The collected metrics include:  
   * **Date and Time**: Timestamp of the data collection.  
   * **Ping Time**: Time taken to ping the server in milliseconds.  
   * **Loading Time**: Time taken to load the webpage in seconds.  
   * **Response Size**: The content length of the HTTP response in bytes.  
   * **Status Code**: The HTTP status code returned by the server.  
   * **Error Message**: Details of any error encountered during the request.  
4. The data is appended to a CSV file named `url_reports.csv`.  
   * If the file doesn't exist, headers are added automatically.

## **Usage**

1. Clone the repository or copy the script into your project directory.  
2. Modify the `url` variable to the URL you want to monitor.  
3. Run the script:  
   bash  
   Copy code  
   `python main.py`  
     
4. The script will create (or update) a CSV file named `url_reports.csv` with the collected data.

## **CSV Format**

The generated CSV file contains the following columns:

* `Date`: Timestamp of the monitoring event.  
* `Ping Time (ms)`: Ping response time in milliseconds.  
* `Loading Time (s)`: Time taken to load the page in seconds.  
* `Response Size (bytes)`: Size of the HTTP response in bytes.  
* `Status Code`: HTTP status code returned by the server.  
* `Error Message`: Error details, if any.

## **Customization**

* **Change Monitoring Interval**: Update the `time.sleep(30)` line to modify the check frequency.  
* **Specify a Different Output File**: Change the `csv_file` variable to use a different filename.

## **Notes**

* The script will continue running until manually stopped.  
* Ensure you have proper permissions to write to the directory where the CSV file is stored.  
* The script handles missing ping times and response sizes by logging `NaN` values.

## **License**

This project is licensed under the MIT License. Feel free to use and modify it as needed.

css 

``Feel free to adjust the `README.md` according to any specific details or extra context you'd like to include!``

