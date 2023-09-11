import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]*src=["\'](https?://(?:www\.)?youtube\.com/embed/([^"\']*))["\'][^>]*>'

    # Search for the pattern in the input HTML
    match = re.search(pattern, s)

    if match:
        embed_url = match.group(1)
        short_url = f"https://youtu.be/{embed_url.split('/')[-1]}"
        return short_url
    else:
        return None


if __name__ == "__main__":
    main()
