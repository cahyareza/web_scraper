import scrapy
from e_commerce_2.items import ECommerce2Item
from bs4 import BeautifulSoup
import re

class search(scrapy.Spider):
    name = "ecomerce_2"
    start_urls = ['https://webscraper.io/test-sites/e-commerce/allinone/',]

    def __init__(self):
        self.declare_xpath()

        # All the XPaths the spider needs to know go here

    def declare_xpath(self):
        self.getAllCategoriesXpath = "//div[@class='sidebar-nav navbar-collapse']/ul[@class='nav']/li/a/@href"
        self.getAllSubCategoriesXpath = "//li[@class='active']/ul[@class='nav nav-second-level collapse in']/li/a/@href"
        self.getAllItemXpath = "//div[@class='thumbnail']/div/div[@class='caption']/h4/a/@href"
        self.Titlexpath = "//div[@class='col-lg-10'/div[@class='caption]/h4/text()"
        self.CategoriesXpath = "//div[@class='sidebar-nav navbar-collapse']/ul[@class='nav']/li/a/text()"
        self.SubCategoriesXpath = "//li[@class='active']/ul[@class='nav nav-second-level collapse in']/li/a/text()"
        self.DescriptionXpath = "//div[@class='caption']/p[@class='description']/text()"
        self.PriceXpath = "//div[@class='caption']/p[@class='description']/h4[@class='pull-right price']/text()"
        self.ReviewXpath = "//div[@class='ratings']/p/text()"

    # from the main page, cal parse_categories on each category link
    def parse(self, response):
        for href in response.xpath(self.getAllCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_categories, dont_filter=True )

    # from each category page, call parse_subcategory on each subcategory link
    def parse_categories(self, response):
        for href in response.xpath(self.getAllSubCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_subcategories, dont_filter=True)

    # from each subcategory page, call parse_main_item on each product page link
    def parse_subcategories(self, response):
        for href in response.xpath(self.getAllItemXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_main_item, dont_filter=True)

        #call parse_subcategory on the next page
        #next_page = response.xpath('//ol[@class="unstyled l_mgn-b-sm"]/li[3]/a/@href')
        #if next_page is not None :
        #   url = response.urljoin(next_page)
        #    yield scrapy.Request(url, callback=self.parse_subcategories, dont_filter=True)

        next_page = response.xpath('//ol[@class="unstyled l_mgn-b-sm"]/li[3]/a/@href').get()
        if next_page is not None:
            url = next_page
            yield scrapy.Request(url, callback=self.parse_subcategories, dont_filter=True)

    def parse_main_item(self, response):
        item = ECommerceItem()

        Title = response.xpath(self.Titlexpath).extract()
        #Title = self.cleanText(self.parseText(self.listToStr(Title)))

        Category = response.xpath(self.CategoryXpath).extract()
        #Category = ','.join(map(str, Category[1:]))
        #Category = self.cleanText(self.parseText(Category))

        Subcategories = response.xpath(self.SubCategoriesXpath).extract()

        Description = response.xpath(self.DescriptionXpath).extract()

        Price = response.xpath(self.PriceXpath).extract()
        #Price = self.cleanText(self.parseText(self.listToStr(Price)))

        Review = response.xpath(self.ReviewXpath).Extract()


        item['Title'] =  Title
        item['Category'] = Category
        item['Price'] = Price
        item['Subcategories'] = Subcategories
        item['Description'] = Description
        item['Review'] = Review

        return item

        # Methods to clean and format text to make it easier to work with later

    def listToStr(self, MyList):
        dumm = " "
        MyList = [i.encode('utf-8') for i in MyList]
        for i in MyList:
            dumm = "{0}{1}".format(dumm, i)
        return dumm

    def parseText(self, str):
        soup = BeautifulSoup(str, 'html.parser')
        return re.sub(" +|\n|\r|\t|\0|\x0b|\xa0", ' ', soup.get_text()).strip()

    def cleanText(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text()
        text = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+", ' ', text).strip()
        return text
