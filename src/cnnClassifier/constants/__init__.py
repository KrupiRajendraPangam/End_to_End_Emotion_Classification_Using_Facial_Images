from pathlib import Path

# This ensures paths are correct no matter where the code is run from
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent  # from constants to root
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"

print("CONFIG FILE:", CONFIG_FILE_PATH)
print("Exists?", CONFIG_FILE_PATH.exists())

from pathlib import Path

# CONFIG_FILE_PATH = Path("config\config.yaml")
# PARAMS_FILE_PATH = Path("params.yaml")
# print(CONFIG_FILE_PATH)
# print("Exists?", CONFIG_FILE_PATH.exists())