
import uuid
import time
from pathlib import Path
from datetime import datetime, timezone

random_id = str(uuid.uuid4())
output_file = Path("/data/output.txt")

while True:
    timestamp = datetime.now(timezone.utc).isoformat()
    line = f"{timestamp}: {random_id}\n"

    output_file.write_text(line, encoding="utf-8")

    print(line, end="", flush=True)
    time.sleep(5)
