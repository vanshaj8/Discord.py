import discord

intents=discord.Intents().default()
intents.members=True
client=discord.Client(intents=intents)

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='Over This Server'))

@client.event
async def on_member_join(member):
	guild=client.get_guild("your id")
	channel=guild.get_channel("your channel id")
	await channel.send(f'Welcome to the server {member.mention}! :partying_face:')
	await member.send(f'Welcome to the {guild.name} server ,{member.name} ! :partying_face:')

@client.event
async def on_message(message):
	if message.content=='hi':
		await message.channel.send('!HELLO')

client.run("Your token")
