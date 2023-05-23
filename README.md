# ows_searchapi
Python API for searching on a Lucene index (written with Django)

## Installation
1. Install Django and the required dependencies, by running ```pip install django djangorestframework whoosh```

## Running the API
1. Enter into `./lucene_search_api` and copy the lucene index directory here.
2. Start the Django development server, by running ```python manage.py runserver```

## Queries
- Open the localhost development server, and add the path ```/api/search/?q=<insert_query_here>``` to make queries to the search API.