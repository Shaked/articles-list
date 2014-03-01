import os
class ArticlesListSettings(): 
	def get(self,pelican_settings, articles_total_count):
	    articles_list_settings = {} 
	    pelican_settings_articles_list = pelican_settings.get("ARTICLES_LIST")
	    if not pelican_settings_articles_list: 
	    	pelican_settings_articles_list = {} 

	    # Directory Path
	    if 'output_path' in pelican_settings_articles_list:
	      path = pelican_settings_articles_list['output_path']
	    else: 
	      path = pelican_settings.get('OUTPUT_PATH')

	    if 'base' in pelican_settings_articles_list: 
	      path += pelican_settings_articles_list['base']
	    else: 
	      path += '/articles_list/'

	    articles_list_settings['path'] = path
	    self.create_articles_list_directory(path)
	    # Filename 
	    if 'filename' in pelican_settings_articles_list:
	      filename = pelican_settings_articles_list['fliename']
	    else: 
	      filename = 'articles_list'

	    articles_list_settings['filename'] = filename
	    articles_list_settings['full_path'] = articles_list_settings['path'] + articles_list_settings['filename']

	    #articles count per page 
	    if 'count_per_page' in pelican_settings_articles_list:
	      count_per_page = pelican_settings_articles_list['count_per_page']
	    else: 
	      count_per_page = articles_total_count

	    articles_list_settings['count_per_page'] = count_per_page
	    articles_list_settings['articles_total_count'] = articles_total_count

	    # article attributes
	    if 'article_attrs' in pelican_settings_articles_list:
	      article_attrs = pelican_settings_articles_list['article_attrs']
	    else: 
	      article_attrs = ['title','summary']

	    articles_list_settings['article_attrs'] = article_attrs

	    # HTML rendering
	    if 'is_rendered_html' in pelican_settings_articles_list:
	      is_rendered_html = pelican_settings_articles_list['is_rendered_html'] 
	    else: 
	      is_rendered_html = False  
	    
	    articles_list_settings["is_rendered_html"] = is_rendered_html  

	    # templates @todo: check if its actually possible to render more than one template 
	    if 'templates' in pelican_settings_articles_list:
	      templates = {}
	    else:
	      templates = {
	        'article_summary.html': 'generated/file.html'
	      }

	    articles_list_settings["templates"] = templates
	    
	    return articles_list_settings
	   
	def create_articles_list_directory(self,path):
	  if not os.path.exists(path):
	      os.makedirs(path)

