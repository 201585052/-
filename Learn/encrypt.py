# -*- coding: utf-8 -*-

# python 内存中用unicode 编码，windows:gb2312,linux:utf8
# encode使用前必须是unicode字符串

import sys
print(sys.getdefaultencoding())



# py2

s = 'abc'
su = u'abc'
s.encode('utf8')
su.encode('utf8')
s = '垚垚'
su = u'垚垚'
s.encode('utf8')

# py3的升级就是前面不用加coding:utf8 的设定，因为他默认把所有的都看成unicode,所以字符串前面也不用加u了