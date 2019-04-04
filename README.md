# Chris Hansen
Deletes NSFW images in Discord chats and mentions the offending user.

## Requirements
* Python
* A pixlab API key (https://pixlab.io/dashboard)
* A Discord bot token (https://discordapp.com/developers/docs/intro)
* discord.py, asyncio, json, requests


## Usage
*1. Download nsfw.py and install its requirements. Replace 
```
key = 'API-KEY'
```
with your own API key.
*2. Create a Discord Developer account: https://discordapp.com/developers/docs/intro
*3. Create an application at https://discordapp.com/developers/applications/
*4. Create a bot for said application in the bots section of your application's settings.
*5. Copy the bot's token.
*6. Replace CLIENT-TOKEN in nsfw.py with your bot's token. For example:
```
client.run('CLIENT-TOKEN')
client.run('NTYxMjkNTANjExODAMjU.XKAVw.VS')
```
*7. Go to the OAuth2 section of your bot's application settings.
*8. Do this:
[Example](https://ibb.co/bzc6xTy)

*9. Copy the link below scope and add bot to your server.
*10. Run nsfw.py
