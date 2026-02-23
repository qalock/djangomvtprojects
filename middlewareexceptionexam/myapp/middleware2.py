from django.http import HttpResponse

class SecondClassMiddleware(object):

    def __init__(self,get_response):
        print('Init method from second class')
        self.get_response=get_response

    def __call__(self, request):
        print('PreRequest from second middleware')
        response=self.get_response(request)
        print('Post Request from second middleware')
        return response