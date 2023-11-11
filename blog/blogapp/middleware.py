def blog_middleware(get_response):

    print("Code need for initialization and is executed only once")

    def my_middleware(request):
        print("Request-Code executed before view function is called")
        res=get_response(request)
        print(res)
        print("Code to be executed after view function is called")

        return res 
    
    return my_middleware