import subprocess
import re
import json

def obtener_perfiles_wifi():
    try:
        resultado = subprocess.run(
            ['netsh', 'wlan', 'show', 'profiles'],
            capture_output=True,
            text=True,
            check=True
        )
        perfiles = re.findall(r":\s(.*)", resultado.stdout)
        return [perfil.strip() for perfil in perfiles if perfil.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener perfiles WiFi: {e}")
        return []

def obtener_contraseña_wifi(perfil):
    try:
        resultado = subprocess.run(
            ['netsh', 'wlan', 'show', 'profile', f'name="{perfil}"', 'key=clear'],
            capture_output=True,
            text=True,
            check=True
        )
        contraseña = re.search(r"Contenido de la clave\s*:\s(.*)", resultado.stdout)
        return contraseña.group(1) if contraseña else "No encontrada"
    except Exception as e:
        return f"Error: {str(e)}"

def guardar_en_json(perfiles):
    datos = {perfil: obtener_contraseña_wifi(perfil) for perfil in perfiles}
    with open('wifi_passwords.json', 'w') as f:
        json.dump(datos, f, indent=4)
    return datos

def main():
    print("Obteniendo contraseñas Wifi guardadas...\n")
    profiles = obtener_perfiles_wifi()

    if not profiles:
        print("No se han encontrado perfiles guardados")
        return

    datos = guardar_en_json(profiles)

    print("Redes Wifi encontradas:")
    for perfil, password in datos.items():
        print(f"\nRed: {perfil}")
        print(f"\nContraseña: {password}")

    print("\nLos datos se han guardado en 'wifi_passwords.json'")

if __name__ == "__main__":
    main()
