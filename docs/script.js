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
function createTree(container, data) {
  data.forEach(item => {
    const div = document.createElement("div");
    div.textContent = (item.icon || "") + " " + item.name;
    if (item.type === "folder") {
      div.style.fontWeight = "bold";
      container.appendChild(div);
      const sub = document.createElement("div");
      sub.style.marginLeft = "1rem";
      createTree(sub, item.children || []);
      container.appendChild(sub);
    } else if (item.type === "file") {
      const link = document.createElement("a");
      link.href = item.url;
      link.target = "_blank";
      link.textContent = (item.icon || "") + " " + item.name;
      container.appendChild(link);
      container.appendChild(document.createElement("br"));
    }
  });
}
fetch("tree.json")
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("folder-tree");
    createTree(container, data);
  });
