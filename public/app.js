document.addEventListener("DOMContentLoaded", () => {
  const isSecure = window.location.protocol === "https:";
  const statusBadge = document.getElementById("status-badge");
  const protocolLink = document.getElementById("protocol-link");
  const host = window.location.hostname || "localhost";

  if (isSecure) {
    statusBadge.textContent = "Secure (HTTPS)";
    statusBadge.className = "badge success";
    document.getElementById("header").style.borderBottom = "4px solid #4CAF50";
    protocolLink.textContent = "Open HTTP version";
    protocolLink.href = `http://${host}:3000`;
    document.body.classList.add("page-https");
  } else {
    statusBadge.textContent = "Unsecure (HTTP)";
    statusBadge.className = "badge danger";
    document.getElementById("header").style.borderBottom = "4px solid #f44336";
    protocolLink.textContent = "Open HTTPS version";
    protocolLink.href = `https://${host}:3443`;
    document.body.classList.add("page-http");
  }
});
