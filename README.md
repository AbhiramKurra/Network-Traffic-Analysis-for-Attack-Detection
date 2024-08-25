# Network Traffic Analysis for Attack Detection



## Project Description

This Python-based project analyzes network traffic data captured in a `.csv` file to detect potential cyber-attacks. The program uses regular expressions and predefined patterns to identify various types of network attacks, such as SYN Flood, SYN-ACK Scan, TCP Reset Attack, and TCP Push Attack. It provides an output that specifies the attack name and type based on the analyzed traffic data.

## Features

- **Input CSV File**: The program accepts a CSV file containing network traffic data as input.
- **Attack Detection**: Detects common network attacks using specific patterns in the traffic data.
- **Output**: Displays detected attacks, including attack names and types, along with the counts of each attack pattern.
- **Optimized for Speed**: Efficiently reads and processes large CSV files.

## Prerequisites

- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/network-traffic-analysis.git
    cd network-traffic-analysis
    ```

2. **Install Dependencies**:
    Install the required Python packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare Your CSV File**:
    Ensure your CSV file contains the following columns:
    - `frame number`, `eth src`, `eth dst`, `eth type`, `ip hdr_len`, `ip len`, `ip id`, `ip flags`, `ip ttl`, `ip proto`, `ip src`, `ip dst`, `tcp src port`, `tcp dst port`, `tcp stream`, `tcp len`, `tcp seq`, `tcp nxtseq`, `tcp ack`, `tcp hdr_len`, `tcp flags`, `tcp window_size_value`, `tcp window_size`, `tcp payload`, `tcp analysis.bytes_in_flight`, `tcp analysis.push_bytes_sent`, `frame len`, `label`

2. **Run the Program**:
    Use the following command to run the script, replacing `path_to_csv_file.csv` with the actual path to your CSV file:
    ```bash
    python analyze_traffic.py <path_to_csv_file.csv>
    ```

3. **View the Output**:
    The program will display detected attacks and their counts in the terminal.


## Project Structure

- **analyze_traffic.py**: Main script to analyze the network traffic CSV file.
- **requirements.txt**: List of dependencies required to run the script.
- **README.md**: Project documentation.


