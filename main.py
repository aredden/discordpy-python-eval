from subprocess import run
import os
from discord import Client, Message
from dotenv import load_dotenv

load_dotenv()

client = Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    cont = str(message.content)

    if cont.startswith('eval python'):
        cont = cont.replace('eval python ',"")
        evaluated = run_python_eval_loop(cont)
        await message.channel.send("```py\n{0}\n```".format(evaluated))

def run_python_eval_loop(text):
    with open("runner.py", "r+") as f:
        data = f.read()
        f.seek(0)
        f.write(text)    
        f.truncate()
        f.close()
        
    resp = os.popen('python runner.py').read()

    return resp


token = os.getenv('DISCORD_TOKEN')
client.run(token)