<!-- markdownlint-disable MD033 -->
<h1 align="center">Welcome to searcher-ge 👋</h1>
<p>
  <a href="https://opensource.org/licenses/MIT" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/naviamold" target="_blank">
    <img alt="Twitter: naviamold" src="https://img.shields.io/twitter/follow/naviamold.svg?style=social" />
  </a>
</p>

> Web Scraper for multiple Georgian Websites built with scrapy

Built with [scrapy](https://scrapy.org/)

## Install

### Using Pip

```bash
git clone https://github.com/Naviamold1/searcher-ge.git
cd searcher-ge
pip install -r requirements.txt
```

### Using [Pipenv](https://pipenv.pypa.io/en/latest/)

```bash
git clone https://github.com/Naviamold1/searcher-ge.git
cd searcher-ge
pipenv install
```

## Usage

run this template command

```sh
scrapy crawl <store> -o <filename>.<json|csv|xml> -a search_term="<product>"
```

replace **`<store>`** with the store name like: `ee, ada or zoommer`

replace `filename` with the name you want your file to be and choose either `json, csv or xml` as the file extension.

replace **`"<product>"`** with an name of a product you are searching for (e.g iphone)

p.s alta broken rn.

Example full command

```sh
scrapy crawl zoommer -o output.json -a search_term="apple watch"
```

## Proxies

If you want to scrape with proxies:

1. Create `proxies.txt` file in the root folder.
2. Fill it with your proxies.

Thats it.
And no I DON'T provide proxies, you will have to find them on your own.

## API

You can turn this scraper into an API via [scrapyrt](https://github.com/scrapinghub/scrapyrt)

just run the following command in the terminal

```sh
scrapyrt
```

by default the port is 9080 so navigate to this url in your browser or on API client

```sh
localhost:9080/crawl.json?start_requests=true&spider_name=<store>&crawl_arg={"search_term":"<product>"}
```

replace **`<store>`** with the store name like: `ee, ada or zoommer`

also replace **`"<product>"`** with an name of a product you are searching for (e.g iphone)

p.s alta broken rn.

Example full url

```sh
localhost:9080/crawl.json?start_requests=true&spider_name=ee&crawl_arg={"search_term":"iphone"
```

### You can specify scrapyrt port by doing this

```sh
scrapyrt -p <port>
```

## Author

👤 **Naviamold**

- Twitter: [@naviamold](https://twitter.com/naviamold)
- Github: [@Naviamold1](https://github.com/Naviamold1)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Naviamold1/searcher-ge/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2022 [Naviamold](https://github.com/Naviamold1).<br />
This project is [MIT](https://opensource.org/licenses/MIT) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
