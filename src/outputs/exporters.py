thonpython
import json
from pathlib import Path
import logging

class JSONExporter:
    def __init__(self, output_path: str):
        self.output_path = Path(output_path)

    def export(self, data: list):
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logging.error(f"Failed to write output: {e}")
            raise