from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys, getopt
import re


from utils import get_image_info, get_subpage_url

def main(argv):
    url = ''
    outputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hu:o:",["url=","ofile="])
    except getopt.GetoptError:
       print ('test.py -u <url> -o <outputfile>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print('test.py -u <url> -o <outputfile>')
          sys.exit()
       elif opt in ("-u", "--url"):
          url = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg

    print('Input url is "', url)
    print('Output file is "', outputfile)

    base_url = url

    image_info_list = get_image_info(base_url)

    sub_page_links = get_subpage_url(base_url)

    for link in sub_page_links:
        print('Get image info for: ', link)
        image_info_list += get_image_info(link)


    xml_file = open(outputfile, 'w')
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
	    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
        <url>
	    <loc>{}</loc>

    """.format(base_url)

    # prevent duplication
    """
      Elaboration of following code

      tupleSet = {tuple(d.items()) for d in l}
      dictList = [dict(t) for t in tupleSet]
    """
    image_info_list = [dict(t)
	               for t in {tuple(d.items()) for d in image_info_list}]

    for image_info in image_info_list:
        xml_content += """
	      <image:image>
	        <image:loc>{}</image:loc>
	        <image:caption>{}</image:caption>
	      </image:image>
	    """.format(image_info['src'], image_info['caption'])

    xml_content += """
        </url> 
    </urlset> 
    """
    xml_file.write(xml_content)
    print("Done!")


if __name__ == "__main__":
    main(sys.argv[1:])
