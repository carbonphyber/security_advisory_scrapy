import json
import scrapy


class FirefoxSpider(scrapy.Spider):
    name = "apple"

    def start_requests(self):
        urls = [
            # Special entry-point Apple KB article for security releases
            # Note: not all entries have URLs or CVEs
            'https://support.apple.com/en-us/HT201222',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.css('#sections'):
            for cve_table in article.css('#tableWraper'):
                for detail_page_href in cve_table.css('td a::attr(href)')[:10]:
                    yield response.follow(detail_page_href, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        cves = list()
        cve_o = {}
        for article in response.css('#content'):
            product_section = article.css('#content > div')
            # This is hacky because adjacent <p> tags are overloaded to describe multiple adjacent CVEs.
            # use a cve_o to assemble fields for the CVE. Reset it when we get to the new CVE heading.
            section_title = None
            cve_o = {}
            for cve in product_section[2].css('div > p'):
                strong_match = cve.css('strong')
                # if the current p is a CVE header, save the previous cve_o to cves and build a new one
                if len(strong_match) > 0:
                    if len(cve_o) > 0 and 'title' in cve_o:
                        cves.append(cve_o)
                    cve_o = {}
                    section_title = ''.join(strong_match.css('::text').getall())
                    cve_o['title'] = section_title

                this_paragraph = ''.join(cve.css('p ::text').getall())
                if this_paragraph is not None:
                    this_paragraph = this_paragraph.strip()
                    if len(this_paragraph) > 0:
                        if this_paragraph[0:15] == 'Available for: ':
                            cve_o['available_for'] = this_paragraph[15:]
                        elif this_paragraph[0:8] == 'Impact: ':
                            cve_o['impact'] = this_paragraph[8:]
                        elif this_paragraph[0:13] == 'Description: ':
                            cve_o['description'] = list()
                            cve_o['description'].append(this_paragraph[13:])
                        elif this_paragraph[0:14] == 'Entry updated ':
                            cve_o['updated_at'] = this_paragraph[14:]
                        else:
                            if 'description' not in cve_o:
                                cve_o['description'] = list()
                            cve_o['description'].append(this_paragraph)
        yield {'cves': cves}
