# The server starts and loads an 'application' callable provided by the web framework/application
# The server reads a request
# The server parses the request
# Builds an 'environ' dictionary using the request data
# Calls the 'application' callable with the 'environ' dictionary and a 
# 'start_response' callable as parameters and gets back a response body
# Then, the server constructs an HTTP response using the data returned by
# the call to the 'application' object and the status and response headers set
# by the 'start_response' callable
# And finally, the server transmits the HTTP response back to the client


def app(environ, start_response):
    """A barebones WSGI application.

    This is a starting point for your own Web framework :)
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world from a simple WSGI application!\n']


"""
WSGIServer: Serving HTTP on port 8888 ...

< GET /hello HTTP/1.1
< Host: localhost:8888
< Connection: keep-alive
< Upgrade-Insecure-Requests: 1
< User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36
< Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
< Accept-Encoding: gzip, deflate, sdch
< Accept-Language: en-US,en;q=0.8
<

> HTTP/1.1 200 OK
> Content-Type: text/plain
> Date: Tue, 31 Mar 2015 12:54:48 GMT
> Server: WSGIServer 0.2
>
> Hello world from a simple WSGI application!
"""
