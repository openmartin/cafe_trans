# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

class BaiduTranslation():
    
    def __init__(self):
        self.api_addr = ' http://openapi.baidu.com/public/2.0/bmt/translate'
        self.api_key = '78wRtVrdXQDxEem9D6XvQFLu'
        
    def trans(self, frm, to, src):
        pass
    
    def trans_en_zh(self, src, isquote=False):
        
        if isquote == False:
            api_para_dict = {"client_id":self.api_key,"q":src,
                         "from":"en", "to":"zh"}
        else:
            api_para_dict = {"client_id":self.api_key,"q":src,
                         "from":"en", "to":"zh"}
            
        api_para = urllib.urlencode(api_para_dict)
        url = self.api_addr + '?' + api_para
        
        api_request = urllib2.Request(url)
        rsp_json = urllib2.urlopen(api_request, timeout=10).read()
        print rsp_json
        
        
        decoded = json.loads(rsp_json)
        dst = str(decoded["trans_result"][0]["dst"])
        
        return dst
    
if __name__ == '__main__':
    bt = BaiduTranslation()
    dst = bt.trans_en_zh("I'm so happy")
    print dst
        