import aiohttp
import asyncio
from aioconsole import aprint
import requests

class DiscordToken():
    def __init__(self):
        with open('tokens.txt', 'r') as t:
            self.tokens : str = t.read().splitlines()
        with open('proxies.txt', 'r') as p:
            self.proxies : str = p.read().splitlines()
    def channel_send(self, channel_id : int = 0, message : str = None, numberofmsg : int = 1):
        tokens = self.tokens
        for token in tokens:
            for i in range(numberofmsg):
                url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
                data = {"content": message}
                header = {"authorization": token}
                r = requests.post(url, data=data, headers=header)
    def createdmchannel(self, user_id):
        tokens = self.tokens
        for token in tokens:
            data = {"recipient_id": user_id}
            headers = {"authorization": token}
    
            r = requests.post(f'https://discord.com/api/v9/users/@me/channels', json=data, headers=headers)
    
            channel_id = r.json()['id']
    
            return channel_id
    def user_send(self, user_id : int = 0, message : str = None, numberofmsg : int = 1):
        tokens = self.tokens
        for token in tokens:
            channel_id = self.createdmchannel(user_id)
            self.channel_send(channel_id, message, numberofmsg)
    async def invite_join(self, invite_code : str = None):
        code = invite_code
        tokens = self.tokens
        proxies = self.proxies
        if len(proxies) > 0:
            for token, proxy in zip(tokens, proxies):
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}, proxy=f"http://{proxy}") as resp:
                        if resp.status == 200:
                            return
                        elif resp.status == 429:
                            j = await resp.json()
                            await asyncio.sleep(j['retry_after'])
                        elif resp.status == 403:
                            return
                        else:
                            return
                    await asyncio.sleep(0.7)
        else:
            for token in tokens:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}) as resp:
                        if resp.status == 200:
                            return
                        elif resp.status == 429:
                            j = await resp.json()
                            await asyncio.sleep(j['retry_after'])
                        elif resp.status == 403:
                            return
                        else:
                            j = await resp.json()
                            await aprint(resp.status, j,)
                    await asyncio.sleep(0.7)