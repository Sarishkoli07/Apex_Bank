"""
Bank Management System Launcher
Starts the Uvicorn ASGI server hosting FastAPI and the rich frontend client.
"""
import uvicorn
import os
import sys

# Ensure backend directory is in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

if __name__ == "__main__":
    print("=" * 65)
    print("   APEX INTERNATIONAL BANK - OBJECT-ORIENTED MANAGEMENT SYSTEM   ")
    print("=" * 65)
    print(" Starting FastAPI server at: http://127.0.0.1:8000")
    print(" Serving Banking Portal & Interactive OOP Inspector...")
    print("=" * 65)
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)
