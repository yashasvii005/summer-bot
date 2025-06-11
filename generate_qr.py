import qrcode

bot_url = "https://summer-bot-ksugd9jrvwqllxqfbldkqz.streamlit.app/"

qr = qrcode.make(bot_url)

qr.save("summer_bot_qr.png")

print("✅ QR code generated successfully as 'summer_bot_qr.png'")
