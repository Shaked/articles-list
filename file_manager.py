import json


class FileManager():
    def __init__(self):
        self.saved_articles = {}

    def save(self, articles_list_full_path, file_num, articles_list):
        self.save_file(articles_list_full_path, file_num, articles_list)
        self.saved_articles[file_num] = articles_list

    def save_file(self, articles_list_full_path, file_num, articles_list):
        file = articles_list_full_path + str(file_num)
        with open(file + '.json', 'w') as outfile:
            outfile.write(json.dumps(articles_list))

    def get_saved_articles(self):
        return self.saved_articles
