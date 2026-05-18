import json

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template

app = FastAPI()

# Integrated 2026 Odoo-Python-PostgreSQL Matrix
ODOO_DATA = {
    "19.0 (Stable)": {
        "python": "3.11, 3.12",
        "postgres": "17.x",
        "lifecycle": "Current Stable",
        "link": "https://www.odoo.com/documentation/19.0/"
    },
    "18.0 (LTS)": {
        "python": "3.11, 3.12",
        "postgres": "16.x, 17.x",
        "lifecycle": "Long Term Support",
        "link": "https://www.odoo.com/documentation/18.0/"
    },
    "17.0": {
        "python": "3.10, 3.11",
        "postgres": "15.x, 16.x",
        "lifecycle": "Supported",
        "link": "https://www.odoo.com/documentation/17.0/"
    },
    "16.0": {
        "python": "3.8, 3.9, 3.10",
        "postgres": "13.x, 14.x, 15.x",
        "lifecycle": "Supported",
        "link": "https://www.odoo.com/documentation/16.0/"
    },
    "10.0 (Legacy)": {
        "python": "2.7",
        "postgres": "9.4, 9.5, 9.6",
        "lifecycle": "End of Life",
        "link": "https://www.odoo.com/documentation/10.0/"
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DB Architecture | Environment Matrix</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
    </style>
</head>
<body class="text-slate-800">
    <nav class="bg-[#1e293b] text-white py-4 px-10 flex justify-between items-center border-b border-indigo-500/30">
        <div class="flex items-center space-x-3">
            <div class="w-2 h-6 bg-indigo-500 rounded"></div>
            <span class="text-lg font-semibold tracking-tight uppercase">Stack Configurator</span>
        </div>
        <div class="text-[10px] border border-slate-700 px-3 py-1 rounded bg-slate-800/50">REL: 2026.Q2</div>
    </nav>

    <main class="max-w-6xl mx-auto mt-12 px-8">
        <div class="grid grid-cols-12 gap-10">
            <!-- Left: Inputs -->
            <div class="col-span-4">
                <div class="bg-white border border-slate-200 p-6 rounded-sm shadow-sm mb-6">
                    <h3 class="text-xs font-bold text-slate-400 uppercase mb-5 tracking-widest">Version Control</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-[10px] font-bold text-slate-500 mb-1">TARGET RELEASE</label>
                            <select id="odooVer" onchange="refresh()" class="w-full bg-slate-50 border border-slate-300 text-sm rounded-sm p-2 outline-none focus:border-indigo-500 transition-colors">
                                {% for v in versions %}
                                <option value="{{ v }}">{{ v }}</option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>
                </div>

                <div class="text-[11px] text-slate-500 bg-slate-100 p-4 border-l-2 border-slate-300 italic">
                    Note: For migrations involving cataloging systems, ensure PostgreSQL 17 parameter tuning is applied for heavy indexing.
                </div>
            </div>

            <!-- Right: Specs -->
            <div class="col-span-8">
                <div class="bg-white border border-slate-200 rounded-sm shadow-sm overflow-hidden">
                    <div class="px-8 py-6 flex justify-between items-end border-b border-slate-100">
                        <div>
                            <h2 id="mainTitle" class="text-2xl font-bold text-slate-900 leading-none">Odoo Specs</h2>
                            <p class="text-sm text-slate-500 mt-2">Verified compatibility for enterprise deployment.</p>
                        </div>
                        <span id="status" class="text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-tighter"></span>
                    </div>

                    <div class="p-8">
                        <div class="grid grid-cols-2 gap-8 mb-10">
                            <div class="space-y-1">
                                <span class="text-[10px] font-bold text-indigo-500 uppercase tracking-widest">Recommended Python</span>
                                <div id="pyVer" class="text-2xl font-semibold text-slate-800"></div>
                            </div>
                            <div class="space-y-1">
                                <span class="text-[10px] font-bold text-emerald-600 uppercase tracking-widest">PostgreSQL Engine</span>
                                <div id="pgVer" class="text-2xl font-semibold text-slate-800"></div>
                            </div>
                        </div>

                        <div class="space-y-8">
                            <section>
                                <h4 class="text-[10px] font-bold text-slate-400 uppercase mb-3">Modern Initialization (UV)</h4>
                                <div class="bg-slate-50 border border-slate-200 p-4 font-mono text-sm text-slate-700 flex justify-between items-center group">
                                    <code>uv venv .venv --python <span class="pyTarget"></span></code>
                                    <span class="text-[10px] text-slate-300 uppercase opacity-0 group-hover:opacity-100 transition-opacity">Copy</span>
                                </div>
                            </section>

                            <section>
                                <h4 class="text-[10px] font-bold text-slate-400 uppercase mb-3">Legacy Initialization (VENV)</h4>
                                <div class="bg-slate-50 border border-slate-200 p-4 font-mono text-sm text-slate-700">
                                    <code>python<span class="pyTarget"></span> -m venv odoo-env</code>
                                </div>
                            </section>
                        </div>

                        <div class="mt-12 flex justify-between items-center">
                            <a id="extLink" href="#" target="_blank" class="text-xs font-bold text-indigo-600 hover:text-indigo-800 uppercase tracking-widest border-b-2 border-indigo-100 pb-1">Documentation Portal</a>
                            <span class="text-[10px] text-slate-400">Database Administration & Architecture Platform</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script>
        const data = {{ data_json | safe }};
        function refresh() {
            const v = document.getElementById('odooVer').value;
            const item = data[v];
            const pyLead = item.python.split(',')[0].trim();

            document.getElementById('mainTitle').innerText = "Odoo " + v.split(' ')[0];
            document.getElementById('pyVer').innerText = item.python;
            document.getElementById('pgVer').innerText = item.postgres;
            document.getElementById('extLink').href = item.link;

            document.querySelectorAll('.pyTarget').forEach(t => t.innerText = pyLead);

            const status = document.getElementById('status');
            status.innerText = item.lifecycle;

            // Contextual Logic
            const lifecycle = item.lifecycle.toLowerCase();
            if(lifecycle.includes('stable')) {
                status.className = "text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-tighter bg-emerald-50 text-emerald-700 border border-emerald-200";
            } else if(lifecycle.includes('end of life')) {
                status.className = "text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-tighter bg-rose-50 text-rose-700 border border-rose-200";
            } else {
                status.className = "text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-tighter bg-indigo-50 text-indigo-700 border border-indigo-200";
            }
        }
        refresh();
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def index():
    template = Template(HTML_TEMPLATE)
    return template.render(versions=list(ODOO_DATA.keys()), data_json=json.dumps(ODOO_DATA))


if __name__ == "__main__":
    # Ensure standard local access
    uvicorn.run(app, host="127.0.0.1", port=8000)