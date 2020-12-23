from flask import Flask, request, jsonify, redirect, url_for
import db
import requests, json
app = Flask(__name__)
# from views import index

import sys
import json
from time import mktime
# import nltk
from datetime import datetime

# @app.route('/addname/<name>/')
# def addname(name):
#     db.expense_budget_collection.insert_one({"name": name.lower()})
#     return redirect(url_for('getnames'))

# @app.route('/getnames/')
# def getnames():
#     names_json = []
#     if db.expense_budget_collection.find({}):
#         for name in db.expense_budget_collection.find({}).sort("name"):
#             names_json.append({"name": name['name'], "id": str(name['_id'])})
#     return json.dumps(names_json)

# #test to insert data to the data base
# @app.route("/test")
# def test():
#     db.expense_budget_collection.insert_one({"name": "John"})
#     return "Connected to the data base!"

# @app.route("/post-selected-news-article/", methods=['GET','POST'])
# def post_selected_news_article():
#     response_object = {'status': 'success'}
#     if request.method == 'POST':
#         # print( request.get_json() )
#         for keyword in request.get_json()['keywords']:
#             print(keyword)
#             break
#     return jsonify(response_object)







# # the real deal
# @app.route('/getproducts/', methods=['GET'])
# def getproducts():
#     products_json = []
#     if db.products_collection.find({}):
#         for product in db.products_collection.find({}).sort("name"):
#             products_json.append({"id": str(product['_id']), "name": product['name']})
#     return json.dumps(products_json)

# @app.route('/addproduct/', methods=['POST'])
# def addproduct():
#     product = {
#         'name': request.json['name'],
#         'desc': request.json['desc']
#     }
#     db.products_collection.insert_one(product)
#     return redirect(url_for('getproducts'))






# import feedparser as fp
# import newspaper
# from newspaper import Article

# data = {}
# data["newspapers"] = {}

# def parse_config(fname):
#     # Loads the JSON files with news sites
#     with open(fname, "r") as data_file:
#         cfg = json.load(data_file)

#     for company, value in cfg.items():
#         if "link" not in value:
#             raise ValueError(f"Configuration item {company} missing obligatory 'link'.")

#     return cfg


# def _handle_rss(company, value, count, limit):
#     """If a RSS link is provided in the JSON file, this will be the first
#     choice. If you do not want to scrape from the RSS-feed, just leave the RSS
#     attr empty in the JSON file.
#     """

#     fpd = fp.parse(value["rss"])
#     # print(f"Downloading articles from {company}")
#     news_paper = {"rss": value["rss"], "link": value["link"], "articles": []}
#     for entry in fpd.entries:
#         # Check if publish date is provided, if no the article is
#         # skipped.  This is done to keep consistency in the data and to
#         # keep the script from crashing.
#         if not hasattr(entry, "published"):
#             continue
#         if count > limit:
#             break
#         article = {}
#         article["link"] = entry.link
#         date = entry.published_parsed
#         article["published"] = datetime.fromtimestamp(mktime(date)).isoformat()
#         try:
#             content = Article(entry.link)
#             content.download()
#             content.parse()
#             content.__dict__
#         except Exception as err:
#             # If the download for some reason fails (ex. 404) the
#             # script will continue downloading the next article.
#             print(err)
#             print("continuing...")
#             continue
#         article["title"] = content.title
#         article["text"] = content.text
#         article["keywords"] = content.keywords
#         news_paper["articles"].append(article)
#         # print(f"{count} articles downloaded from {company}, url: {entry.link}")
#         count = count + 1
#     return count, news_paper


# def _handle_fallback(company, value, count, limit):
#     """This is the fallback method that uses the python newspaper library 
#     to extract articles if a RSS-feed link is not provided."""

