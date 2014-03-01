import unittest
import settings
import file_manager
import creator 
from pelican.settings import read_settings
from mock import MagicMock

# Mocks 
class DummyParser():
  def generate_output(self,article,templates):
    return True

class DummyArticle(): 
  def __init__(self,title,summary,unknown):
  	self.title = title
  	self.summary = summary 
  	self.unknown = unknown

# Here's our "unit tests".
class CreatorTests(unittest.TestCase):
  def setUp(self):
    fm = file_manager.FileManager()
    fm.save_file = MagicMock(return_value=True)
    self.creator = creator.Creator(fm)
    self.parser = DummyParser()

  def tearDown(self): 
    self.creator = None

  def testCreatorDefaultSettings(self):
    articles = [
      DummyArticle('title 1', 'summary 1', 'unknown 1'),
      DummyArticle('title 2', 'summary 2', 'unknown 2'),
    ]
    articles_total_count = len(articles)
    articles_list_settings = self.getSettings(articles_total_count)
    actual = self.creator.run(articles ,articles_list_settings, self.parser)
    expected = [
      {'title':'title 1', 'summary':'summary 1'},
      {'title':'title 2', 'summary':'summary 2'},
    ]
    self.assertItemsEqual(sorted(actual), sorted(expected))

  def getSettings(self, articles_total_count):
    s = settings.ArticlesListSettings()
    s.create_articles_list_directory = MagicMock(return_value=True)
    override_settings = {'OUTPUT_PATH':'/output/path'}
    pelican_settings = read_settings(override=override_settings) 
    articles_list_settings = s.get(pelican_settings,articles_total_count)
    return articles_list_settings

def main():
  unittest.main()

if __name__ == '__main__':
  main()