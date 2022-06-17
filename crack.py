import os
import platform
import webbrowser
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/KAR-DATA')
except:pass
try:os.system('mkdir /sdcard/KAR-DATA/OK')
except:pass
try:os.system('mkdir /sdcard/KAR-DATA/CP')
except:pass
try:os.system('mkdir /sdcard/KAR-DATA/TAP-A2F')
except:pass
try:os.system('touch .prox.txt')
except:pass
if __name__ == "__main__":
        try:
                __import__("crack").login()
        except Exception as e:
                exit(str(e))
