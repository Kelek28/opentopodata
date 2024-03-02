import webbrowser
import time

with open("test.txt", "r") as f:
    url_list = f.read().split("\n")

for i, url in enumerate(url_list):
    webbrowser.open_new_tab(url)
    if i % 100 == 0:
        time.sleep(5) # pause 5s every 100 it to avoid rate limiting.