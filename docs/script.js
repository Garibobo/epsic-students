let treeData = [];

function loadTree() {
  fetch("tree.json")
    .then(res => res.json())
    .then(data => {
      treeData = data;
      renderTree(treeData, document.getElementById("folder-tree"));
      document.getElementById("loader-overlay").style.display = "none";
    });
}

function renderTree(data, container) {
  container.innerHTML = "";
  data.forEach(item => {
    const el = document.createElement("div");
    el.className = "tree-item";
    if (item.type === "folder") {
      el.innerHTML = `📁 <span class="folder-name">${item.name}</span>`;
      const childrenContainer = document.createElement("div");
      childrenContainer.style.marginLeft = "1rem";
      childrenContainer.style.display = "none";
      el.appendChild(childrenContainer);
      el.querySelector(".folder-name").onclick = () => {
        childrenContainer.style.display = childrenContainer.style.display === "none" ? "block" : "none";
      };
      renderTree(item.children, childrenContainer);
    } else {
      let icon = "📄";
      if (item.icon === "image") icon = "🖼️";
      if (item.icon === "doc") icon = "📑";
      el.innerHTML = `${icon} <a href="${item.url}" target="_blank">${item.name}</a>`;
    }
    container.appendChild(el);
  });
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

function setLanguage(lang) {
  fetch("lang.json")
    .then(res => res.json())
    .then(data => {
      document.querySelector("h1").textContent = data[lang]["title"];
      document.querySelector("#qr-section h2").textContent = data[lang]["qr"];
      document.querySelector("#navigation h2").textContent = data[lang]["nav"];
      document.querySelector("button[onclick*='downloadQR']").textContent = data[lang]["download"];
      document.querySelector("#search-input").placeholder = data[lang]["search"];
      document.querySelector("button[onclick*='toggleAll']").textContent = data[lang]["toggle"];
    });
}

function filterTree() {
  const query = document.getElementById("search-input").value.toLowerCase();
  const filtered = treeData.filter(item => JSON.stringify(item).toLowerCase().includes(query));
  renderTree(filtered, document.getElementById("folder-tree"));
}

function toggleAll() {
  document.querySelectorAll("#folder-tree div > div").forEach(el => {
    el.style.display = el.style.display === "none" ? "block" : "none";
  });
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}

window.onscroll = () => {
  document.getElementById("back-to-top").style.display = window.scrollY > 200 ? "block" : "none";
};

window.onload = loadTree;
