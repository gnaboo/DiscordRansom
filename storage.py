from saver import *

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
        self.roles[roles.id] = {"name": roles.name, "permissions": roles.permissions.value}

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

    def turn_data_to_unicode(self):
        for channel in self.text_channels:
            self.text_channels[channel]["topic"] = str(self.text_channels[channel]["topic"])
            self.text_channels[channel]["name"] = str(self.text_channels[channel]["name"])
            self.text_channels[channel]["position"] = str(self.text_channels[channel]["position"])
            self.text_channels[channel]["type"] = str(self.text_channels[channel]["type"])
        for channel in self.voice_channels:
            self.voice_channels[channel]["name"] = str(self.voice_channels[channel]["name"])
            self.voice_channels[channel]["position"] = str(self.voice_channels[channel]["position"])
            self.voice_channels[channel]["type"] = str(self.voice_channels[channel]["type"])
        for category in self.category:
            self.category[category]["name"] = str(self.category[category]["name"])
            self.category[category]["position"] = str(self.category[category]["position"])
        for roles in self.roles:
            self.roles[roles]["name"] = str(self.roles[roles]["name"])
            self.roles[roles]["permissions"] = str(self.roles[roles]["permissions"])
        for users in self.users:
            self.users[users]["name"] = str(self.users[users]["name"])
            self.users[users]["discriminator"] = str(self.users[users]["discriminator"])
            self.users[users]["avatar"] = str(self.users[users]["avatar"])

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
        print(config)
        save_json("victims.json", config)