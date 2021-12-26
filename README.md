# DiscordRansom

> An educational project to raise awareness about unsafe Discord Bots


> [**Developed using discord.py**](https://discordpy.readthedocs.io/en/stable/)


# Concept

> The concept is fairly simple and inspired by [ransomwares](https://www.malwarebytes.com/ransomware), consisting in a *a type of malware that prevents users from accessing their system or personal files and demands ransom payment in order to regain access.*

> I had this concept of Discord Server Ransomware sitting in my head until I met a friend who considered her Discord Server as her baby, and that she would do anything to protect it. 

> Using [Discord's Developers Portal](https://discord.com/developers/docs/intro), it is pretty easy to make a bot that, when given the correct permissions, will trash a server. (*A.k.a. a Raid Bot*), but then they would be no going back.

> This Discord Bot will register all informations in the file `victims.json` and then trash the server. That way, it is very simple for users to get their server back if given the json backup.

## An exemple:

```json
{
    "840954377291300875": {
        "name": "Some Discord Server",
        "text_channels": {
            "924609730817704007": {
                "name": "c29tZSBkaXNjb3JkIHRleHQgY2hhbm5lbA==",
                "topic": "c29tZSB0b3BpYw==",
                "position": 22,
                "type": [
                    "text",
                    0
                ]
            }
        },
        "voice_channels": {
            "924609701646319618": {
                "name": "c29tZSBkaXNjb3JkIHZvaWNlIGNoYW5uZWw=",
                "position": 7,
                "type": [
                    "voice",
                    2
                ]
            }
        },
        "category": {
            "924609679668174868": {
                "name": "c29tZSBjYXRlZ29yeQ==",
                "position": 4
            }
        },
        "users": {
            "722023862497443861": {
                "name": "c29tZSBiYXNlNjQgbmFtZQ==",
                "discriminator": "0157",
                "avatar": "some avatar tag"
            }
        }
    }
}
```

# Documentation

The file `main.py` is the main file of this project. It uses `saver.py` and `storage.py` in order to work. In this file remains all the **discord.py** coding, including the encryption command and the decryption command. To work, it is required to have a token in the file `token.txt`.

The file `saver.py` contains some **json utilities** that allow us to backup the server before destroying it.

The file `storage.py` is the file that saves the backup using the **utilities** in `saver.py`.


# Thank you for reading this documentation

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=gnaboo&repo=DiscordRansom&theme=dark)](https://github.com/gnaboo/RSA)

