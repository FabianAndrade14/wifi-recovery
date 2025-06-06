import subprocess
import re
import json

def obtener_perfiles_wifi():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], capture_output=True)
    profiles = re.findall(r":\s(.*)", result.stdout)
    return [perfil.strip() for perfil in profiles if perfil.strip()]
def obtener_contraseña_wifi(perfil):
    try:
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'profile', perfil, 'key=clear'],
            capture_output=True, text=True
        )
        password = re.search(r"Contraseña\s*:\s(.*)", result.stdout)
        return password.group(1) if password else "No encontrada"
    except Exception as e:
        return f"Error: {str(e)}"