import requests

SOURCE_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/torrent.txt"
OUTPUT_FILE = "torrent-urls.txt"

def extract_urls(text):
    urls = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue  # skip comments and empty lines
        parts = line.split()
        if len(parts) == 2 and parts[0] in ("0.0.0.0", "127.0.0.1"):
            urls.append(parts[1])  # keep only the domain
        elif len(parts) == 1:
            urls.append(parts[0])
    return urls

def main():
    response = requests.get(SOURCE_URL)
    if response.status_code == 200:
        urls = extract_urls(response.text)
        with open(OUTPUT_FILE, "w") as f:
            for url in urls:
                f.write(url + "\n")
        print(f"{len(urls)} clean URLs saved to {OUTPUT_FILE}")
    else:
        print(f"Failed to fetch source. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
