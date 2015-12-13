from scrapy import Spider
from scrapy.selector import Selector
import os
import csv
from indeed.items import IndeedItem
from indeed.mail_sender import send_email


class IndeedSpider(Spider):
    name = "indeed"
    allowed_domains = ["indeed.com.mx"]
    start_urls = [
        "http://www.indeed.com.mx/trabajo?q=python&l=M%C3%A9xico&sort=date",
    ]

    def parse(self, response):
        jobs = Selector(response).xpath('//*[@id="resultsCol"]/div[@class="  row  result"]')
        file_path = os.path.join(os.getcwd(), 'items.csv')
        job_data = []
        mail_msg = ''

        with open(file_path, 'r+') as data_file:
            f_csv = csv.DictReader(data_file)
            next(f_csv)
            for row in f_csv:
                job_data.append(row['url'])

            for job in jobs:
                item = IndeedItem()
                item['title'] = job.xpath('h2/a[@class="turnstileLink"]/text()').extract()[0]
                item['url'] = 'http://www.indeed.com.mx' + job.xpath('h2/a[@class="turnstileLink"]/@href').extract()[0]

                if item['url'] not in job_data:
                    data_file.write(item['url'] + ',' + item['title'] + '\n')
                    mail_msg += '%s - %s \n\n' % (item['title'], item['url'] )

        if mail_msg != '':
            send_email(mail_msg)
