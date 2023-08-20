import scrapy
from scrapy_splash import SplashRequest

# TODO


class AltaSpider(scrapy.Spider):
    name = "alta"
    allowed_domains = ["alta.ge"]
    handle_httpstatus_list = [403]

    def start_requests(self):
        yield SplashRequest(
            url=f"https://alta.ge/?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q={self.search_term}&dispatch=products.search&items_per_page=1000",
            callback=self.parse,
        )

    def parse(self, response):
        for product in response.css("div.ty-column3"):
            try:
                yield {
                    "title": product.css("a.product-title::text").get(),
                    "price": float(product.css("span.ty-price-num::text").get()),
                    "link": product.css("a.product-title::attr(href)").get(),
                    "thumbnail": product.css(
                        "div.ty-grid-list__item div.ty-grid-list__image img.ty-pict.cm-image:not(.lazyowl)::attr(src)"
                    ).get(),
                }
            except ValueError:
                continue
        next_page = response.css(
            "#pagination_contents > div.ty-pagination__bottom > div > a:nth-child(3)::attr(href)"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
