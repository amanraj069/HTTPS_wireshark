# HTTP vs HTTPS Demo

This project is a demonstration web app that shows the difference between HTTP and HTTPS. It includes a simple login/signup UI and a request inspector to illustrate how data is transmitted over each protocol.

## What this demo shows

- HTTP traffic on `http://localhost:3000`
- HTTPS traffic on `https://localhost:3443`
- A login form and signup form that submit data to `/api/login` and `/api/signup`
- A request inspector that displays whether the current request is secure and whether the traffic is encrypted
- A secondary animated demo page at `/anim`
- Clear visual messaging showing that HTTP is unencrypted and HTTPS is encrypted

## Project structure

- `server.js` – Express server that serves the demo pages and API endpoints
- `public/` – static frontend files for the UI
- `public/anim.html` – animated demo page loaded at `/anim`
- `package.json` – project metadata and npm scripts
- `private.key`, `certificate.crt` – self-signed SSL certificate files (generated via npm script)

## Prerequisites

- Node.js v14 or higher
- npm

## Setup and run

1. Open a terminal in the `http` directory.
2. Install dependencies:

```bash
npm install
```

3. Generate a local self-signed certificate for HTTPS. This uses OpenSSL via the npm script to create `private.key` and `certificate.crt` for `localhost`:

```bash
npm run generate-cert
```

4. Start the demo server:

```bash
npm start
```

5. Open the demo in your browser:

- HTTP: `http://localhost:3000`
- HTTPS: `https://localhost:3443`

> When using HTTPS locally, your browser may show a self-signed certificate warning. Accept or proceed to the page to continue.

## Notes

- The HTTPS server only starts if `private.key` and `certificate.crt` exist.
- The demo uses in-memory storage for users, so all signups are temporary and reset when the server restarts.
- This project is for educational purposes only and does not use production authentication or secure storage.

## Scripts

- `npm install` – install project dependencies
- `npm run generate-cert` – create a self-signed SSL certificate for local HTTPS testing
- `npm start` – start the server with `nodemon`

## How it works

- `server.js` creates both an HTTP server and an HTTPS server using Express.
- Express serves the static demo UI from the `public/` folder and the additional animation page at `/anim`.
- API endpoints use JSON body parsing to accept login and signup requests.
- The HTTPS server loads `private.key` and `certificate.crt` from the project root.
- The app logs a warning message for HTTP requests and confirms encryption for HTTPS requests.

