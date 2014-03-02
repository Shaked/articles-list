import unittest
import settings
import file_manager
import html_parser
import creator
from pelican.settings import read_settings
from mock import MagicMock


# Mocks
class DummyArticle():
    def __init__(self, title, summary, unknown):
        self.title = title
        self.summary = summary
        self.unknown = unknown


# Here's our "unit tests".
class CreatorTests(unittest.TestCase):
    def setUp(self):
        self.parser = html_parser
        self.parser.generate_output = MagicMock(return_value='')

    def tearDown(self):
        self.creator = None

    def testCreator(self):
        articles = [
            DummyArticle('title 1', 'summary 1', 'unknown 1'),
            DummyArticle('title 2', 'summary 2', 'unknown 2'),
        ]
        data = [{
            'name': 'basic settings test',
            'articles': articles,
            'settings': {},
            'expected': {
                1: [{'title': 'title 1', 'summary': 'summary 1'},
                    {'title': 'title 2', 'summary': 'summary 2'}]}
        }, {
            'name': 'rendered html test',
            'articles': articles,
            'settings': {'is_rendered_html': True},
            'expected': {
                1: [{'title': 'title 1', 'summary': 'summary 1', 'html': ''},
                    {'title': 'title 2', 'summary': 'summary 2', 'html': ''}]}
        }, {
            'name': 'file division number test',
            'articles': articles+[DummyArticle('title 3', 'summary 3', 'unknown 3')],
            'settings': {'count_per_page': 2},
            'expected': {
                1: [{'title': 'title 1', 'summary': 'summary 1'},
                    {'title': 'title 2', 'summary': 'summary 2'}],
                2: [{'title': 'title 3', 'summary': 'summary 3'}]}
        }]
        for item in data:
            print('Running test: ' + item['name'])
            self._testCreator(item['articles'], item['settings'], item['expected'])

    def _testCreator(self, articles, articles_list_settings_override, expected):
        articles_total_count = len(articles)
        articles_list_settings = self.getSettings(articles_total_count, articles_list_settings_override)
        actual = self.getCreator().run(articles, articles_list_settings, self.parser)
        self.assertEqual(sorted(actual), sorted(expected))

    def getSettings(self, articles_total_count, articles_list_settings_override):
        s = settings.ArticlesListSettings()
        s.create_articles_list_directory = MagicMock(return_value=True)
        override_settings = {'OUTPUT_PATH': '/output/path'}
        pelican_settings = read_settings(override=override_settings)
        articles_list_settings = s.get(pelican_settings, articles_total_count)
        articles_list_settings.update(articles_list_settings_override)
        return articles_list_settings

    def getCreator(self):
        fm = file_manager.FileManager()
        fm.save_file = MagicMock(return_value=True)
        return creator.Creator(fm)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
