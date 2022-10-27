import os


def run_startup():
    os.system("virtualenv venv")
    os.system("venv/bin/activate")
    os.system("pip install -r requirements.txt")


if __name__ == "__main__":
    run_startup()
