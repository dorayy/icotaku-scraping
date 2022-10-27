import scrapy
from icotaku.pipelines import Database
from icotaku.items import PlanningDetailItem
from scrapy import Request

class PlanningcontentSpider(scrapy.Spider):
    name = 'planningContent'
    allowed_domains = ['anime.icotaku.com']

    Database.connectDb()
    Database.createTable()

    # On récupère les infos de la bdd
    urls = Database.getPlanningUrls()

    start_urls = [url[0] for url in urls]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        content = response.css('div.contenu')

        item = PlanningDetailItem()

        for info in content:
            # Titre français
            try:
                item['titleFr'] = str(info.css('div.informations > div.p.info_fiche > div::text')[3].extract()).strip()
            except:
                item['titleFr'] = ''
            # Titre japonais
            try:
                item['titleJp'] = str(info.css('div.informations > div.p.info_fiche > div::text')[1].extract()).strip()
            except:
                item['titleJp'] = ''
            # Origine
            try:
                item['origin'] = str(info.css('div.informations > div.p.info_fiche > div::text')[7].extract()).strip()
            except:
                item['origin'] = ''
            # Genre
            try:
                item['genre'] = ' '.join(info.css('div.informations > div.p.info_fiche > div > span > a::text')[:-1].extract())
            except:
                item['genre'] = ''
            # Public
            try:
                item['public'] = str(info.css('div.informations > div.p.info_fiche > div::text')[17].extract()).strip()
            except:
                item['public'] = ''
            # nbEpisode
            try:
                item['nbEpisode'] = str(info.css('div.informations > div.p.info_fiche > div::text')[19].extract()).strip()
            except:
                item['nbEpisode'] = ''
            # durationEpisode
            try:
                item['durationEpisode'] = str(info.css('div.informations > div.p.info_fiche > div::text')[21].extract()).strip()
            except:
                item['durationEpisode'] = ''
            # Editor
            try:
                item['editor'] = info.css('div.informations > div.p.info_fiche > div >a::text')[0].extract()
            except:
                item['editor'] = ''
            # Official website
            try:
                item['officialWebsite'] = info.css('div.informations > div.p.info_fiche > div >a::text')[1].extract()
            except:
                item['officialWebsite'] = ''
            # Story
            try:
                item['story'] = info.css('div.informations > p::text')[0].extract()
            except:
                item['story'] = ''
            # Img
            try: 
                item['img'] = info.css('div.complements > p > img::attr(src)').get().replace('/images/../', 'https://anime.icotaku.com/')
            except:
                item['img'] = ''

            print(item)
            Database.addRowPlanningContent(item)

            yield item
       