import time

tid = round(time.time() * 1000)

while True:
    if tid < round(time.time() * 1000) - 800:
        print("flytt på slangen")
        tid = round(time.time() * 1000)