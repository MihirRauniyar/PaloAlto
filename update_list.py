import requests
import re

# Source URL of the torrent blocklist (RAW format)
SOURCE_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/torrent.txt"
OUTPUT_FILE = "torrent-urls.txt"

def extract_urls(text):
    urls = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue  # skip comments and blank lines
        # Clean URL-like entries only (skip IPs if needed)
        if re.match(r"^(https?://|www\.)", line) or "." in line:
            urls.append(line)
    return urls

def main():
    response = requests.get(SOURCE_URL)
    if response.status_code == 200:
        urls = extract_urls(response.text)
        with open(OUTPUT_FILE, "w") as f:
            for url in urls:
                f.write(url + "\n")
        print(f"{len(urls)} URLs saved to {OUTPUT_FILE}")
    else:
        print(f"Failed to fetch source. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
