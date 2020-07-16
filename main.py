import discord
import random
import os
import time

from discord import Member
from discord.ext import commands

client = commands.Bot(command_prefix='pont ')


@client.event
async def on_ready():
    print('Bot ready.')


@client.event
async def on_member_join(member):
    await member.send(f'{member} has joined!')


@client.event
async def on_member_remove(member):
    await member.send(f'{member} left. Good riddance!')


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def motivate(ctx):
    newf = open('A:/Code/Pont/motivation.txt', 'r+', 1)
    phrases = newf.readlines()

    await ctx.send(f'{random.choice(phrases)}')


@client.command()
async def calc(ctx, num1, op, num2):
    num1 = float(num1)
    num2 = float(num2)
    if op == '+':
        ans = int(num1 + num2)
    elif op == '-':
        ans = int(num1 - num2)
    elif op == '*':
        ans = int(num1 * num2)
    elif op == '/' and num2 == 0:
        ans = 'Cant divide by zero! It violates all practical and abstract mathematical properties.'
    elif op == '/':
        ans = float(num1 / num2)
    elif op == '%%':
        ans = int(num1 % num2)
    elif op == '%':
        ans = float((num1 / 100) * num2)

    await ctx.send(ans)


@client.command()
async def mg(ctx):
    pics = os.listdir('monster')
    with open('A:/Code/Pont/monster/' + random.choice(pics), 'rb') as fp:
        await ctx.send(file=discord.File(fp, 'A:/Code/Pont/monster/' + random.choice(pics)))


@client.command()
async def members(ctx):
    await ctx.send(f'Member Count: {ctx.guild.member_count}\n\nMembers: ')
    listmember = []

    x = ctx.guild.members

    for member in x:
        listmember.append(f"{member}")

    await ctx.send('```' + '\n'.join(map(str, listmember)) + '```')


def onmobile(user):
    return user.mobile_status


def ondesktop(user):
    return user.desktop_status


def onweb(user):
    return user.web_status


@client.command()
async def deepsearch(ctx, user: Member):
    listroles = user.roles
    allroles = []

    for role in listroles:
        new = str(role).split('name=')
        allroles.append(new)

    nroles = str(allroles)

    for item in nroles:
        item.replace('\'', '')

    fulllist = [f"Account Created: {user.created_at}\n", f"User ID: {user.id}\n",
                f"Connection Status:\n  Mobile: {onmobile(user)}\n  Desktop: {ondesktop(user)}\n  Web: {onweb(user)}\n",
                f"Joined server at: {user.joined_at}\n", f"Nickname: {user.nick}\n",
                f"Nitro (if applicable): {user.premium_since}\n", f"Roles: {nroles}\n"]

    await ctx.send("```fix\n" + '\n'.join(map(str, fulllist)) + "\n```")


@client.command()
async def psychic(ctx, question):
    answers = [
    "It is certain.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Yes.",
    "Reply hazy, try again.", 
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Doubt it."
    ]

    await ctx.send(random.choice(answers))

//OMITTED 