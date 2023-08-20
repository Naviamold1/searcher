<!-- markdownlint-disable MD033 -->
<h1 align="center">Welcome to searcher-scraper 👋</h1>
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

## Store List

| Store Name       | Status | Argument  | Website                 | Notes                                                                                                |
| ---------------- | ------ | --------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Alta             | [x]    | alta      | <https://alta.ge/>      | Newly added might be some bugs.                                                                      |
| Elit Electronics | [x]    | ee        | <https://ee.ge/>        |                                                                                                      |
| Zoommer          | [x]    | zoommer   | <https://zoommer.ge/>   | On Zoommer's current website if there are multiple pages for a search result it stalks for a bit     |
| Ada              | [x]    | ada       | <https://adashop.ge/>   | Ada's current search api returns all of there products sometimes if the search term is very specific |
| Metromart        | [ ]    | metro     | <https://metromart.ge/> | Not working right now, having issues with websites lazy loading                                      |
| gITec            | [ ]    | gitec     | <https://gitec.ge/>     | Not implemented yet                                                                                  |
| allmarket        | [ ]    | allmarket | <https://allmarket.ge/> | Not implemented yet                                                                                  |
| gsshop           | [ ]    | gsshop    | <https://gsshop.ge/>    | Not implemented yet                                                                                  |
| mymarket         | [ ]    | mymarket  | <https://mymarket.ge/>  | Not implemented yet                                                                                  |

Additional store suggestions are welcome

## Install

### Installing via [Docker](https://www.docker.com/)

```bash
git clone https://github.com/Naviamold1/searcher-scraper.git
docker-compose up -d
```

This will install, setup and run the project with [scrapyrt](#api) (click to learn more)

### Manual Installation

#### Install Splash

This project uses [scrapy-splash](https://pypi.org/project/scrapy-splash/) for some scraping, therefor to use this project at its full extend we need to install [splash](https://splash.readthedocs.io/en/latest/install.html):

```bash
docker pull scrapinghub/splash
docker run -it -p 8050:8050 --rm scrapinghub/splash
```

After that you can install the project via Pip **OR** [Poetry](#using-poetry)

#### Using Pip

```bash
git clone https://github.com/Naviamold1/searcher-scraper.git
cd searcher-scraper
pip install -r requirements.txt
```

#### Using [Poetry](https://python-poetry.org/)

```bash
git clone https://github.com/Naviamold1/searcher-scraper.git
cd searcher-scraper
poetry shell
poetry install
```

If you plan on using an [API](#api) you should also install api dependencies

```sh
poetry install --with api
```

If you plan on altering or contributing to this repo you should also install dev dependencies

```sh
poetry install --with dev
```

## Usage

run this template command

```sh
scrapy crawl <store> -o <filename>.<json|csv|xml> -a search_term="<product>"
```

replace **`<store>`** with the store name **argument** which you can get from this [table](#store-list) (e.g. ee, ada, zoommer...)

replace `filename` with the name you want your file to be and choose either `json, csv or xml` as the file extension.

replace **`"<product>"`** with an name of a product you are searching for (e.g iphone)

Example full command

```sh
scrapy crawl zoommer -o output.json -a search_term="apple watch"
```

## Proxies

If you want to scrape with proxies:

1. go to [searcher\settings.py](https://github.com/Naviamold1/searcher/blob/d43be643de89297f834276af9ce3482138ff3735/searcher/settings.py) scroll down until you see `DOWNLOADER_MIDDLEWARES` option and uncomment the rotating.proxies lines.
2. Create `proxies.txt` file in the root folder.
3. Fill it with your proxies.

Thats it.
And no I DON'T provide proxies, you will have to find them on your own.

## API

You can turn this scraper into an API via [scrapyrt](https://github.com/scrapinghub/scrapyrt)

just run the following command in the terminal

```sh
scrapyrt
```

The default scrapyrt port is 9080 so navigate to this url in your browser or in an API client

```sh
localhost:9080/crawl.json?start_requests=true&spider_name=<store>&crawl_arg={"search_term":"<product>"}
```

replace **`<store>`** with the store name **argument** which you can get from this [table](#store-list) (e.g. ee, ada, zoommer...)

also replace **`"<product>"`** with an name of a product you are searching for (e.g iphone)

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