#     # print(f"Building site for {company}")
#     paper = newspaper.build(value["link"], memoize_articles=False)
#     news_paper = {"link": value["link"], "articles": []}
#     none_type_count = 0
#     for content in paper.articles:
#         if count > limit:
#             break
#         try:
#             content.download()
#             content.parse()
#             content.nlp()
#         except Exception as err:
#             print(err)
#             print("continuing...")
#             continue
#         # If there is no found publish date the article will be skipped.
#         # After 10 downloaded articles from the same newspaper without publish date, the company will be skipped.
#         if content.publish_date is None:
#             # print(f"{count} Article has date of type None...")
#             none_type_count = none_type_count + 1
#             if none_type_count > 10:
#                 # print("Too many noneType dates, aborting...")
#                 none_type_count = 0
#                 break
#             count = count + 1
#             continue
#         article = {
#             "title": content.title,
#             "text": content.text,
#             "link": content.url,
#             "keywords": content.keywords,
#             "published": content.publish_date.isoformat(),
#         }
#         news_paper["articles"].append(article)
#         print(
#             f"{count} articles downloaded from {company} using newspaper, url: {content.url}, keywords:{content.keywords}"
#         )
#         count = count + 1
#         none_type_count = 0
#     return count, news_paper


# def run(config, limit=4):
#     """Take a config object of sites and urls, and an upper limit. Iterate through each news company.
#     Write result to scraped_articles.json."""
#     for company, value in config.items():
#         count = 1
#         if "rss" in value:
#             count, news_paper = _handle_rss(company, value, count, limit)
#         else:
#             count, news_paper = _handle_fallback(company, value, count, limit)
#         data["newspapers"][company] = news_paper

#     # Finally it saves the articles as a JSON-file.
#     try:
#         with open("scraped_articles.json", "w") as outfile:
#             json.dump(data, outfile, indent=2)
#     except Exception as err:
#         print(err)


# def news():
#     """News site scraper."""
    
#     try:
#         config = parse_config("NewsPapers.json")
#     except Exception as err:
#         sys.exit(err)
#     run(config)

# #-----------------------------

# @app.route("/get-top-news/", methods=['GET'])
# def get_top_news():

#     keywords_list = []
#     with open("scraped_articles.json", "r") as data_file:
#         scraped_file = json.load(data_file)

#     for comp, paper in scraped_file.items():
#         for b, value in paper.items():
#             if "link" not in value:
#                 raise ValueError(f"Configuration item {value} missing obligatory 'link'.")
#             else:
#                 for article in value['articles']:
#                     for keyword in article['keywords']:
#                         print(keyword)
#                         keywords_list.append(keyword)
            
#     return jsonify(keywords_list)

# @app.route("/get-top-news-articles/", methods=['GET'])
# def get_top_news_articles():

#     articles_list = []
#     with open("scraped_articles.json", "r") as data_file:
#         scraped_file = json.load(data_file)

#     for comp, paper in scraped_file.items():
#         for b, value in paper.items():
#             if "link" not in value:
#                 raise ValueError(f"Configuration item {value} missing obligatory 'link'.")
#             else:
#                 for article in value['articles']:
#                     articles_list.append(article)
            
#     return jsonify(articles_list)

# @app.route("/post-selected-news-article/", methods=['POST'])
# def post_selected_news_article():

#     articles_list = []
#     with open("scraped_articles.json", "r") as data_file:
#         scraped_file = json.load(data_file)

#     for comp, paper in scraped_file.items():
#         for b, value in paper.items():
#             if "link" not in value:
#                 raise ValueError(f"Configuration item {value} missing obligatory 'link'.")
#             else:
#                 for article in value['articles']:
#                     articles_list.append(article)
            
#     return jsonify(articles_list)

# # @app.route('/post/', methods=['POST'])
# # def post_something():
# #     param = request.form.get('name')
# #     print(param)
# #     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
# #     if param:
# #         return jsonify({
# #             "Message": f"Welcome {name} to our awesome platform!!",
# #             # Add this option to distinct the POST request
# #             "METHOD" : "POST"
# #         })
# #     else:
# #         return jsonify({
# #             "ERROR": "no name found, please send a name."
# #         })

# #-----------------------------

@app.route("/")
def pg():
    # index()
    # news()
    url = "https://product-categorization.p.rapidapi.com/categorized"

    querystring = {"title":"french fries","price":"23000"}

    headers = {
        'x-rapidapi-key': "a316563259msh808280fd09a9419p1e1e98jsnf72eb1d4263b",
        'x-rapidapi-host': "product-categorization.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return response.text

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)