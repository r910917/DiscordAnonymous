import discord
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Bot 已上線：{bot.user}')

@app.route('/post-message', methods=['POST'])
def post_message():
    data = request.json
    channel_id = int(data['1308829015116615760'])
    message_content = data['content'] 
    
    channel = bot.get_channel(channel_id)
    if channel:
        bot.loop.create_task(channel.send(f"匿名訊息：{message_content}"))
        return jsonify({'status': 'Message sent!'})
    return jsonify({'status': 'Channel not found!'}), 404

def run_flask():
    app.run(host='0.0.0.0', port=5000)

threading.Thread(target=run_flask).start()
bot.run('MTMwODgyMzE5OTQ3OTM2OTcyOQ.G9LMLU.XiD2YKmcncfXtfnlstW0ojd3aEvLdDm9naHYdA')

