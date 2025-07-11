import requests

SOURCE_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/main/torrent.txt"
OUT_FILE = "custom_torrent_urls.txt"

def fetch_blocklist(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse_urls(blocklist):
    urls = []
    for line in blocklist.splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        if line.startswith("0.0.0.0 "):
            domain = line.split()[1]
            urls.append(domain)
    return urls

def save_urls(urls, filename):
    with open(filename, "w") as f:
        for url in urls:
            f.write(url + "\n")

def main():
    blocklist = fetch_blocklist(SOURCE_URL)
    urls = parse_urls(blocklist)
    save_urls(urls, OUT_FILE)
    print(f"Saved {len(urls)} URLs to {OUT_FILE}")

if __name__ == "__main__":
    main()
