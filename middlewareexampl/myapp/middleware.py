# class ExecutionFlowMiddleware(object):
#     def __init__(self,get_response):
#         print("Init Method Execution")
#         self.get_response=get_response

#     def __call__(self, request):
#         print("PreProcessing of  a request")
#         response=self.get_response(request)
#         print("Post processing of a request")
#         return response

from django.http import HttpResponse      
        

class AppMaintainenceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        # response=self.get_response(request)
        # return response
        return HttpResponse('<h1>Currently under maintainence try againg later</h1>')