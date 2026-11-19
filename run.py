"""FleetSense — Urban Mobility Pattern Clustering."""

import os
import subprocess
import sys

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host="127.0.0.1", port=port, reload=False)
