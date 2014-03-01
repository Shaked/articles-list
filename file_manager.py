import json

class FileManager(): 
  def __init__(self):
  	self.saved_articles = []

  def save(self, articles_list_full_path,file_num,articles_list): 
    self.save_file()
    self.saved_articles += articles_list

  def save_file(self, articles_list_full_path,file_num,articles_list):
    with open(articles_list_full_path + str(file_num) + '.json','w') as outfile: 
      outfile.write(unicode(json.dumps(articles_list)))

  def get_saved_articles(self):
  	return self.saved_articles