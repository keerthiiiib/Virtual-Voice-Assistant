from newsapi import NewsApiClient

api = NewsApiClient(api_key='db787b2690094b989858aa5df49dc1a4')

def get_latest_news():
    top_headlines = api.get_top_headlines(language='en', country='us')
    articles = top_headlines['articles']
    news = [article['title'] for article in articles]
    return "Here are the latest headlines: " + ", ".join(news)
