from saver import *
import base64

class Victim:
    def __init__(self,
                 server,
                 text_channels={},
                 voice_channels={},
                 category={},
                 roles={},
                 users={}
                 ):

        self.server = server

        self.text_channels = text_channels
        self.voice_channels = voice_channels
        self.category = category
        self.roles = roles
        self.users = users

    def add_text_channels(self, channel):
        self.text_channels[channel.id] = {"name": channel.name, "topic": channel.topic, "position": channel.position, "type": channel.type}

    def add_voice_channels(self, channel):
        self.voice_channels[channel.id] = {"name": channel.name, "position": channel.position, "type": channel.type}
    
    def add_category(self, category):
        self.category[category.id] = {"name": category.name, "position": category.position}

    def add_role(self, roles):
        self.roles[roles.id] = {"name": roles.name}

    def add_user(self, users):
        self.users[users.id] = {"name": users.name, "discriminator": users.discriminator, "avatar": users.avatar}

    def print_data(self):
        print(self.server.name)
        print(self.server.id)
        print("\n")
        print(self.text_channels)
        print(self.voice_channels)
        print(self.category)
        print(self.roles)
        print(self.users)

    def encode_data(self):
        for channel in self.text_channels:
            self.text_channels[channel]["topic"] = base64.b64encode(str(self.text_channels[channel]["topic"]).encode()).decode()
            self.text_channels[channel]["name"] = base64.b64encode(str(self.text_channels[channel]["name"]).encode()).decode()
            #self.text_channels[channel]["position"] = base64.b64encode(str(self.text_channels[channel]["position"]).encode()).decode()
            #self.text_channels[channel]["type"] = base64.b64encode(str(self.text_channels[channel]["type"]).encode()).decode()
        for channel in self.voice_channels:
            self.voice_channels[channel]["name"] = base64.b64encode(str(self.voice_channels[channel]["name"]).encode()).decode()
            #self.voice_channels[channel]["position"] = base64.b64encode(str(self.voice_channels[channel]["position"]).encode()).decode()
            #self.voice_channels[channel]["type"] = base64.b64encode(str(self.voice_channels[channel]["type"]).encode()).decode()
        for category in self.category:
            self.category[category]["name"] = base64.b64encode(str(self.category[category]["name"]).encode()).decode()
            #self.category[category]["position"] = base64.b64encode(str(self.category[category]["position"]).encode()).decode()
        for roles in self.roles:
            self.roles[roles]["name"] = base64.b64encode(str(self.roles[roles]["name"]).encode()).decode()
        for users in self.users:
            self.users[users]["name"] = base64.b64encode(str(self.users[users]["name"]).encode()).decode()
            #self.users[users]["discriminator"] = base64.b64encode(str(self.users[users]["discriminator"]).encode()).decode()
            #self.users[users]["avatar"] = base64.b64encode(str(self.users[users]["avatar"]).encode()).decode()

    def decode_data_from_base64(self):
        for channel in self.text_channels:
            self.text_channels[channel]["topic"] = base64.b64decode(str(self.text_channels[channel]["topic"]).encode()).decode()
            self.text_channels[channel]["name"] = base64.b64decode(str(self.text_channels[channel]["name"]).encode()).decode()
        for channel in self.voice_channels:
            self.voice_channels[channel]["name"] = base64.b64decode(str(self.voice_channels[channel]["name"]).encode()).decode()
        for category in self.category:
            self.category[category]["name"] = base64.b64decode(str(self.category[category]["name"]).encode()).decode()
        for roles in self.roles:
            self.roles[roles]["name"] = base64.b64decode(str(self.roles[roles]["name"]).encode()).decode()
        for users in self.users:
            self.users[users]["name"] = base64.b64decode(str(self.users[users]["name"]).encode()).decode()

    def load_data(self):
        config = load_json("victims.json")
        self.server = config[str(self.server.id)]
        self.text_channels = self.server["text_channels"]
        self.voice_channels = self.server["voice_channels"]
        self.category = self.server["category"]
        self.roles = self.server["roles"]
        self.users = self.server["users"]

    def store_data(self):
        config = load_json("victims.json")
        config = create_server(config,
                               self.server.id,
                               self.server.name,
                               self.text_channels,
                               self.voice_channels,
                               self.category,
                               self.roles,
                               self.users)

        save_json("victims.json", config)