# HTTP vs HTTPS Demo

A simple demonstration website to show the difference between HTTP and HTTPS protocols, with login and signup functionality.

## Features
- **Dual Protocol Support**: Run on both HTTP (port 3000) and HTTPS (port 3443)
- **Login & Signup Forms**: Simple authentication interface
- **Request Inspector**: See the data being sent in real-time
- **Visual Indicators**: Clear warnings about security levels
- **Comparison Table**: HTTP vs HTTPS feature comparison

## Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm

### Installation

1. Install dependencies:
npm install
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    console.log(`[LOGIN] Received over ${req.protocol}: email=${email}, password=${password}`);
    res.json({ success: true, message: 'Login successful' });
});

app.post('/api/signup', (req, res) => {
    const { email, password } = req.body;
    console.log(`[SIGNUP] Received over ${req.protocol}: email=${email}, password=${password}`);
    res.json({ success: true, message: 'Signup successful' });
});

const HTTP_PORT = 3000;
http.createServer(app).listen(HTTP_PORT, () => {
    console.log(` HTTP Server running on http://localhost:${HTTP_PORT}`);
    console.log(`     WARNING: Data sent over HTTP is NOT encrypted and visible in plain text!`);
});

const HTTPS_PORT = 3443;
try {
    const privateKey = fs.readFileSync('private.key', 'utf8');
    const certificate = fs.readFileSync('certificate.crt', 'utf8');
    const credentials = { key: privateKey, cert: certificate };
    
    https.createServer(credentials, app).listen(HTTPS_PORT, () => {
        console.log(` HTTPS Server running on https://localhost:${HTTPS_PORT}`);
        console.log(`    All data sent over HTTPS is encrypted and secure!`);
    });
} catch (error) {
    console.log(`\n Could not start HTTPS server: ${error.message}`);
    console.log(` Please run 'npm run generate-cert' to create the required SSL certificates.\n`);
}
# HTTPS_wireshark
