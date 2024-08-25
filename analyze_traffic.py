import pandas as pd
import numpy as np
import re
import sys

def analyze_traffic(file_path):
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    def detect_attack(row):
        if row['tcp.flags.syn'] == 1 and row['tcp.flags.ack'] == 0:
            return 'SYN Flood', 'Denial of Service'
        elif row['tcp.flags.syn'] == 1 and row['tcp.flags.ack'] == 1:
            return 'SYN-ACK Scan', 'Reconnaissance'
        elif row['tcp.flags.reset'] == 1:
            return 'TCP Reset Attack', 'Denial of Service'
        elif row['tcp.flags.push'] == 1:
            return 'TCP Push Attack', 'Denial of Service'
        else:
            return 'Unknown', 'Unknown'

    data['Attack Name'], data['Attack Type'] = zip(*data.apply(detect_attack, axis=1))

    filtered_data = data[data['Attack Name'] != 'Unknown']

    print("\nDetected attacks:")
    print(filtered_data[['ip.src', 'ip.dst', 'tcp.srcport', 'tcp.dstport', 'Attack Name', 'Attack Type']].head())

    attack_counts = filtered_data['Attack Name'].value_counts()

    print("\nAttack Pattern Counts:")
    for attack_name, count in attack_counts.items():
        print(f"{attack_name}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_traffic.py <path_to_csv>")
    else:
        csv_file_path = sys.argv[1]
        analyze_traffic(csv_file_path)
