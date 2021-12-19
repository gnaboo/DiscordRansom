import json

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        create_json(filename)
        return {}

def create_json(filename):
    with open(filename, 'w') as f:
        json.dump({}, f)

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

# def create_server(data, server_id, key, server_name, server_members, server_channels, users):
#     data[server_id] = {"name": server_name, "key": key, "members": server_members, "text_channels": server_channels, "users": users}
#     return data
def create_server(config, serverid ,servername, text_channels, voice_channels, category, roles, users):
    config[serverid] = {"name": servername, 
                        "text_channels": text_channels, 
                        "voice_channels": voice_channels, 
                        "category": category, 
                        "roles": roles, 
                        "users": users
                        }
    return config

def get_server(server_id, data):
    return data[server_id]