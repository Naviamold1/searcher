import scrapy
from scrapy_splash import SplashRequest

# TODO


class MetroSpider(scrapy.Spider):
    name = "metro"
    allowed_domains = ["metromart.ge"]
    custom_settings = {"ROBOTSTXT_OBEY": False}

    def start_requests(self):
        yield SplashRequest(
            url=f"https://metromart.ge/ka_GE/shop?search={self.search_term}",
            callback=self.parse,
        )

    def parse(self, response):
        for product in response.css(".oe_product"):
            yield {
                "title": product.css(".oe_product_name::text").get(),
                "price": product.css("span.oe_currency_value::text").get(),
                "link": product.css("a.img-product ::attr(href)").get(),
                "thumbnail": product.css("img.img::attr(src)").get(),
            }
