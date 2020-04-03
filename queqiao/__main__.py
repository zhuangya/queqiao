import sys
from pathlib import Path

from queqiao.queqiao import process

if __name__ == "__main__":
    luna_dict_file_path = Path(sys.argv[1])
    process(luna_dict_file_path)
