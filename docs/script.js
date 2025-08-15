
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

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.onscroll = function () {
  const btn = document.getElementById("back-to-top");
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    btn.style.display = "block";
  } else {
    btn.style.display = "none";
  }
};

window.onload = function () {
  setTimeout(() => {
    document.getElementById("loading-overlay").style.display = "none";
  }, 800);
};

function toggleAll() {
  const folders = document.querySelectorAll("#folder-tree details");
  const expand = !Array.from(folders).every(d => d.open);
  folders.forEach(d => d.open = expand);
}

function filterTree() {
  const input = document.getElementById("searchInput").value.toLowerCase();
  const items = document.querySelectorAll("#folder-tree li");
  items.forEach(item => {
    const text = item.textContent.toLowerCase();
    item.style.display = text.includes(input) ? "" : "none";
  });
}
