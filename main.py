import asyncio
from app.__main__ import main

loop = asyncio.new_event_loop()
loop.create_task(main())
loop.run_forever()
