"""
Article list generator plugin for Pelican
================================

The idea is to generate a (json) file to be able to communicate togehter with Ajax calls
This will allow creating single page endless scroll without the need of using server side files
"""

from pelican import signals

import html_parser
import settings
import creator
import file_manager


def parser_factory(type, settings):
    if html_parser.TYPE_HTML == type:
        return html_parser.Parser(settings)


def articles_list(generator):
    pelican_settings = generator.settings
    parser = parser_factory(html_parser.TYPE_HTML, pelican_settings)
    articles_total_count = len(generator.articles)
    s = settings.ArticlesListSettings()
    articles_list_settings = s.get(pelican_settings, articles_total_count)
    articles_list_settings['articles_total_count'] = articles_total_count
    al = creator.Creator(file_manager.FileManager())
    al.run(generator.articles, articles_list_settings, parser)


def register():
    signals.article_generator_finalized.connect(articles_list)
