import os


def run_startup():
    cwd = os.path.abspath('./')
    os.systems(f"cd {cwd}")
    os.system("python -m virtualenv venv")
    os.system("venv/bin/activate")
    os.system("pip install -r requirements.txt")


if __name__ == "__main__":
    run_startup()
