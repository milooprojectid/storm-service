from newspaper import Article

def getNews(url):
    """
    Get paragrah form news
    :param url : url of news online
    :return : sentence of news online
    """
    article = Article(url)
    article.download()
    article.html
    article.parse()
    news = article.text
    return(news)