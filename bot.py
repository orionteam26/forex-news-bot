import os
import requests
from datetime import datetime

WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

message = f"📰 Forex News Bot attivo - {datetime.now()}"

requests.post(WEBHOOK, json={
    "content": message
})
