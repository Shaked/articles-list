Pelican Articles List
====================

[![Build Status](https://travis-ci.org/Shaked/articles_list.png)](https://travis-ci.org/Shaked/articles_list)

Pelican static web generator plugin that generates a file/files containing articles list with different parameters. 

This will allow the ability to set up ajax requests and together with that the ability to support endless scrolling 

### Requirements (Tested with)

- Python 2.7.5
- Pelican 3.3.0

#### Unit test
- [Mock - Mocking and Testing Library](http://www.voidspace.org.uk/python/mock/), Installation (pip): ```sudo pip install -U mock```
- [Nose](https://nose.readthedocs.org/en/latest/), Installation (pip): ```pip install nose```
- [Coverage](http://nedbatchelder.com/code/coverage/) Installation (pip): ```pip install coverage```

### Configuration

In order to override the default configuration a variable called ```ARTICLES_LIST``` has to be created inside ```pelicanconf.py```

The available settings are: 

| Name          | Description   | Type   | Default       | Example | 
| ------------- |:-------------:| ------:|--------------:|--------:|
| output_path   | Ability to use another root instead of the default one | string | OUTPUT_PATH   |  "/path/to/output" |
| base          | Base path of where the files will be created      | string | /articles_list| "/list/of/articles" |
| filename      | Base name for the files that will be created      | string | articles_list |  "list" |
| count_per_page| count of articles per file | int    | len(articles) | 10 |
| article_attrs | Pelican's article available attributes | array  | ['title', 'summary'] | ['title'] |
| is_rendered_html | Renders a template and appends *html* attribute to returned JSON | bool | False | True |
| templates | templates to render | dict | { 'article_summary.html': 'generated/file.html' } | {'sum.html': 'generated/file.html' } |
  
Example (*pelicanconf.py*):

```
  ... 
  ARTICLES_LIST = {'count': 2, 'filename': 'some_other_name'}
  ...
```
