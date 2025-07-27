from src import main
import os
from pathlib import Path
import sys


project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

def local_main():
    print("Hello from ai-docs-research!")


if __name__ == "__main__":
    main()
