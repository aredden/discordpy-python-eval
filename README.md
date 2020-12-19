# discordpy-python-eval
Example discord.py python eval bot

This is a simple example discord.py bot that will evaluate python based on discord message content. It reads message content, then prints the message content into the runner.py file. Then uses `os.popen` to run the file as python on the host machine. Once the file has run, the stdout will be sent back to the discord channel that the python message originated from.

This project requires a `.env` file located in the same directory as the main.py file. It should contain your discord token like this:
```
# Without curly braces
DISCORD_TOKEN={Your token}
```
