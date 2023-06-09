import json

import scrapy


class EeSpider(scrapy.Spider):
    name = "ee"
    allowed_domains = ["api.ee.ge"]
    start_urls = ["https://api.ee.ge/product/filter_products"]

    def start_requests(self):
        payload = {
            "min_price": 0,
            "max_price": 0,
            "category": "",
            "sort_by": "",
            "item_per_page": 1000,
            "page_no": "",
            "search_text": self.search_term,
            "sale_products": 0,
            "slug": "",
            "pageno": "",
        }
        yield scrapy.Request(
            "https://api.ee.ge/product/filter_products",
            method="POST",
            headers={"Content-Type": "application/json"},
            body=json.dumps(payload),
            callback=self.parse,
        )

    def parse(self, response):
        for product in response.json()["data"]:
            try:
                yield {
                    "title": product["product_desc"],
                    "price": float(product["actual_price"]),
                    "link": f'https://ee.ge/{product["parent_category_slug_gr"]}/{product["category_slug_gr"]}/{product["product_slug_gr"]}',
                    "images": product["image"],
                }
            except:
                continue
