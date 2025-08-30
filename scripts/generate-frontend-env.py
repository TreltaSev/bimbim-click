"""
Generates the envfile used for the frontend.
"""
import sys
from typing import Any
sys.dont_write_bytecode = True 

from pathlib import Path

import yaml

def main():
    root = Path(__file__).parent.parent
    config_path = root / "config.yml"
    env_path = root / "packages/frontend/.env"

    if not config_path.exists():
        raise FileNotFoundError(f"No config file exists at: {config_path.resolve()}")

    with config_path.open() as f:
        config = yaml.safe_load(f)
    
    frontend: dict[str, Any] = config.get("frontend")
    
    out: list[str] = []
    list_stage = [[k.upper(), frontend[k]] for k in frontend]
    
    for key, value in list_stage:
        
        if isinstance(value, str):
            value = f"\"{value}\""
            
        out.append(f"{key}={value}\n")
        
    env_path.write_text("\n".join(out))


if __name__ == "__main__":
    main()
