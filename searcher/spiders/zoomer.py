import scrapy


class ZoommerSpider(scrapy.Spider):
    name = "zoommer"
    allowed_domains = ["zoommer.ge"]
    custom_settings = {"ROBOTSTXT_OBEY": False}

    def start_requests(self):
        yield scrapy.Request(
            f"https://zoommer.ge/search?q={self.search_term}&CategoryIds=0"
        )

    def parse(self, response):
        for product in response.css(".product_item"):
            yield {
                "title": product.css("h4::attr(title)").get(),
                "price": float(
                    product.css(".product_new_price::text")
                    .get()
                    .rstrip("₾")
                    .replace(" ", "")
                    .replace(" ", "")
                ),
                "link": f"https://zoommer.ge/{product.css('.product_link::attr(href)')[0].get()}",
                "images": product.css(".product_img::attr(data-src)").getall(),
            }
        next_page = response.css(".show_more_btn::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
