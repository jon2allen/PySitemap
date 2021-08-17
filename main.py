import argparse
from crawler import Crawler
from urllib.parse import urlparse



# initializing parameters
parser = argparse.ArgumentParser(description="Sitemap generator")
parser.add_argument('--url', action="store", default="", help="For example https://www.finstead.com")
parser.add_argument('--exclude', action="store", default="", help="regex pattern to exclude. For example 'symbol/info' will exclude https://www.finstead.com/symbol/info/ORCL")
parser.add_argument('--no-verbose', action="store_true", default="", help="print verbose output")
parser.add_argument('--output', action="store", default="sitemap.xml", help="File path for output, if file exists it will be overwritten")
parser.add_argument('--wp', action="store_true", help="Wordpress aware sitemap")

# parsing parameters
args = parser.parse_args()
url = args.url.rstrip("/")

found_links = []

# initializeing crawler
crawler = Crawler(url, exclude=args.exclude, no_verbose=args.no_verbose)

# fetch links
links = crawler.start()

def sanitize_link(link):
    """make correction so link is proper"""
    if link.lower().startswith("http"):
        return link
    if link.startswith("#"):
        return "/" + link
    if not link.startswith("/"):
        return "/" + link
    return link

def wp_remove_dup(link):
    """no number nodes om last node 
       This remove duplicates in Monthly, yearly
       summaries/archives.
       test for page to preserve categories, tags
    """
    if "page" in link.lower():
        return False
    split_url = link.split("/") 
    item = ''.join(split_url[-2:-1])

    if item.isnumeric():
        return True
    return False
            
            
    
#write into file
with open(args.output, "w") as file: 
	file.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

	for link in links:
		prefix = ""
		if link.startswith(url):
			prefix = ""
		else:
			prefix = url
		f_link = sanitize_link( link)
		print( "flink:  ", f_link)
		if args.wp:
			if not wp_remove_dup(link):
				file.write("\n\t\t<url>\n\t\t\t<loc>\n\t\t\t\t{0}{1}\n\t\t\t</loc>\n\t\t</url>".format(prefix, f_link))

	file.write('</urlset>')


