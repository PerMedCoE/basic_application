from permedcoe import invoker
from .main import invoke


def main():
    invoker(invoke)  # Does automatically the parameter parsing


if __name__ == "__main__":
    main()
