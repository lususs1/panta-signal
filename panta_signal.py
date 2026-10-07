"""Read-only Panta discovery MVP. Python 3.11+, no dependencies.

Run: PANTA_API_BASE_URL=https://YOUR_HOST/api/v1 PANTA_API_KEY=... python panta_signal.py
Then open http://127.0.0.1:8080. Credentials never reach the browser.
"""
import json
import os
import re
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, parse_qs, urlencode, quote
from urllib.request import Request, urlopen, HTTPRedirectHandler, build_opener
from urllib.error import HTTPError, URLError

MAX_BYTES = 2_000_000

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None

def upstream_path(path, query):
    """Only explicit catalog GET routes can leave this server."""
    if path == '/api/markets':
        allowed = {'category', 'status', 'cursor', 'limit'}
        if set(query) - allowed:
            raise ValueError('Unsupported query')
        args = {k: v[0] for k, v in query.items() if len(v) == 1}
        if len(args) != len(query) or any(len(v) > 512 for v in args.values()):
            raise ValueError('Invalid query')
        limit = int(args.get('limit', '20'))
        if not 1 <= limit <= 50:
            raise ValueError('Limit must be between 1 and 50')
        args['limit'] = str(limit)
        return '/markets/?' + urlencode(args)
    match = re.fullmatch(r'/api/markets/([A-Za-z0-9_-]{1,128})', path)
    if match and match[1] not in {'create', 'buy', 'claim'} and not query:
        return '/markets/' + quote(match[1], safe='') + '/'
    raise ValueError('Route not allowed')

def validate(data, detail=False):
    if not isinstance(data, dict):
        raise ValueError('Invalid upstream object')
    rows = [data] if detail else data.get('items')
    if not isinstance(rows, list) or len(rows) > 50:
        raise ValueError('Invalid market list')
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get('marketId'), str):
            raise ValueError('Invalid market identifier')
        if not re.fullmatch(r'[A-Za-z0-9_-]{1,128}', row['marketId']):
            raise ValueError('Invalid market identifier')
        for field in ('title', 'category', 'phase', 'description'):
            if field in row and row[field] is not None and not isinstance(row[field], str):
                raise ValueError('Invalid text field')
    cursor = data.get('nextCursor')
    if not detail and cursor is not None and (not isinstance(cursor, str) or len(cursor) > 512):
        raise ValueError('Invalid pagination cursor')
    return data

