import api


for i in range(0, 1000):
    udid = "PCo2PXraDiqyUTW9BrV7yQ"
    id = "daily_tpet"
    status = api.story_respond(udid, id)
    if (status != "yes"):
        print(i)
        exit()