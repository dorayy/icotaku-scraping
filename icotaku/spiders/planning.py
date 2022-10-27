from unicodedata import category
import scrapy
from scrapy import Request
from icotaku.items import PlanningItem
from icotaku.pipelines import Database
import numpy as np

class PlanningSpider(scrapy.Spider):
    name = 'planning'
    allowed_domains = ['www.icotaku.com']

    #Liste des pages à collecter
    start_urls = np.array([[f'https://anime.icotaku.com/planning/planningSaisonnier/saison/{i}/annee/{n}' for i in ['hiver','printemps','ete','automne']] for n in range(2015,2023)])
    start_urls = start_urls.flatten()
    start_urls = list(start_urls)
    #print(start_urls)

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)
        
        
    def parse(self, response):
        liste_anime = response.css('div.planning_saison')
        category = response.css('div.planning_saison').css('div.categorie > h2::text').extract()
        
        for anime in liste_anime:
            item = PlanningItem()
            
            
            item['category'] = anime.css('div.categorie > h2::text').get()
            print("Categorie :" ,  item['category'])

            # #indice boursier
            # try: 
            #   item['indice'] = indices.css('td.c-table__cell.c-table__cell--dotted.u-text-uppercase').css('a::text').get()
            # except:
            #   item['indice'] = 'None'
            
            # #indice cours de l'action
            # try: 
            #   item['cours'] = indices.css('span.c-instrument.c-instrument--last::text').get()
            # except:item['cours'] = 'None'
            
            # #Variation de l'action
            # try: 
            #   item['var'] = indices.css('span.c-instrument.c-instrument--instant-variation::text').get()
            # except:
            #   item['var'] = 'None'
            
            # #Valeur la plus haute
            # try: 
            #   item['hight'] = indices.css('span.c-instrument.c-instrument--high::text').get()
            # except:
            #   item['hight'] = 'None'
            
            # #Valeur la plus basse
            # try: 
            #   item['low'] = indices.css('span.c-instrument.c-instrument--low::text').get()
            # except:
            #   item['low'] = 'None'

            # #Valeur d'ouverture
            # try: 
            #   item['open_'] = indices.css('span.c-instrument.c-instrument--open::text').get()
            # except:
            #   item['open_'] = 'None'

            # #Date de la collecte
            # try: 
            #   item['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # except:
            #   item['time'] = 'None'

            # self.pipeline.process_item_boursorama(item)

            # yield item