import json
import csv

def run():
    # Read JSON input data
    with open('scripts//EXPORT_SPAS/export_spas_input.json') as f:
        data = json.load(f)

    # Open output CSV file for writing
    with open('scripts//EXPORT_SPAS/export_spas_output.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # Write CSV header
        writer.writerow(['account', 'type', 'name', 'ecosystem', 'env', 'region', 'organization', 'configured_version', 'stack_name', 'stack_status', 'update_behavior', 'version'])

        # Write CSV rows
        for row in data:
            writer.writerow([row['account'], row['type'], row['name'], row['ecosystem'], row['env'], row['region'], row['organization'], row['configured_version'], row['stack_name'], row['stack_status'], row['update_behavior'], row['version']])

run()