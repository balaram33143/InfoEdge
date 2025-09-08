from fastapi import FastAPI
from data_pipeline import stocks, news, reddit  # Import your modules

app = FastAPI()  # Create FastAPI app instance

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "InfoEdge is running!"}

# Stock endpoint example
@app.get("/stocks")
def get_stocks():
    return stocks.fetch_stock_data("AAPL")  # Example: Apple stock

# News endpoint example
@app.get("/news")
def get_news():
    return news.fetch_news("finance")  # Example: finance news

# Reddit endpoint example
@app.get("/reddit")
def get_reddit():
    return reddit.fetch_posts("stocks")  # Example: subreddit 'stocks'

