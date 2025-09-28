from telethon import TelegramClient, events

api_id = 12345678 <--API_ID kalian sendiri
api_hash = "sdbfkgdskhfbgkdsbf" #<-- api_hash kalian sendiri
session_name = "testdoang aja" #<-- bebas isi apa aja

PROMO_MESSAGE = "ANJAY BISA EUY" #<-- bebas isi apa aja

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.out:
        return
    
    if event.is_group:
        await client.send_message(event.chat_id, PROMO_MESSAGE)

print("Userbot Jalan... Tekan Ctrl+C Untuk Stop")
client.start()
client.run_until_disconnected()
