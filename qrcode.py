import qrcode
from PIL import Image

while True:
    print("\n1. Generar QR\n2. Salir")
    op = input("> ")
    if op == "2": break
    elif op == "1":
        data = input("Texto/URL: ")
        archivo = input("Archivo (ej: qr.png): ")
        box = int(input("Tamaño (ej: 10): "))
        fill = input("Color QR (default black): ") or "black"
        back = input("Color fondo (default white): ") or "white"
        qr = qrcode.QRCode(version=1, box_size=box, border=5)
        qr.add_data(data); qr.make(fit=True)
        img = qr.make_image(fill_color=fill, back_color=back)
        img.save(archivo); img.show(); print(f"QR guardado como {archivo}")
    else: print("Opción inválida")
