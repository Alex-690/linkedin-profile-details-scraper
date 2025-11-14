thonpython
import json
import logging
from pathlib import Path
from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_input_urls(file_path: str):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    input_file = "data/inputs.sample.txt"
    output_file = "data/sample.json"

    logging.info("Loading input URLs...")
    urls = load_input_urls(input_file)

    parser = LinkedInParser()

    results = []
    for url in urls:
        logging.info(f"Processing: {url}")
        data = parser.parse_profile(url)
        results.append(data)

    exporter = JSONExporter(output_file)
    exporter.export(results)

    logging.info(f"Completed. Output written to {output_file}")

if __name__ == "__main__":
    main()