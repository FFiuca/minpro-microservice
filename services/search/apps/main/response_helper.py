import sys, os
from rest_framework.response import Response

def response_builder(data:any, status:int):
    return Response({
        'status': status,
        'data': data
    }, status=status)

def message_error(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    # print('message_error', exc_type, exc_obj, exc_tb)
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
    print(fname)
    fname= fname[1]
    return "An exception of type {} occured: {}. {}. {}. {}".format(type(e).__name__, e, exc_type, fname, exc_tb.tb_lineno)
