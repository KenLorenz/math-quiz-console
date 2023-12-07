import json

def createJSON(): # writes default settings
    default_settings = {
        "level": {1:"1-10"},
        "op": 1, #1 = add, 2 = sub, 3 = mul
        "numItems": 5,
        "ansVariety": 5, # 5 below the correct answer and 5 above the correct answer, for randrange
    }
    
    with open('assets/settings_data.json', 'w') as json_file:
        json.dump(default_settings, json_file)
        return
    
def loadJSON(): # reads json file
    try:
        with open('assets/settings_data.json', 'r') as json_file:
            x = json.load(json_file)
            return x
    except:
        createJSON()
        return loadJSON()

def settings_modify(specified_setting, new_value): # only changes one setting at a time.
        settings_data = loadJSON()
        
        settings_data[specified_setting] = new_value # modifies a specific setting
        
        with open('assets/settings_data.json', 'w') as json_file:
            json.dump(settings_data, json_file) # recreates a new json with modified setting
