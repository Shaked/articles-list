"""
Article list generator plugin for Pelican
================================

The idea is to generate a (json) file to be able to communicate togehter with Ajax calls
This will allow creating single page endless scroll without the need of using server side files

@todos
 - Generate files by pages (e.g if there are 50 articles and I want to have 10 articles per load)
 - Allow Json but consider also supporting XML
 - Setup which article params should be parsed into Json
"""
from pelican import signals
import os,io,json
import pprint 

def create_articles_list(generator): 
    config = generator.settings.get("ARTICLES_LIST")
    pprint.pprint(config)
    if "output_path" in config:
      articles_list_path = config["output_path"]
    else: 
      articles_list_path = generator.settings.get("OUTPUT_PATH")

    if not hasattr(config,"base"): 
      articles_list_path += "/articles_list/"
    else: 
      articles_list_path += config["base"]

    if not os.path.exists(articles_list_path):
      os.makedirs(articles_list_path)

    if not hasattr(config,"filename"): 
      articles_list_filename = "articles_list"
    else: 
      articles_list_filename = config["fliename"]
     
    articles_total_count = len(generator.articles)
    if "count" in config:
      articles_list_page_count = config['count']
      file_num = 1
    else: 
      articles_list_page_count = articles_total_count
      file_num = 0
   
    print "articles list page count: " + str(articles_list_page_count)
    counter = 1
    articles_list = [] 
    for article in generator.articles:
      articles_list.append({
        "title":article.title,
        "summary":article.summary
      })
      if counter % articles_list_page_count == 0:
        with open(articles_list_path + articles_list_filename  + str(file_num) + '.json','w') as outfile: 
          outfile.write(unicode(json.dumps(articles_list)))
        file_num += 1
        articles_list = []
      counter += 1

def register():
    signals.article_generator_finalized.connect(create_articles_list)
