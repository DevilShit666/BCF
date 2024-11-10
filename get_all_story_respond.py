import api
import json
import time

import info_bot

with open("story_respond_ids", "r") as story_ids_file:
    story_ids = story_ids_file.read().split("\n")

while True:
    try:
        with open("story_respond_queue", "r") as account_ids_file:
            account_ids = account_ids_file.read().split("\n")

        for udid in account_ids:
            if udid == "":
                continue

            level = 0
            for id in story_ids:
                while level == 0:
                    try:
                        level = api.story_respond(udid, id)
                    except Exception as e:
                        print(f"Ошибка при обработке {udid} и {id}: {e}")
                        time.sleep(1)

            info_bot.send_notify_level_up(udid, level, "???")
            account_ids.remove(udid)


        with open("story_respond_queue", "w") as account_ids_file:
            account_ids_file.write("\n".join(account_ids))

    except Exception as e:
        print(f"Общая ошибка: {e}")

    time.sleep(1)