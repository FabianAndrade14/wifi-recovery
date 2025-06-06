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
def guardar_json(profiles):
    datos = {perfil: obtener_contraseña_wifi(perfil) for perfil in profiles}
    with open('wifi_passwords.json', 'w') as f:
        json.dump(datos, f, indent=4)
    return datos

def main():
    print("Obteniendo contraseñas Wifi guardadas...\n")
    profiles = obtener_perfiles_wifi()

    if not profiles:
        print("No se han encontrado perfiles guardados")
        return

    datos = guardar_json(profiles)

    print("Redes Wifi encontradas:")
    for perfil, password in datos.items():
        print(f"\nRed: {perfil}")
        print(f"\nContraseña: {password}")

    print("\nLos datos se han guardado en 'wifi_passwords.json'")

if __name__ == "__main__":
    main()
