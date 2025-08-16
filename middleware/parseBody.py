import json

def parseBody(request):
    reqarr = request.split("\r\n\r\n")
    if len(reqarr) > 0:
        decoder = json.JSONDecoder()
        return decoder.decode(reqarr[1])
    return None