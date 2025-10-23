from django.http import HttpResponse

class SampleMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        return HttpResponse('<h1>Currently we are facing some technical issue, please try after some time.!!!</h1>')