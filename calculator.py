import math
import discord
from discord.ext import commands
import random

client=commands.Bot(command_prefix='-',help_command=None)


def sub(x:float ,y: float): #Used for subtractiom
	return x-y

def add(x:float ,y: float): #used for Addition
	return x+y

def div(x:float ,y: float): #usef for division
	return x/y

def mul(x:float ,y: float): #used for multiplication
	return x*y

def rando(x:int ,y: int):
	return random.randint(x,y) #returns the random integer between these two arguments

def sqrt(x:float):
	return math.sqrt(x)


#All commands are over now


@client.command()
async def mathadd(ctx,x:float,y:float):
	res=add(x,y)
	await ctx.send(res)

@client.command()
async def mathsub(ctx,x:float,y:float):
	res=sub(x,y)
	await ctx.send(res)

@client.command()
async def mathdiv(ctx,x:float,y:float):
	res=div(x,y)
	await ctx.send(res)

@client.command()
async def mathmul(ctx,x:float,y:float):
	res=mul(x,y)
	await ctx.send(res)

@client.command()
async def mathrandom(ctx,x:float,y:float):
	res=rando(x,y)
	await ctx.send(res)

@client.command()
async def mathsqrt(ctx,x:float):
	res=sqrt(x)
	await ctx.send(res)

# End of Functions

@client.event
async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='Calculating'))
        print(f'{client.user.name} is online')


client.run("ODEzNTIxMjAyODk1MTI2NTQ4.YDQgqQ.r0pFPrxskn2Y0zwnSATpneT3KbQ")
