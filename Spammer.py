import pyautogui
import time

print("""

░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
""")

print("[1] Discord Spammer")
print("[2] Youtube Live Spammer")
print("[3] Minecraft Spammer(Java版推奨)")
select = input(">")

if select == "1":
	print("Discord Spammerでは1秒間隔でメッセージが送信されます。")
	message = input("スパムメッセージ: ")
	print("Discordでスパムしたいチャンネルを開いてください。")
	print("準備ができたらEnterキーを教えてください。")
	input()
	print("10秒以内にDiscordのウィンドウを選択してください。")
	print("自動的にスパムが開始されます。")
	time.sleep(10)
	while True:
		pyautogui.write(f"{message}")
		pyautogui.press("enter")
		time.sleep(1)
elif select == "2":
	print("Youtube Live Spammerでは5秒間隔でメッセージが送信されます。")
	message = input("スパムメッセージ: ")
	print("スパムしたいLiveを開いてください。")
	print("準備ができたらEnterキーを教えてください。")
	input()
	print("10秒以内にブラウザのウィンドウを選択してください。")
	print("自動的にスパムが開始されます。")
	time.sleep(10)
	while True:
		pyautogui.write(f"{message}")
		pyautogui.press("enter")
		time.sleep(5)
elif select == "3":
	print("Minecraft Spammerでは5秒間隔でメッセージが送信されます。")
	message = input("スパムメッセージ: ")
	print("スパムしたいサーバーに入った状態にしてください。")
	print("準備ができたらEnterキーを教えてください。")
	input()
	print("10秒以内にMinecraftを選択してください。")
	print("自動的にスパムが開始されます。")
	time.sleep(10)
	while True:
		pyautogui.press("t")
		time.sleep(0.1)
		pyautogui.write(f"{message}")
		pyautogui.press("enter")
else:
	print("「1」「2」「3」のどれかを選択してください。")
	print("10秒後にプログラムが終了します。")
	time.sleep(10)
	exit()