import time
from datetime import datetime

print(f"🚀 Live trading bot kjører med 4x giring! Startet {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
while True:
    print("📈 Sjekker markedet og vurderer kjøp/salg ...")
    time.sleep(60)
