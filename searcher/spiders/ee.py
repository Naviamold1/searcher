import json

import scrapy


class EeSpider(scrapy.Spider):
    name = "ee"
    allowed_domains = ["api.ee.ge"]
    start_urls = ["https://api.ee.ge/07072022/product/filter_products"]

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
            "https://api.ee.ge/07072022/product/filter_products",
            method="POST",
            headers={"Content-Type": "application/json"},
            body=json.dumps(payload),
            callback=self.parse,
        )

    def parse(self, response):
        for product in response.json()["data"]:
            a = product["parent_category_slug_gr"]
            b = product["category_slug_gr"]
            c = product["product_slug_gr"]
            yield {
                "title": product["product_desc"],
                "price": float(product["actual_price"]),
                "link": f"https://ee.ge/{a}/{b}/{c}",
                "images": product["image"],
            }
