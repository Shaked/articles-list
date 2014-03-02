import unittest
import settings
from pelican.settings import read_settings
from mock import MagicMock


# Here's our "unit tests".
class ArticlesListSettingsTests(unittest.TestCase):
    def setUp(self):
        self.settings = settings.ArticlesListSettings()
        self.settings.create_articles_list_directory = MagicMock(return_value=True)

    def tearDown(self):
        self.settings = None

    def testGet(self):
        articles_total_count = 1
        data = [{
            'name': 'defaults',
            'override_settings': {},
            'expected': {
                'path': '/articles_list/',
                'filename': 'articles_list',
                'full_path': '/articles_list/articles_list',
                'count_per_page': articles_total_count,
                'articles_total_count': articles_total_count,
                'article_attrs': ['title', 'summary'],
                'is_rendered_html': False,
                'templates': {
                    'article_summary.html': 'generated/file.html'}
                },
        }, {
            'name': 'change articles list settings',
            'override_settings': {
                'ARTICLES_LIST': {
                    'output_path': '/some/path/to/output',
                    'base': '/list',
                    'filename': 'foo_list',
                    'count_per_page': 10,
                    'article_attrs': ['title'],
                    'is_rendered_html': True,
                    'templates': {
                        'summary.html': 'generated/f.html'}
                }
            },
            'expected': {
                'path': '/some/path/to/output/list/',
                'filename': 'foo_list',
                'full_path': '/some/path/to/output/list/foo_list',
                'count_per_page': 10,
                'articles_total_count': articles_total_count,
                'article_attrs': ['title'],
                'is_rendered_html': True,
                'templates': {
                    'summary.html': 'generated/f.html'}
                },
        }, ]

        for item in data:
            print('Testing: ' + item['name'])
            self._testGet(item['override_settings'], item['expected'], articles_total_count)

    def _testGet(self, override_settings, expected, articles_total_count):
        pelican_settings = read_settings(override=override_settings)
        actual = self.settings.get(pelican_settings, articles_total_count)
        self.assertEqual(sorted(actual), sorted(expected))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
