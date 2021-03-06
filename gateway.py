# import os
# import sys
# from app import simple_app
#
# def wsgi_to_bytes(s):
#     return s.encode()
#
# def run_with_cgi(application):
#     environ = dict(os.environ.items())
#     environ['wsgi.input'] = sys.stdin.buffer
#     environ['wsgi.errors'] = sys.stderr
#     environ['wsgi.version'] = (1,0)
#     environ['wsgi.multithread'] = False
#     environ['wsgi.multiprocess'] = True
#     environ['wsgi.run_once'] = True
#
#     if environ.get('HTTPS','off') in ('on','1'):
#         environ['wsgi.url_scheme'] = 'https'
#     else:
#         environ['wsgi.url_scheme'] = 'http'
#
#     headers_set = []
#     headers_sent = []
#
#     def write(data):
#         out = sys.stdout.buffer
#
#         if not headers_set:
#             raise AssertionError("write() before start_response()")
#         elif not headers_sent:
#             # 在输出第一行数据之前，先发送响应头
#             status,response_headers = headers_sent[:] = headers_set
#             out.write(wsgi_to_bytes('Status: %s\r\n' % status))
#             for header in response_headers:
#                 out.write(wsgi_to_bytes('%s: %s\r\n' % header))
#             out.write(wsgi_to_bytes('\r\n'))
#
#         out.write(data)
#         out.flush()
#
#     def start_response(status,response_headers,exc_info=None):
#         if exc_info:
#             try:
#                 if headers_sent:
#                     # 如果已经发送了header，则重新抛出原始异常信息
#                     raise (exc_info[0], exc_info[1], exc_info[2])
#             finally:
#                 exc_info = None  # 避免循环引用
#         elif headers_set:
#             raise AssertionError("Headers already set!")
#         headers_set[:] = [status,response_headers]
#         return write
#     result = application(environ,start_response)
#
#     try:
#         for data in result:
#             if data:  # 如果没有body数据，则不发送header
#                 write(data)
#         if not headers_sent:
#             write('')  # 如果body为空，则不发送header
#     finally:
#         if hasattr(result,'close'):
#             result.close()
#
# if __name__=='__main__':
#     run_with_cgi(simple_app)

import os
import sys

from app import simple_app


def run_with_cgi(application):
    environ = dict(os.environ.items())
    environ['wsgi.input'] = sys.stdin
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True

    if environ.get('HTTPS', 'off') in ('on', '1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    def write(data):
        if not headers_set:
            raise AssertionError("write() before start_response()")

        elif not headers_sent:
            # Before the first output, send the stored headers
            status, response_headers = headers_sent[:] = headers_set
            sys.stdout.write('Status: %s\r\n' % status)
            for header in response_headers:
                sys.stdout.write('%s: %s\r\n' % header)
            sys.stdout.write('\r\n')

        sys.stdout.write(data)
        sys.stdout.flush()

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    # Re-raise original exception if headers sent
                    raise (exc_info[0], exc_info[1], exc_info[2])
            finally:
                exc_info = None     # avoid dangling circular ref
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status, response_headers]
        return write

    result = application(environ, start_response)
    try:
        for data in result:
            if data:    # don't send headers until body appears
                write(data)
        if not headers_sent:
            write('')   # send headers now if body was empty
    finally:
        if hasattr(result, 'close'):
            result.close()

if __name__ == '__main__':
    run_with_cgi(simple_app)



