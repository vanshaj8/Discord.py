import discord
from discord.ext.commands import Bot
from discord.ext import commands ,tasks
import youtube_dl
from discord.ext import commands
import asyncio
import time
import praw
import random
from random import choice


client=commands.Bot(command_prefix='!')


status=['Under Maintainance','IN PROGRESS','WORK MODE ON','Hustling','Bored','Creator :Vanshaj']
@client.event
async def on_ready():
	change_status.start()
	print('HELL YEAH')
	

@client.command(name='server',help='Displays Server details')
async def server(ctx):
	name=str(ctx.guild.name)
	description=str(ctx.guild.description)

	owner=str(ctx.guild.owner)
	id=str(ctx.guild.id)
	region=str(ctx.guild.region)
	memberCount=str(ctx.guild.member_count)


	icon=str(ctx.guild.icon_url)

	embed=discord.Embed(title=name+"Server Information",description=description,color=discord.Color.blue())
	embed.set_thumbnail(url=icon)
	embed.add_field(name="Owner",value=owner,inline=True)
	embed.add_field(name="Server ID",value=id,inline=True)
	embed.add_field(name="Region",value=region,inline=True)
	embed.add_field(name="Member Count",value=memberCount,inline=True)

	await ctx.send(embed=embed)

#Ping Command

@client.command(name='ping',help='Returns the ping')
async def ping(ctx):
	await ctx.send(f'**PONG!** latency:{round(client.latency*1000)}ms')


#Hello Command

@client.command(name='hello',help='Welcome To DEZIO Server')
async def hello(ctx):
	responses=['Hello Guys','Wassup?','Kaise hai Jnta','Aur bhai kaise hai?','Vansh OP ho jaye','Bhai kya haal chaal','Sab kaisa chal rha','Hello bhai ! Bandi ptva de bhai','Was hapennin?','Ghar par sab kaise']
	await ctx.send(choice(responses))


#DIE COMMAND

@client.command(name='die',help='Bot gets Deactviated')
async def die(ctx):
	responses=['Deactivate mat karo please','Marr gya bhai ','Time to say good bye','Bhai next time mat bulana','Time to go mars','Motherboard','See ya next time','acha chlta hoon','Chalo kal milte','bye bye guys']
	await ctx.send(choice(responses))



# Reddit PRAW LIBRARY

reddit=praw.Reddit(client_id="3UzM7zWmKN7XRg",client_secret="Km6OR_sKYNHJ6cnsaJEEJPlzN1Vomg",username="your username",password="your passowrd",user_agent="pythonpraw",check_for_async=False)

@client.command(name='meme',help='Displays Memes')
async def meme(ctx):
	subreddit=reddit.subreddit("memes")
	all_subs=[]

	top=subreddit.top(limit=50)

	for submission in top:
		all_subs.append(submission)
	
	random_sub=random.choice(all_subs)

	name=random_sub.title
	url=random_sub.url

	em=discord.Embed(title=name)
	em.set_image(url=url)

	await ctx.send(embed=em)


#NEWS COMMAND

@client.command(name='news',help='Displays News')
async def news(ctx):
	subreddit=reddit.subreddit("news")
	all_subs=[]

	top=subreddit.top(limit=50)

	for submission in top:
		all_subs.append(submission)

	random_sub=random.choice(all_subs)
	
	name=random_sub.title
	url=random_sub.url

	em=discord.Embed(title=name)
	em.set_image(url=url)

	await ctx.send(embed=em)



#Adult Commands

#@client.command(name='tharki',help='Displays explicit Content')
#async def tharki(ctx):
#	subreddit=reddit.subreddit("tharki")
#	all_subs=[]
#
#	top=subreddit.top(limit=50)
#
#	for submission in top:
#		all_subs.append(submission)
#
#	random_sub=random.choice(all_subs)
#	
#	name=random_sub.title
#	url=random_sub.url

#	em=discord.Embed(title=name)
#	em.set_image(url=url)

#	await ctx.send(embed=em)


@tasks.loop(seconds=20) # change the Status every 20 seconds
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))

client.run('Your Token')