HTML = r'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Panta Signal</title>
<style>body{margin:0;background:#101721;color:#e5edf6;font:16px system-ui}main{max-width:1000px;margin:auto;padding:32px 20px}h1{font-size:40px;margin-bottom:8px}p,small{color:#a8bacb}section,article{background:#1a2533;border:1px solid #35485d;border-radius:12px;padding:20px;margin:16px 0}input,select,button{font:inherit;padding:12px;border-radius:8px;border:1px solid #536a80;background:#101721;color:#fff;margin:4px}button{cursor:pointer;background:#236e71}button:disabled{opacity:.5}label{display:inline-block}#list{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}article{margin:0}pre{white-space:pre-wrap;overflow-wrap:anywhere}#status{padding:16px;border-left:3px solid #63c8bd}footer{padding:24px 0;color:#80cec5}</style>
<main><small>READ-ONLY MARKET INTELLIGENCE</small><h1>Panta Signal</h1><p>Find prediction markets. Inspect their source data without connecting a wallet.</p>
<section><label>Search loaded markets<br><input id="search" placeholder="Title or market ID"></label><label>Category<br><input id="category" placeholder="e.g. crypto"></label><label>Phase<br><select id="phase"><option value="">All</option>primary</option><option>secondary</option><option>resolved</option><option>cancelled</option></select></label><button id="load">Load markets</button></section>
<div id="status" role="status">No data loaded. A server-side Panta API key is required.</div><p id="summary"></p><div id="list"></div><button id="more" hidden>Load next page</button><section id="detail" hidden><h2 id="title"></h2><p id="description"></p><small id="provenance"></small><pre id="raw"></pre></section><footer>Powered by Panta</footer></main>
<script>
const $=id=>document.getElementById(id);let rows=[],cursor=null,query='',busy=false,observed=null,source=null;
function text(tag,value,parent){const el=document.createElement(tag);el.textContent=value;parent.append(el);return el}
function render(){const needle=$('search').value.toLowerCase();$('list').replaceChildren();const visible=rows.filter(m=>(m.title+' '+m.marketId).toLowerCase().includes(needle));$('summary').textContent=`${visible.length} shown / ${rows.length} loaded. Counts describe this loaded subset only.`;for(const m of visible){const card=document.createElement('article');text('h2',m.title||m.marketId,card);text('p',`${m.category||'Unknown category'} · ${m.phase||'Unknown phase'}`,card);text('small',`Active volume: ${m.volumeUsdc??'Unknown'} USDC`,card);const b=text('button','Inspect source',card);b.onclick=()=>detail(m.marketId);b.disabled=busy;$('list').append(card)}$('more').hidden=!cursor;}
async function request(path){const r=await fetch(path);const data=await r.json();if(!r.ok)throw Error(data.error||'Request failed');return data}
function lock(value){busy=value;$('load').disabled=value;$('more').disabled=value;render()}
async function load(append=false){if(busy)return;lock(true);$('status').textContent='Loading Panta data…';try{if(!append){rows=[];cursor=null;$('detail').hidden=true;query=new URLSearchParams({limit:'20',...($('category').value?{category:$('category').value}:{}),...($('phase').value?{status:$('phase').value}:{})}).toString()}const d=await request('/api/markets?'+query+(append?'&cursor='+encodeURIComponent(cursor):''));const seen=new Set(rows.map(m=>m.marketId));rows.push(...d.data.items.filter(m=>!seen.has(m.marketId)));cursor=d.data.nextCursor||null;observed=d.observedAt;source=d.sourcePath;$('status').textContent=`Panta response received ${observed}. This is retrieval time, not the market update time. No automatic refresh.`;}catch(e){cursor=null;$('status').textContent=e.message+' Displayed data, if any, is from an earlier successful response.';}finally{lock(false)}}
async function detail(id){if(busy)return;lock(true);$('detail').hidden=true;try{const d=await request('/api/markets/'+encodeURIComponent(id));$('title').textContent=d.data.title||id;$('description').textContent=d.data.description||'No description provided.';$('provenance').textContent=`Source: Panta ${d.sourcePath} · Retrieved: ${d.observedAt}`;$('raw').textContent=JSON.stringify(d.data,null,2);$('detail').hidden=false;}catch(e){$('status').textContent=e.message}finally{lock(false)}}
$('load').onclick=()=>load();$('more').onclick=()=>load(true);$('search').oninput=render;
</script></html>'''

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # Never log request parameters or upstream credentials.

    def send(self, status, value, content_type='application/json'):
        body = value.encode() if isinstance(value, str) else json.dumps(value).encode()
        self.send_response(status)
        self.send_header('Content-Type', content_type + '; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        self.send(405, {'error': 'Read-only service: GET only'})

    do_PUT = do_POST
    do_PATCH = do_POST
    do_DELETE = do_POST

    def do_GET(self):
        parsed = urlsplit(self.path)
        if parsed.path == '/':
            return self.send(200, HTML, 'text/html')
        try:
            path = upstream_path(parsed.path, parse_qs(parsed.query, keep_blank_values=True))
        except (ValueError, TypeError):
            return self.send(400, {'error': 'Invalid or unsupported catalog request'})
        base = os.environ.get('PANTA_API_BASE_URL', '').rstrip('/')
        key = os.environ.get('PANTA_API_KEY', '')
        config = urlsplit(base)
        if not key or config.scheme != 'https' or not config.hostname or config.username or config.password or config.query or config.fragment:
            return self.send(503, {'error': 'Configure PANTA_API_BASE_URL (HTTPS) and PANTA_API_KEY on the server. Live integration is not configured.'})
        try:
            req = Request(base + path, headers={'X-Api-Key': key, 'Accept': 'application/json'}, method='GET')
            with build_opener(NoRedirect()).open(req, timeout=10) as response:
                raw = response.read(MAX_BYTES + 1)
                if len(raw) > MAX_BYTES:
                    raise ValueError('Response too large')
                data = validate(json.loads(raw), parsed.path != '/api/markets')
            self.send(200, {'data': data, 'source': 'Panta API', 'sourcePath': path, 'observedAt': datetime.now(timezone.utc).isoformat()})
        except HTTPError as e:
            self.send(502, {'error': f'Panta returned HTTP {e.code}. No upstream error body is exposed.'})
        except (URLError, TimeoutError, ValueError, OSError):
            self.send(502, {'error': 'Panta unavailable or response failed validation. No synthetic data substituted.'})

if __name__ == '__main__':
    ThreadingHTTPServer(('127.0.0.1', int(os.environ.get('PORT', '8080'))), Handler).serve_forever()
