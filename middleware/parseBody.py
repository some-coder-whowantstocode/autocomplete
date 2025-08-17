import json

from lib.logging import write

def parseBody(request):
    reqarr = request.split("\r\n\r\n")
    if len(reqarr) > 1:
        try:            
            decoder = json.JSONDecoder()
            return decoder.decode(reqarr[1])
        except json.JSONDecodeError as e :
            write(f"Error at middleware/parseBody.py: \n {e}")
            return None
    return None