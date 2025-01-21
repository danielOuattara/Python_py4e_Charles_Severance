""" A simple web browser """

import string  # for removing punctuation
import urllib.error
import urllib.request


# ----- A simplest web browser

def web_browser(url):
    try:
        with urllib.request.urlopen(url) as file_handle:
            for line in file_handle:
                print(line.decode().strip())
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    print('\n')


# ----- Treat it Like a file


def web_browser_as_file(url):
    counts = {}
    try:
        with urllib.request.urlopen(url) as file_handle:
            for line in file_handle:
                line = line.decode().strip()
                # Split line into words, normalize and count them
                words = line.split()
                for word in words:
                    # Remove punctuation and convert to lowercase
                    word = word.strip(string.punctuation).lower()
                    counts[word] = counts.get(word, 0) + 1
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e}")
        return  # Exit function on error
    except Exception as e:
        print(f"Unexpected error: {e}")
        return  # Exit function on error

    # Print word counts
    print(f'Word counts for {url}:')
    for word, count in counts.items():
        print(f"{word}: {count}")
    print('\n')


# ----- Storing Web page


def web_browser_write_to_file(url, output_file):

    try:
        with urllib.request.urlopen(url) as file_handle:
            result = ""
            for line in file_handle:
                # Ignore decoding errors if any
                result += line.decode('utf-8', errors='ignore').strip()
            with open(output_file, "w", encoding='utf-8') as file:
                file.write(result)
            print(f"Successfully wrote content of {url} to {output_file}")
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # web_browser(url="http://data.pr4e.org/romeo.txt")
    # web_browser_as_file(url="http://data.pr4e.org/romeo.txt")
    web_browser_write_to_file(
        url="https://www.youtube.com/",  output_file="./result.html")


"""
Considerations for Improvement:
--------------------------------

1. HTML Parsing and Manipulation: If you plan to work extensively with HTML 
content (like extracting specific elements or attributes), consider using 
a library like BeautifulSoup (bs4) for more structured parsing and manipulation.


2. Efficiency: When handling large files or frequent requests, consider 
implementing optimizations such as streaming processing (read in chunks) rather 
than accumulating the entire content in memory.

3. Input Validation: Validate the URL input to ensure it conforms to expected 
formats and protocols before making the request.

4. Logging: For more detailed debugging or logging purposes, you might consider 
logging errors or specific actions within each function.

"""
