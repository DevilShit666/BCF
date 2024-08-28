import api
import json
import time

import info_bot

daily_ids_file = open("daily_ids", "r")
daily_ids = daily_ids_file.read().split("\n")
daily_ids_file.close()


while True:
    try:
        account_ids_file = open("daily", "r")
        account_ids = account_ids_file.read().split("\n")
        account_ids_file.close()
        for udid in account_ids:
            if (udid == ""):
                continue
            for id in daily_ids:
                level = 0
                while (level == 0):
                    level = api.story_respond(udid, id)
            info_bot.send_notify_level_up(udid, level, "???")
    except:
        print("ERROR???")
    time.sleep(86400)


