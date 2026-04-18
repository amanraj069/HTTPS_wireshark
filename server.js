const express = require("express");
const https = require("https");
const http = require("http");
const fs = require("fs");
const path = require("path");
const bodyParser = require("body-parser");

const app = express();

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

// Store for demo users (in-memory)
const users = {};

// Routes
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.get("/anim", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "anim.html"));
});

app.post("/api/signup", (req, res) => {
  const { email, password, username } = req.body;

  if (users[email]) {
    return res.status(400).json({ error: "Email already exists" });
  }

  users[email] = { username, password, email };

  res.json({
    success: true,
    message: "Signup successful!",
    user: { email, username },
  });
});

app.post("/api/login", (req, res) => {
  const { email, password } = req.body;

  if (!users[email] || users[email].password !== password) {
    return res.status(401).json({ error: "Invalid credentials" });
  }

  res.json({
    success: true,
    message: "Login successful!",
    user: { email, username: users[email].username },
  });
});

// Get request details for demo
app.get("/api/request-info", (req, res) => {
  const protocol = req.protocol.toUpperCase();
  const secure = req.secure;

  res.json({
    protocol,
    secure,
    encrypted: secure,
    message: secure ? "Data is ENCRYPTED " : "Data is PLAIN TEXT ",
  });
});

// HTTP Server
const httpServer = http.createServer(app);

// HTTPS Server
let httpsServer;
const certPath = path.join(__dirname, "certificate.crt");
const keyPath = path.join(__dirname, "private.key");

if (fs.existsSync(certPath) && fs.existsSync(keyPath)) {
  const options = {
    cert: fs.readFileSync(certPath),
    key: fs.readFileSync(keyPath),
  };
  httpsServer = https.createServer(options, app);
}

// Start servers
const HTTP_PORT = 3000;
const HTTPS_PORT = 3443;

httpServer.listen(HTTP_PORT, () => {
  console.log(` HTTP Server running on http://localhost:${HTTP_PORT}`);
  console.log(
    `     WARNING: Data sent over HTTP is NOT encrypted and visible in plain text!`,
  );
});

if (httpsServer) {
  httpsServer.listen(HTTPS_PORT, () => {
    console.log(` HTTPS Server running on https://localhost:${HTTPS_PORT}`);
    console.log(`    All data sent over HTTPS is encrypted and secure!`);
  });
} else {
  console.warn("  SSL certificates not found. Run: npm run generate-cert");
}

console.log("\nDemo Instructions:");
console.log("1. Test with HTTP: http://localhost:3000");
console.log(
  "2. Test with HTTPS: https://localhost:3443 (accept the self-signed certificate warning)",
);
console.log("3. Open DevTools (F12) → Network tab to see the request data");
console.log("4. For HTTP, you'll see the plain text password in the request");
console.log("5. For HTTPS, the data is encrypted in transit\n");
