#!/usr/bin/env python
# encoding: utf-8

import urllib2
import requests
from urlparse import urljoin


# req = urllib2.Request()
# req.add_header()
def get_upload_link(url, token):
    resp = requests.get(
        url, headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    return resp.json()


values = {
    'username': 'xuhui@chinadaas.com',
    'password': '13436567526'
}
server = 'http://192.168.61.9:8000'

repo_id = "2a4f443a-7d42-4006-832b-72321dbc78ce"

url_partten = {
    'ping': '/api2/ping',   #health接口
    'token': '/api2/auth-token/',   #获取token的接口
    'repos': '/api2/repos/',    #获取library的id
    'dir': '/api2/repos/{repo_id}/dir/?p=/'.format(repo_id=repo_id),    #获取dir的入口
    'get_upload_link': '/api2/repos/{repo_id}/upload-link/'.format(repo_id=repo_id),    # 获得上传地址
}
token = "fe1a6e49a37cea089b2298a308d1c43ec652c4ef"

token_headers = {'Authorization': 'Token ' + token}

if __name__ == '__main__':
    get_uri = urljoin(server, url_partten['get_upload_link'])
    upload_link = requests.get(get_uri, headers=token_headers).json()
    print upload_link
    ipath = 'F:\information\jqueryApi\徐晖10月份外出记录表.xls'
    uipath = unicode(ipath, "utf8")
    response = requests.post(upload_link,
                             data={'filename': u'徐晖10月份外出记录表.xls', 'parent_dir': '/'},
                             files={'file': (
                             '徐晖10月份外出记录表.xls', open(uipath, 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})},

                             headers=token_headers
                             )
    print response.text
