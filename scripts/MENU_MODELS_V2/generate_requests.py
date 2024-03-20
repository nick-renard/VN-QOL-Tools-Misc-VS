import pandas as pd
import json

def process_column(df, column):
    json_data = {"settings": []}
    for index, row in df.iterrows():
        value = row[column]
        setting = {
            "name": row['setting_name'],
            "value": value,
            "configuration_model_id": column
        }
        if pd.notna(value):  
            if row['value_type'] == 'boolean' and setting['value'] is not None:
                setting['value'] = str(setting['value']).lower() == 'true'
            elif row['value_type'] == 'int' and setting['value'] is not None:
                setting['value'] = int(setting['value'])
            elif row['value_type'] == 'float' and setting['value'] is not None:
                setting['value'] = float(setting['value'])
            elif row['value_type'] == 'string' and setting['value'] is not None:
                setting['value'] = str(setting['value'])
            elif row['value_type'] == 'array' and setting['value'] is not None:
                setting['value'] = setting['value'].split(', ')
                
            existing_setting = next((s for s in json_data["settings"] if s["name"] == setting["name"]), None)
            if existing_setting:
                existing_setting["value"] = setting["value"]
            else:
                json_data["settings"].append(setting)

    return json_data

def generate_json_files(csv_file):
    df = pd.read_csv(csv_file)

    for column in df.columns[2:]:
        json_data = process_column(df, column)
        json_file_type = ".json"
        initial_path = "scripts/MENU_MODELS_V2/outputs/"
        output_file = initial_path + column + json_file_type
        # output_file = f"scripts/MENU_MODELS/outputs/{column}.json"
        with open(output_file, 'w') as file:
            json.dump(json_data, file, indent=4)

if __name__ == "__main__":
    csv_file = 'scripts/MENU_MODELS_V2/settingMatrix.csv'
    generate_json_files(csv_file)
