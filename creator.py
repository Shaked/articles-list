class Creator():
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def run(self, articles, articles_list_settings, parser):
            file_num = 1
            counter = 1
            articles_list = []
            articles_total_count = articles_list_settings['articles_total_count']
            for article in articles:
                values = {}
                if True == articles_list_settings['is_rendered_html']:
                    values['html'] = parser.generate_output(
                        article,
                        articles_list_settings['templates']
                    )

                for key in articles_list_settings['article_attrs']:
                    values[key] = getattr(article, key)

                articles_list.append(values)
                if (
                    counter % articles_list_settings['count_per_page'] == 0
                ) or (
                    (articles_total_count - counter) == 0
                ):
                    self.file_manager.save(articles_list_settings['full_path'], file_num, articles_list)
                    file_num += 1
                    articles_list = []
                counter += 1
            return self.file_manager.get_saved_articles()
