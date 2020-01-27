import scrapy


class FirefoxSpider(scrapy.Spider):
    name = "firefox"

    def start_requests(self):
        urls = [
            # entry point for Firefox and Thunderbird security advisories
            'https://www.mozilla.org/en-US/security/advisories/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.css('.mzp-c-article'):
            for date_list in article.css('ul'):
                for date_page_href in response.css('li.level-item a::attr(href)'):
                    yield response.follow(date_page_href, callback=self.parse_date_page)

    def parse_date_page(self, response):
        for article in response.css('.mzp-c-article'):
            for cve in article.css('section.cve'):
                summary = list(zip(cve.css('dt::text').getall(), cve.css('dd *::text').getall()))
                yield {
                    'id': cve.css('h4::attr(id)').get(),
                    'title': cve.css('h4 a::text').get(),
                    'description': ' '.join(cve.css('h5 + p *::text').extract()),
                    'references': cve.css('h5 + ul > li *::text').get(),
                    'summary': summary,
                }
