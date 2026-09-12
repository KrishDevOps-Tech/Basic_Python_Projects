# Remainder for Drink water !

import time
import win32com.client
from plyer import notification

# Setup Voice Engine (from pywin32)
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def play_voice_alert(remainder_count: int):
    try:
        print(f"Alert !! {remainder_count} playing voice remainder.")
        speaker.speak(
            "In this extreme hot season of Delhi, please keep your body hydrated Krishna Sir."
        )
    except Exception as e:
        print(f"Voice Alert Error: {e}")


def remainder_to_drink_water(interval_seconds: int):
    print(f"________This is a remainder for Hydration!!_________\n")
    print("------------press Ctrl + C to stop Remainder-------------")
    remainder_count = 1

    while True:
        time.sleep(interval_seconds)
        show_msg = "Time to Drink water!"  # yeh title hai msg ka.
        body_msg = (
            f"Remainder #{remainder_count}: Take a break, and drink a glass of water!"
        )

        try:
            notification.notify(
                title=show_msg,
                message=body_msg,
                app_name="Hydration Tracker",
                timeout=5,  # Pop-up stays for 5 seconds
            )
        except Exception as e:
            print(f"Notification Error: {e}")

        finally:
            play_voice_alert(remainder_count)
            remainder_count += 1


if __name__ == "__main__":
    # Testing ke liye 10 seconds set kiya hai (Real life me 3600 seconds = 1 hour rakh sakte hai).
    Interval = 10
    try:
        remainder_to_drink_water(Interval)
    except KeyboardInterrupt:
        speaker.speak("Water Remainder successfully stopped by You krishna sir . Stay Hydrated !")
