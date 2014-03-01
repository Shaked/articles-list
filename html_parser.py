from tempfile import mkdtemp
from pelican.generators import TemplatePagesGenerator
from pelican.writers import Writer

import os

TYPE_HTML = "html"

class Parser():
    def __init__(self,settings):
      self.settings = settings 
      self.output_path = mkdtemp('articles_list_template')

    def __enter__(self):
        return self

    def __exit__(self):
        rmtree(self.output_path)

    def generate_output(self,article,templates):
      settings = self.settings
      settings['TEMPLATE_PAGES'] = templates

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