"""Local desktop launcher for JobNchill."""
import os
import threading
import webbrowser

import uvicorn


def _open_browser() -> None:
    webbrowser.open("http://127.0.0.1:8000")


def main() -> None:
    os.environ.setdefault("APP_MODE", "app")
    threading.Timer(1.5, _open_browser).start()
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="info")


if __name__ == "__main__":
    main()
