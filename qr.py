import qrcode
from PIL import Image

# URL de tu perfil que quieras que se abra al escanear el QR
url = "https://github.com/javilopercoder" #Ejemplo

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear la imagen del QR
qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Cargar el logo de lo que quieras de fondo (asegúrate de tener un logo en PNG)
logo_path = "images/Github-Light.png"
logo = Image.open(logo_path)

# Redimensionar el logo para que se ajuste al centro del QR
logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)  # 1/4 del tamaño del QR
logo = logo.resize(logo_size, Image.LANCZOS)

# Posicionar el logo en el centro del QR
logo_position = (
    (qr_image.size[0] - logo.size[0]) // 2,
    (qr_image.size[1] - logo.size[1]) // 2,
)
qr_image.paste(logo, logo_position, mask=logo)

# Guardar el QR personalizado
qr_image.save("qr/Github_QR.png")
print("Código QR generado y guardado")