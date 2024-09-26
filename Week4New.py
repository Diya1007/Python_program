'''import pandas as pd
import numpy as np

# Load the current dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/pokemon/pokemon_entries.csv')

def validate_entry(new_entry):
    # Normalize trainer_name to lowercase
    new_entry['trainer_name'] = new_entry['trainer_name'].lower()
    
    # Check for duplicate entries
    if ((df['pokemon_id'] == new_entry['pokemon_id']) &
        (df['trainer_name'].str.lower() == new_entry['trainer_name']) &
        (df['seen_time'] == new_entry['seen_time'])).any():
        print(f"Duplicate entry found for {new_entry['trainer_name']} with ID {new_entry['pokemon_id']} at {new_entry['seen_time']}.")
        return None  # Indicate a duplicate entry

    # Validate pokemon_id
    try:
        new_entry['pokemon_id'] = int(new_entry['pokemon_id'])
        assert new_entry['pokemon_id'] >= 0
    except (ValueError, AssertionError):
        return {"error": "pokemon_id must be a non-negative integer."}

    # Validate pokemon_type
    valid_types = {'Water', 'Fire', 'Grass', 'Earth', 'Normal'}
    pokemon_type = new_entry.get('pokemon_type', '').strip()
    
    if pokemon_type == "":
        new_entry['pokemon_type'] = None
    elif pokemon_type.capitalize() not in valid_types:
        return {"error": "Invalid pokemon_type."}
    else:
        new_entry['pokemon_type'] = pokemon_type.capitalize()

    # Validate seen_time
    try:
        new_entry['seen_time'] = pd.to_datetime(new_entry['seen_time'])

        # Check if new seen_time is before existing sightings
        existing_seen_time = df.loc[df['trainer_name'].str.lower() == new_entry['trainer_name'], 'seen_time']
        if not existing_seen_time.empty:
            if new_entry['seen_time'] < pd.to_datetime(existing_seen_time.min()):
                return {"error": f"This sighting is before the first recorded sighting for {new_entry['trainer_name']}."}
    except (ValueError, TypeError):
        return {"error": "Invalid seen_time format."}

    return new_entry

new_sighting = {
    'pokemon_id': 12,
 'trainer_name': 'Trainer_8',
 'pokemon_type': 'Normal',
 'seen_time': '2022-01-04'
}

valid_entry = validate_entry(new_sighting)
if isinstance(valid_entry, dict) and 'error' not in valid_entry:
    print("Valid entry:", valid_entry)
    newItem = pd.DataFrame([valid_entry])
    df = pd.concat([df, newItem], ignore_index=True)
    print("Appended to dataset.")
else:
    print("Not valid:", valid_entry)
    '''


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/pokemon/pokemon_entries.csv')

def validate_entry(entry):
    if df[(df['pokemon_id'] == entry['pokemon_id']) & 
          (df['trainer_name'].str.lower() == entry['trainer_name'].lower()) & 
          (df['seen_time'] == entry['seen_time'])].shape[0] > 0:
        print("Duplicate entry")
        return None

    valid_types = {'Water', 'Fire', 'Grass', 'Earth', 'Normal'}
    if 'pokemon_type' in entry:
        pokemon_type = entry['pokemon_type'].capitalize()
        if pokemon_type == "":
            entry['pokemon_type'] = None
        elif pokemon_type not in valid_types:
            print("Invalid pokemon type")
            return None
        else:
            entry['pokemon_type'] = pokemon_type

    try:
        entry['pokemon_id'] = int(entry['pokemon_id'])
        assert entry['pokemon_id'] >= 0, "pokemon_id must be >= 0"
    except ValueError:
        print("pokemon_id should be valid integer")
        return None
    except AssertionError as e:
        print(str(e))
        return None

    try:
        if len(entry['seen_time']) != 19:  # YYYY-MM-DD HH:MM:SS format, hence len 19
            print("The seen_time has no time associated with it")
            return None
        
        new_time = pd.to_datetime(entry['seen_time'])
        trainer_entries = df[df['trainer_name'].str.lower() == entry['trainer_name'].lower()]
        
        if not trainer_entries.empty:
            earliest_time = pd.to_datetime(trainer_entries['seen_time'].min())
            if new_time < earliest_time:
                print(f"This is before the first sighting for {entry['trainer_name']}")
                return None
    except ValueError:
        print(f"Invalid date format: {entry['seen_time']}")
        return None

    return entry


new_entry = {
  'pokemon_id': 5,
 'trainer_name': 'Trainer_6',
 'pokemon_type': 'Fire',
 'seen_time': '2024-01-01 16:00:00'
}

valid_entry = validate_entry(new_entry)
if valid_entry:
    print("Entry Validated:", valid_entry)          #print the data of valid entry
    newItem = pd.DataFrame([valid_entry])
    df = pd.concat([df, newItem], ignore_index=True)
else:
    print("Entry not valid")