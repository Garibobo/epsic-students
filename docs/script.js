
document.addEventListener("DOMContentLoaded", () => {
  fetch("tree.json")
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("folder-tree");
      container.innerHTML = "";
      buildTree(data, container);
    })
    .finally(() => {
      document.getElementById("loader-overlay").style.display = "none";
    });

  document.getElementById("search").addEventListener("input", function() {
    const term = this.value.toLowerCase();
    document.querySelectorAll("#folder-tree li").forEach(li => {
      li.style.display = li.textContent.toLowerCase().includes(term) ? "" : "none";
    });
  });

  window.addEventListener("scroll", () => {
    document.getElementById("back-to-top").style.display = window.scrollY > 200 ? "block" : "none";
  });
});

function buildTree(nodes, parent) {
  const ul = document.createElement("ul");
  nodes.forEach(node => {
    const li = document.createElement("li");
    li.textContent = (node.icon || "") + " " + node.name;
    if (node.url) {
      const a = document.createElement("a");
      a.href = node.url;
      a.target = "_blank";
      a.textContent = node.icon + " " + node.name;
      li.textContent = "";
      li.appendChild(a);
    }
    if (node.children) {
      li.classList.add("folder");
      buildTree(node.children, li);
    } else {
      li.classList.add("file");
    }
    ul.appendChild(li);
  });
  parent.appendChild(ul);
}

function toggleQR() {
  document.getElementById("qr-code").classList.toggle("fullscreen");
}
function downloadQR() {
  const link = document.createElement("a");
  link.href = "qr-code.png";
  link.download = "qr-code.png";
  link.click();
}
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function toggleAll() {
  const folders = document.querySelectorAll("#folder-tree ul");
  folders.forEach(ul => {
    ul.style.display = ul.style.display === "none" ? "block" : "none";
  });
}
function setLanguage(lang) {
  alert("Langue changée en : " + lang);
}
