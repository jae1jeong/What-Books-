
from django.shortcuts import render
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote
import json
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def search_book(request):

    if request.method == 'GET':

        CLIENT_ID = "I4IvQbMJzyTRa2L0TDp0"
        CLIENT_SECERET = "qtVKgFeiLw"
        search_word = request.GET.get('query')

        encText = quote("{}".format(search_word))

        req = Request(
            'https://openapi.naver.com/v1/search/book?query=' + encText)
        req.add_header('X-Naver-Client-Id', CLIENT_ID)
        req.add_header('X-Naver-Client-Secret', CLIENT_SECERET)

        response = urlopen(req)
        res_status = response.getcode()
        if (res_status == 200):
            # print(res_status)
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            print(result)
            items = result.get('items')

            context = {
                'items': items
            }

            return render(request, 'booklist.html', context=context)


def index(request):

    return render(request, 'bookform.html')
