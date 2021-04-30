import asyncio
from aiohttp import web
import aiosqlite
from datetime import datetime, tzinfo, timedelta

class simple_utc(tzinfo):
    def tzname(self,**kwargs):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)

DB_PATH="webmention-logger.sqlite"
MAX_CONTENT_LENGTH=65536
DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS webmentions (
    id integer primary key autoincrement,
    source text,
    target text,
    timestamp text,
    sender text
);
"""

async def handle(request):
    if request.content_length and request.content_length > MAX_CONTENT_LENGTH:
        return web.Response(text="body too large", status=400)
    
    if request.content_type != "application/x-www-form-urlencoded":
        return web.Response(text="expected application/x-www-form-urlencoded content-type", status=400)

    errors = []
    data = await request.post()
    if "source" not in data:
        errors.append("'source' field not found")
    if "target" not in data:
        errors.append("'target' field not found")
    
    # FIXME: add checks: target belongs to instance, source and sender is not blacklisted (+ optional whitelist mode)
    
    if errors:
        return web.Response(text='\n'.join(errors), status=400)

    async with aiosqlite.connect(DB_PATH) as db:
        values = {
            "source": data["source"],
            "target": data["target"],
            "timestamp": datetime.utcnow().replace(tzinfo=simple_utc()).isoformat(),
            "sender": request.forwarded or request.host
        }
        print(values)
        await db.execute(
            "INSERT INTO webmentions VALUES (NULL, :source, :target, :timestamp, :sender)", 
            values
        )
        await db.commit()
        return web.Response(status=201, text="Accepted for further processing")

async def init():
    app = web.Application()
    app.add_routes([web.post('/{path:.*}', handle)])
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(DB_SCHEMA)
        return app

if __name__ == '__main__':
    web.run_app(init(), host = '127.0.0.1', port = 1234)

