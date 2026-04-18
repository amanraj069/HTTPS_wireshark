import sys

with open('latest.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure emojis are gone
html = html.replace('✅', '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-4 h-4 text-emerald-600 inline"><path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12.75l6 6 9-13.5" /></svg>')

# Replace CLIENT NODE
client_str = "{/* CLIENT NODE */}"
client_rep = """{/* CLIENT NODE */}
{mode === 'https' && (
    <div className="absolute -bottom-16 w-full flex justify-center pointer-events-none z-0">
        <span className="text-[10px] sm:text-xs text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-200 mt-1 whitespace-nowrap shadow-sm font-semibold flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-3 h-3"><path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m6.75 12l-3-3m0 0l-3 3m3-3v6m-1.5-15H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" /></svg> Trusted CAs
        </span>
    </div>
)}
"""

# Replace SERVER NODE
server_str = "{/* SERVER NODE */}"
server_rep = """{/* SERVER NODE */}
{['encrypt', 'https'].includes(mode) && (
    <div className="absolute -bottom-24 w-full flex flex-col items-center justify-center pointer-events-none z-0 gap-1.5">
        <span className="text-[10px] sm:text-xs text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 mt-1 whitespace-nowrap shadow-sm font-semibold flex items-center gap-1 shadow-sm">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-3 h-3"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" /></svg> Public Key
        </span>
        <span className="text-[10px] sm:text-xs text-teal-700 bg-teal-50 px-2 py-0.5 rounded border border-teal-200 whitespace-nowrap shadow-sm font-semibold flex items-center gap-1 shadow-sm">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-3 h-3"><path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" /></svg> Private Key
        </span>
        {mode === 'https' && (
            <span className="text-[10px] sm:text-xs text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-200 whitespace-nowrap shadow-sm font-semibold flex items-center gap-1 shadow-sm">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-3 h-3"><path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m6.75 12l-3-3m0 0l-3 3m3-3v6m-1.5-15H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" /></svg> CA Signed
            </span>
        )}
    </div>
)}
"""

# Replace HACKER NODE
hacker_str1 = "<!-- HACKER NODE -->"
hacker_str2 = "{/* HACKER NODE */}"
hacker_rep = """{/* HACKER NODE */}
{['encrypt', 'https'].includes(mode) && (
    <div className="absolute -bottom-24 w-full flex flex-col items-center justify-center pointer-events-none z-0 gap-1.5">
        <span className="text-[10px] sm:text-xs text-purple-700 bg-purple-50 px-1.5 py-0.5 rounded border border-purple-200 mt-1 whitespace-nowrap shadow-sm font-semibold flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-3 h-3"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" /></svg> Fake PubKey
        </span>
        <span className="text-[10px] sm:text-xs text-fuchsia-700 bg-fuchsia-50 px-1.5 py-0.5 rounded border border-fuchsia-200 whitespace-nowrap shadow-sm font-semibold flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-3 h-3"><path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" /></svg> Fake PrivKey
        </span>
    </div>
)}
"""

html = html.replace(client_str, client_rep)
html = html.replace(server_str, server_rep)
if hacker_str1 in html:
    html = html.replace(hacker_str1, hacker_rep + "\n<!-- HACKER NODE -->")
elif hacker_str2 in html:
    html = html.replace(hacker_str2, hacker_rep + "\n{/* HACKER NODE */}")

with open('http/public/anim.html', 'w', encoding='utf-8') as f:
    f.write(html)
