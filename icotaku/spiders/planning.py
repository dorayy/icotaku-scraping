import scrapy
from scrapy import Request
from icotaku.items import PlanningItem
from icotaku.pipelines import Database
import numpy as np

class PlanningSpider(scrapy.Spider):
    name = 'planning'
    allowed_domains = ['www.icotaku.com']

    Database.connectDb()
    Database.createTablePlanning()
        
    #Liste des pages à collecter
    start_urls = np.array([[f'https://anime.icotaku.com/planning/planningSaisonnier/saison/{i}/annee/{n}' for i in ['hiver','printemps','ete','automne']] for n in range(2022,2023)])
    start_urls = start_urls.flatten()
    start_urls = list(start_urls)

    # start_urls = [f'https://anime.icotaku.com/planning/planningSaisonnier/saison/automne/annee/2022']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
      liste_anime = response.css('div.planning_saison')
      category = liste_anime.css('div.categorie')
      season = response.css('h2.planning_title > span::text')[2].extract().split('\xa0\n')[1].strip(' ')

      for animes in category:
        item = PlanningItem()
        nb_anime_in_category = len(animes.css('table').extract())

        for i in range(nb_anime_in_category):
          try: 
              item['title'] = animes.css('th.titre > a::text')[i].extract().strip()
          except:
              item['title'] = 'None'
          
          try: 
              item['origin'] = animes.css('span.origine::text')[i].extract().strip()
          except:
              item['origin'] = 'None'
          
          try: 
              item['distribution'] = animes.css('span.editeur::text')[i].extract().strip()
          except:
              item['distribution'] = 'None'
          
          try: 
              item['editor'] = animes.css('span.studio::text')[i].extract().strip()
          except:
              item['editor'] = 'None'

          try: 
              item['releaseDate'] = " ".join(animes.css('span.date::text')[i].extract().strip().split())
          except:
              item['releaseDate'] = 'None'
          
          try: 
              item['category'] = animes.css('h2::text').get()
          except:
              item['category'] = 'None'

          try: 
              item['season'] = season
          except:
              item['season'] = 'None'
          
          try:
              item['link'] = animes.css('th.titre > a::attr(href)')[i].extract().replace('/anime','https://anime.icotaku.com/anime')
          except:
              item['link'] = 'None'

          Database.addRowPlanning(item)
          
          yield item