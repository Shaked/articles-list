"""
Article list generator plugin for Pelican
================================

The idea is to generate a (json) file to be able to communicate togehter with Ajax calls
This will allow creating single page endless scroll without the need of using server side files
"""
from pelican import signals
from tempfile import mkdtemp
from pelican.generators import TemplatePagesGenerator
from pelican.writers import Writer


import os,io,json
import math
import pprint 

class ParseArticlesListTemplate():

    def __init__(self,settings):
      self.settings = settings 
      self.output_path = mkdtemp('articles_list_template')

    def __enter__(self):
        return self

    def __exit__(self):
        rmtree(self.output_path)

    def generate_output(self,article):
      settings = self.settings
      settings['TEMPLATE_PAGES'] = {
        'article_summary.html': 'generated/file.html'
      }

      generator = TemplatePagesGenerator(
          context={'article': article}, settings=settings,
          path=settings['PATH'], theme=settings['THEME'], output_path=self.output_path)

      writer = Writer(self.output_path, settings=settings)
      generator.generate_output(writer)

      output_path = os.path.join(self.output_path, 'generated', 'file.html')

      # output content is correct
      with open(output_path, 'r') as output_file:
          rendered_html = output_file.read()

      return rendered_html

def save_files(articles_list_full_path,file_num,articles_list): 
  with open(articles_list_full_path + str(file_num) + '.json','w') as outfile: 
    outfile.write(unicode(json.dumps(articles_list)))

def create_articles_list(generator): 
    config = generator.settings.get('ARTICLES_LIST')

    if 'output_path' in config:
      articles_list_path = config['output_path']
    else: 
      articles_list_path = generator.settings.get('OUTPUT_PATH')

    if not hasattr(config,'base'): 
      articles_list_path += '/articles_list/'
    else: 
      articles_list_path += config['base']

    if not os.path.exists(articles_list_path):
      os.makedirs(articles_list_path)

    if not hasattr(config,'filename'): 
      articles_list_filename = 'articles_list'
    else: 
      articles_list_filename = config['fliename']
     
    articles_total_count = len(generator.articles)
    if 'count' in config:
      articles_list_page_count = config['count']
      file_num = 1
    else: 
      articles_list_page_count = articles_total_count
      file_num = 0

    if not 'article_attrs' in config:
      article_attrs = ['title','summary']
    else: 
      article_attrs = config['article_attrs']
    
    if not 'rendered_html' in config:
      rendered_html = False 
    else: 
      rendered_html = config['rendered_html'] 

    articles_list_full_path = articles_list_path + articles_list_filename
    counter = 1
    articles_list = [] 
    t = ParseArticlesListTemplate(generator.settings)
    html = ''
    for article in generator.articles:
      values = {}
      if True == rendered_html:
        values['html'] = t.generate_output(article)

      for key in article_attrs: 
        values[key] = getattr(article,key)
    
      articles_list.append(values)
      if (counter % articles_list_page_count == 0) or ((articles_total_count - counter) == 0):
        save_files(articles_list_full_path,file_num,articles_list)
        file_num += 1
        articles_list = []
      counter += 1

def register():
    signals.article_generator_finalized.connect(create_articles_list)
