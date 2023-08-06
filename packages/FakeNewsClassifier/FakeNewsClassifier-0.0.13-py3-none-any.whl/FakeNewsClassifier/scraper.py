from newspaper import Article

def parse_article(url):

    
    article = Article(url)                      # Unspecified language

    
    article.download()                          # To download the article


    article.parse()                             # To parse the article

    full_text = article.title + article.text    # Combine title and text

    full_text = full_text.replace('\n', '')

    full_text = [full_text]                     # Serialize


    return full_text
