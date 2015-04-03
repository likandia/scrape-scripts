from lxml import html
import requests

def main():
    page = requests.get('http://queue.acm.org/listing.cfm?item_topic=Distributed%20Computing&qc_type=theme_list&filter=Distributed%20Computing&page_title=Distributed%20Computing&order=desc')
    tree = html.fromstring(page.text)
    articles = tree.xpath('//h2/a')
    i = 1
    for a in articles:
        print(str(i) + ". " + a.text_content())
        i += 1

if __name__ == "__main__":
    main()
