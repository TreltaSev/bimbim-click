import sys
sys.dont_write_bytecode = True

import yaml
from pathlib import Path

root: Path = Path(__file__).parent.parent
config: dict = yaml.load((root / 'config.yml').read_text(), Loader=yaml.FullLoader)

template_init_file = root / "packages/database/template.init.js"
init_file = root / "packages/database/init.js"

database_config = config["database"]
username = database_config["username"]
password = database_config["password"]

template_contents = template_init_file.read_text()
template_contents = template_contents.replace("{username}", username)
template_contents = template_contents.replace("{password}", password)

init_file.write_text(template_contents)