import os
import platform
import time


def run_startup():
    os_name = platform.system()
    cwd = os.path.abspath("./")
    os.system(f"cd {cwd}")
    os.system("python -m virtualenv venv")
    time.sleep(5)
    print("Waiting on venv to install...")
    if os_name == "Windows":
        while not os.path.exists("./venv/Scripts/activate.ps1"):
            time.sleep(5)
            print("still waiting...")
        print("Activating virtual environment.")
        os.system("venv/Scripts/activate")
    else:
        while not os.path.exists("./venv/bin/activate"):
            time.sleep(5)
            print("still waiting...")
        print("Activating virtual environment.")
        os.system("source venv/bin/activate")
    print("installing requirements")
    os.system("pip install -r requirements.txt")
    print("All files installed, ready to scrape!")


if __name__ == "__main__":
    run_startup()
