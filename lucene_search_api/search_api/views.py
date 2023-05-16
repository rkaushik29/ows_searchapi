from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from whoosh import index
from whoosh.qparser import QueryParser

# Create your views here.

@csrf_exempt
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')

        # Open the index directory
        ix = index.open_dir("/Users/rohitkaushik/dev/tugraz/ows_searchapi/lucene_search_api/cranfield")

        # Create a QueryParser to parse the user's search query
        qp = QueryParser("content", schema=ix.schema)

        # Parse the user's query
        q = qp.parse(query)

        # Create an IndexSearcher and get the top 10 search results
        with ix.searcher() as searcher:
            results = searcher.search(q, limit=10)

        # Serialize the search results to a JSON response
        response = results
        return JsonResponse(response)

    return JsonResponse({'error': 'Invalid request method'})