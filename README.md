Pelican Articles List
====================

Pelican static web generator plugin that generates a file/files containing articles list with different parameters. 

This will allow the ability to set up ajax requests and together with that the ability to support endless scrolling 

### Requirements (Tested with)

- Python 2.7.5
- Pelican 3.3.0
- [Mock - Mocking and Testing Library](http://www.voidspace.org.uk/python/mock/), Installation is easy: ```sudo pip install -U mock``` 

### Configuration

In order to override the default configuration a variable called ```ARTICLES_LIST``` has to be created inside ```pelicanconf.py```

The available settings are: 

- **output_path** - Ability to use another root instead of the default one (default: the output directory, OUTPUT_PATH)
- **base** - Base path of where the files will be created (default: */articles_list/*)
- **filename** - Base name for the files that will be created (default: *articles_list*)
- **count** - count of articles per file (default: *length of all articles togehter*) 
  
Example:

```
  pelicanconf.py
  ARTICLES_LIST = { 'count':2, 'filename':'some_other_name' }
```
