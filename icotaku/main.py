import os
import sys

# execute ls command
os.system('cd spiders/ && scrapy crawl planningContent -o ../export/planningContent.csv')
