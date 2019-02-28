# Bangla Dictionary
An English-to-Bengali dictionary made out of scraped web data

## Flask API
- To run the API Install the dependencies from requirements.txt
- Use the command `python run.py` file to start server at `http://localhost:5000/`
- For unit testing, install `pytest` and then enter command `pytest test_api.py`

## Web UI with Vue
- Change directory to `vue-ui`
- Install dependencies with command `npm install`
- To run development mode use command `npm run serve`, the server will start at  `http://localhost:8080/`
- To create a production build run 'npm run build'
- To be able to fetch data you have to keep the API running

## Web Crawler
- To run the scraper install `Scrapy`.
- Go to the directory `web-scraper`.
- Run the command `scrapy crawl dictionary`
- The crawler will save the data in root directory within a sqlite database.
- Change the old database in `api/database` to serve new data with the api.
