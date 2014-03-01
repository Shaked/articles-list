"""
Article list generator plugin for Pelican
================================

The idea is to generate a (json) file to be able to communicate togehter with Ajax calls
This will allow creating single page endless scroll without the need of using server side files
"""
from pelican import signals
from tempfile import mkdtemp

import html_parser
import settings
import os,io,json
import math
import pprint 

def parser_factory(type, settings):
  if html_parser.TYPE_HTML == type: 
    return html_parser.Parser(settings)

def save_files(articles_list_full_path,file_num,articles_list): 
  with open(articles_list_full_path + str(file_num) + '.json','w') as outfile: 
    outfile.write(unicode(json.dumps(articles_list)))

def articles_list(generator): 
    pelican_settings = generator.settings
    parser = parser_factory(html_parser.TYPE_HTML, pelican_settings)
    articles_total_count = len(generator.articles)
    s = settings.ArticlesListSettings()
    articles_list_settings = s.get(pelican_settings, articles_total_count)
    articles_list_settings['articles_total_count'] = articles_total_count
    create(generator, articles_list_settings, parser)

def create(generator, articles_list_settings, parser): 
    file_num = articles_list_settings['file_num']
    counter = 1
    articles_list = [] 
    html = ''
    for article in generator.articles:
      values = {}
      if True == articles_list_settings['is_rendered_html']:
        values['html'] = parser.generate_output(article,articles_list_settings['templates'])

      for key in articles_list_settings['article_attrs']: 
        values[key] = getattr(article,key)
    
      articles_list.append(values)
      if (counter % articles_list_settings['count_per_page'] == 0) or ((articles_list_settings['articles_total_count'] - counter) == 0):
        save_files(articles_list_settings['full_path'],file_num,articles_list)
        file_num += 1
        articles_list = []
      counter += 1

def register():
    signals.article_generator_finalized.connect(articles_list)
