import json

import scrapy


class AdaSpider(scrapy.Spider):
    name = "ada"
    allowed_domains = ["api.adashop.ge"]
    start_urls = ["https://api.adashop.ge/api/v1/products/rest_search/search"]

    def start_requests(self):
        payload = {"search": self.search_term}
        yield scrapy.Request(
            "https://api.adashop.ge/api/v1/products/rest_search/search",
            method="POST",
            headers={"Content-Type": "application/json"},
            body=json.dumps(payload),
            callback=self.parse,
        )

    def parse(self, response):
        for product in response.json()["searched_products"]:
            try:
                yield {
                    "title": product["name"],
                    "price": float(product["price_with_price_tag"]),
                    "link": f'https://adashop.ge/product/{product["_id"]}',
                    "images": f'https://adashop.ge/_next/image?url=http%3A%2F%2Flocalhost%3A5001%2Fimages%2Fproducts%2F{product["image"]}&w=640&q=75',
                }
            except ValueError:
                continue
