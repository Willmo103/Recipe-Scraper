import os
import platform


def run_startup():
    os_name = platform.system()
    cwd = os.path.abspath("./")
    os.system(f"cd {cwd}")
    os.system("python -m virtualenv venv")
    if os_name == "Windows":
        os.system("venv/Scripts/activate")
    else:
        os.system("source venv/bin/activate")
    os.system("pip install -r requirements.txt")
    os.system("python ./app.py")


if __name__ == "__main__":
    run_startup()
