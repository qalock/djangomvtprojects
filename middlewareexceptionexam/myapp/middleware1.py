from django.http import HttpResponse

class FirstClassMiddleware(object):

    def __init__(self,get_response):
        print('Init method from first class')
        self.get_response=get_response

    def __call__(self, request):
        print('PreRequest from First middleware')
        response=self.get_response(request)
        print('Post Request from first middleware')
        return response