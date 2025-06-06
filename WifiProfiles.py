import subprocess
import re
import json

def obtener_perfiles_wifi():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], capture_output=True)
    profiles = re.findall(r":\s(.*)", result.stdout)