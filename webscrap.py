import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=10):
    base_url = "http://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    params = {
        "q": query,
        "num": num_results
    }

    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code != 200:
        print("Failed to retrieve results")
        return []

    # Debugging: Print the response text to verify its content
    print("Response Status Code:", response.status_code)
    print("Response Content (Preview):", response.text[:1000])

    soup = BeautifulSoup(response.text, "html.parser")

    # Debugging: Check the elements that match the selector
    all_results = soup.select('.tF2Cxc')
    print(f"Found {len(all_results)} results using the selector '.tF2Cxc'")

    results = []

    for result in all_results:
        title = result.select_one('h3')
        link = result.select_one('a')
        description = result.select_one('.VwiC3B')

        if title and link and description:
            results.append({
                "title": title.get_text(),
                "link": link['href'],
                "description": description.get_text()
            })

    if not results:
        print("No results found")
    
    return results

query = "HTML"
results = google_search(query, num_results=10)

for idx, result in enumerate(results, start=1):
    print(f"{idx}. {result['title']}")
    print(f"Link: {result['link']}")
    print(f"Description: {result['description']}\n")
