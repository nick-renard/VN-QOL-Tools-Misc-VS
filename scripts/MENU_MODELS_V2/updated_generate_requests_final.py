import pandas as pd
import json

def generate_ecosystem_settings(config_models_path, settings_path):
    config_df = pd.read_csv(config_models_path)
    settings_df = pd.read_csv(settings_path)

    # Map models to ecosystems and UUIDs
    model_to_info = {row['configuration_models_name']: (row['Ecosystem'], row['configuration_models_uuid']) 
                        for _, row in config_df.iterrows()}
    
    # Initialize a dictionary to hold settings by ecosystem
    ecosystems_settings = {}
    
    # Process settings for each model
    for column in settings_df.columns[2:]:  # Exclude 'setting_name' and 'value_type' columns
        ecosystem, uuid = model_to_info.get(column, (None, None))
        if ecosystem:
            if ecosystem not in ecosystems_settings:
                ecosystems_settings[ecosystem] = []
            
            for _, row in settings_df.iterrows():
                setting = {
                    "name": row['setting_name'],
                    "value": row[column],
                    "configuration_model_id": uuid
                }
                # Process and convert the value based on its declared type
                if row['value_type'] == 'boolean':
                    setting['value'] = True if row[column].lower() == 'true' else False
                elif row['value_type'] == 'array':
                    setting['value'] = row[column].split(', ')
                ecosystems_settings[ecosystem].append(setting)
    
    # Output a file for each ecosystem
    for ecosystem, settings in ecosystems_settings.items():
        with open(f'scripts/MENU_MODELS_V2/outputs/{ecosystem}_settings.json', 'w') as file:
            json.dump({"settings": settings}, file, indent=4)

if __name__ == "__main__":
    config_models_path = 'scripts/MENU_MODELS_V2/configuration_models_prd.csv'
    settings_path = 'scripts/MENU_MODELS_V2/settingMatrix.csv'
    generate_ecosystem_settings(config_models_path, settings_path)
