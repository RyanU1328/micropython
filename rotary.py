from machine import Pin
from time import sleep

MASTER = 500
FIREFOX = 500
SPOTIFY = 500
GAMES = 500
DISCORD = 500
user = "PC"

MasterPin = [3, 4, 5]
FirefoxPin = [6, 7, 8]
SpotifyPin = [9, 10, 11]
GamesPin = [13, 14, 15]
DiscordPin = [18, 19, 20]
def volume_knobs():
    turn_sleep_time = 0.005

    volume_max = 1000

    red = Pin(2, Pin.OUT)

    step_pin_master = Pin(MasterPin[0], Pin.IN, Pin.PULL_UP)
    direction_pin_master = Pin(MasterPin[1], Pin.IN, Pin.PULL_UP)
    button_pin_master = Pin(MasterPin[2], Pin.IN, Pin.PULL_UP)

    step_pin_firefox = Pin(FirefoxPin[0], Pin.IN, Pin.PULL_UP)
    direction_pin_firefox = Pin(FirefoxPin[1], Pin.IN, Pin.PULL_UP)
    button_pin_firefox = Pin(FirefoxPin[2], Pin.IN, Pin.PULL_UP)

    step_pin_spotify = Pin(SpotifyPin[0], Pin.IN, Pin.PULL_UP)
    direction_pin_spotify = Pin(SpotifyPin[1], Pin.IN, Pin.PULL_UP)
    button_pin_spotify = Pin(SpotifyPin[2], Pin.IN, Pin.PULL_UP)

    step_pin_games = Pin(GamesPin[0], Pin.IN, Pin.PULL_UP)
    direction_pin_games = Pin(GamesPin[1], Pin.IN, Pin.PULL_UP)
    button_pin_games = Pin(GamesPin[2], Pin.IN, Pin.PULL_UP)

    step_pin_discord = Pin(DiscordPin[0], Pin.IN, Pin.PULL_UP)
    direction_pin_discord = Pin(DiscordPin[1], Pin.IN, Pin.PULL_UP)
    button_pin_discord = Pin(DiscordPin[2], Pin.IN, Pin.PULL_UP)

    user_button = Pin(16, Pin.IN, Pin.PULL_DOWN)

    global MASTER
    global SPOTIFY
    global FIREFOX
    global GAMES
    global DISCORD
    global user

    previous_value_master = True
    button_down_master = False
    previous_value_firefox = True
    button_down_firefox = True
    previous_value_spotify = True
    button_down_spotify = False
    previous_value_games = True
    button_down_games = False
    previous_value_discord = True
    button_down_discord = False



    tempValueMaster = 0
    tempValueSpotify = 0
    tempValueFirefox = 0
    tempValueGames = 0
    tempValueDiscord = 0

    while True:
        if user_button.value() == 1:
            if user == "PC":
                user = "LAPTOP"
                red.on()
                sleep(0.5)
                red.off()
            else:
                user = "PC"
                red.on()
                sleep(0.5)
                red.off()

        if previous_value_master != step_pin_master.value():
            if not step_pin_master.value():
                if not direction_pin_master.value():
                    print("turned left")
                    if MASTER == 1023:
                        MASTER = volume_max
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
                    elif MASTER > 0:
                        MASTER -= 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()

                else:
                    print("turned right")
                    if MASTER < volume_max:
                        MASTER += 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
                    if MASTER == volume_max:
                        MASTER = 1023

            previous_value_master = step_pin_master.value()

        if button_pin_master.value() == 0 and not button_down_master:
            print("button pushed")
            if MASTER > 0:
                tempValueMaster = MASTER
                MASTER = 0
            else:
                MASTER = tempValueMaster
                tempValueMaster = 0
            button_down_master = True
            red.on()
            sleep(0.5)
            red.off()
        if button_pin_master.value() == True and button_down_master:
            button_down_master = False


        if previous_value_firefox != step_pin_firefox.value():
            if not step_pin_firefox.value():
                if not direction_pin_firefox.value():
                    print("turned left")
                    if FIREFOX > 0:
                        FIREFOX -= 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
                else:
                    print("turned right")
                    if FIREFOX < volume_max:
                        FIREFOX += 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
            previous_value_firefox = step_pin_master.value()

        if button_pin_firefox.value() == 0 and not button_down_firefox:
            print("button pushed")
            if FIREFOX > 0:
                tempValueFirefox = FIREFOX
                FIREFOX = 0
            else:
                FIREFOX = tempValueFirefox
                tempValueFirefox = 0
            button_down_firefox = True
            red.on()
            sleep(0.5)
            red.off()
        if button_pin_firefox.value() == True and button_down_firefox:
            button_down_firefox = False


        if previous_value_spotify != step_pin_spotify.value():
            if not step_pin_spotify.value():
                if not direction_pin_spotify.value():
                    print("turned left")
                    if SPOTIFY > 0:
                        SPOTIFY -= 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
                else:
                    print("turned right")
                    if SPOTIFY < volume_max:
                        SPOTIFY += 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
            previous_value_spotify = step_pin_spotify.value()

        if button_pin_spotify.value() == False and not button_down_spotify:
            print("button pushed")
            if SPOTIFY > 0:
                tempValueSpotify = SPOTIFY
                SPOTIFY = 0
            else:
                SPOTIFY = tempValueSpotify
                tempValueSpotify = 0
            button_down_spotify = True
            red.on()
            sleep(0.5)
            red.off()
        if button_pin_spotify.value() == True and button_down_spotify:
            button_down_spotify = False



        if previous_value_games != step_pin_games.value():
            if not step_pin_games.value():
                if not direction_pin_games.value():
                    print("turned left")
                    if GAMES > 0:
                        GAMES -= 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
                else:
                    print("turned right")
                    if GAMES < volume_max:
                        GAMES += 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
            previous_value_games = step_pin_games.value()

        if button_pin_games.value() == 0 and not button_down_games:
            print("button pushed")
            if GAMES > 0:
                tempValueGames = GAMES
                GAMES = 0
            else:
                GAMES = tempValueGames
                tempValueGames = 0
            button_down_games = True
            red.on()
            sleep(0.5)
            red.off()
        if button_pin_games.value() == True and button_down_games:
            button_down_games = False


        if previous_value_discord != step_pin_discord.value():
            if not step_pin_discord.value():
                if not direction_pin_discord.value():
                    print("turned left")
                    if DISCORD > 0:
                        DISCORD -= 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
                else:
                    print("turned right")
                    if DISCORD < volume_max:
                        DISCORD += 50
                        red.on()
                        sleep(turn_sleep_time)
                        red.off()
            previous_value_discord = step_pin_discord.value()

        if button_pin_discord.value() == 0 and not button_down_discord:
            print("button pushed")
            if DISCORD > 0:
                tempValueDiscord = DISCORD
                DISCORD = 0
            else:
                DISCORD = tempValueDiscord
                tempValueDiscord = 0
            button_down_discord = True
            red.on()
            sleep(0.5)
            red.off()
        if button_pin_discord.value() == True and button_down_discord:
            button_down_discord = False