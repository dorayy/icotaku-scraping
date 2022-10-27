import os
import sys

# execute les commandes
os.system('cd spiders')
os.system('scrapy crawl planning -o ../export/planning.csv')
os.system('scrapy crawl planningContent -o ../export/planningContent.csv')

