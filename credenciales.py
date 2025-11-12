# mapear_varias_ips.py
import subprocess

# Lista de IPs a las que quieres "autenticar" (añade las que necesites)
ips = [
    "192.168.1.131",
    "192.168.1.132",
    "192.168.1.133",
    "192.168.1.134",
    "192.168.1.135",
    "192.168.1.136",
    "192.168.1.137",
    #"192.168.1.139", difefente
    "192.168.1.120",
    "192.168.1.122",
    "192.168.1.156",
    "192.168.1.159",
    "192.168.1.160",
    "192.168.1.164",
    "192.168.1.167",
    "192.168.1.168",
    "192.168.1.106",
    "192.168.1.114",
    "192.168.1.118",
    "192.168.1.140",
    "192.168.1.165",
    "192.168.1.205"
]


username = "monitor"
password = "monitor"
share_name = "IPC$"  # hace que se conecte al pc directamente sin necesidad de un recurso compartido específico

results = []

for ip in ips:
    resource = f"\\\\{ip}\\{share_name}"

    # Intentamos borrar una conexión previa hacia ese recurso (evita errores 1219/conflictos)
    subprocess.run(["net", "use", resource, "/delete"], capture_output=True, text=True)

    # Construimos el comando (pasamos la contraseña explícita como segundo argumento)
    cmd = ["net", "use", resource, password, f"/user:{username}", "/persistent:yes"]

    # Por seguridad no mostramos la contraseña en el log, imprimimos sólo recurso y usuario
    print(f"\nEjecutando: net use {resource} /user:{username} /persistent:yes ...")

    res = subprocess.run(cmd, capture_output=True, text=True)
    rc = res.returncode

    if rc == 0:
        print(f"[OK] {ip}")
        results.append((ip, "OK", res.stdout.strip() or res.stderr.strip()))
    else:
        # mostramos mensajes útiles para depurar
        stdout = res.stdout.strip()
        stderr = res.stderr.strip()
        print(f"[ERROR] {ip} -> rc={rc}")
        if stdout:
            print("STDOUT:", stdout)
        if stderr:
            print("STDERR:", stderr)
        results.append((ip, f"ERROR rc={rc}", (stdout + "\n" + stderr).strip()))

# Informe final sencillo
print("\n--- Resumen ---")
for ip, status, msg in results:
    print(f"{ip}: {status}")

input("\nPresiona Enter para finalizar...")

