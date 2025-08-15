import qrcode
import os

site_url = "https://garibobo.github.io/epsic-students/"
qr = qrcode.make(site_url)

os.makedirs("docs", exist_ok=True)
qr.save("docs/qrcode_site.png")