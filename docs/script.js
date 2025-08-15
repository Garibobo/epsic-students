function setLanguage(lang) {
  alert("Langue changée en : " + lang);
}

function toggleQR() {
  const qr = document.getElementById("qr-code");
  qr.classList.toggle("fullscreen");
}

function downloadQR() {
  const link = document.createElement("a");
  link.href = "qr-code.png";
  link.download = "qr-code.png";
  link.click();
}
