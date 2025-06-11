import qrcode

bot_url = "http://<your-ec2-public-ip>:8501"  

qr = qrcode.make(bot_url)

qr.save("bot_qr_code.png")

print("✅ QR code generated successfully as 'bot_qr_code.png'")
