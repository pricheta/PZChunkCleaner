import sys
import subprocess


def run(cmd, use_line_breaks=True):
    print(f"▶ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

    if use_line_breaks:
        print("\n")


def format():
    run("black .")


def typecheck():
    run("mypy .")


def test():
    run("pytest .")


def clear():
    run("cls", use_line_breaks=False)


def check():
    format()
    typecheck()
    test()


if __name__ == "__main__":
    clear()
    task = sys.argv[1] if len(sys.argv) > 1 else "check"
    globals()[task]()
