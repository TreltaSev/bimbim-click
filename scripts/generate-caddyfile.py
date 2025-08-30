"""
Generates the Caddyfile used for Caddy.
"""

from pathlib import Path
import yaml

def main():
    root = Path(__file__).parent.parent
    config_path = root / "config.yml"
    template_path = root / "packages/router/Caddyfile.template"
    caddyfile_path = template_path.parent / "Caddyfile"

    if not config_path.exists():
        raise FileNotFoundError(f"No config file exists at: {config_path.resolve()}")

    with config_path.open() as f:
        config = yaml.safe_load(f)

    domain = config.get("host")
    if not domain:
        raise KeyError("Missing 'host' in config.yml")

    template_content = template_path.read_text()
    caddyfile_content = template_content.replace("{host}", domain)
    caddyfile_path.write_text(caddyfile_content)

if __name__ == "__main__":
    main()
