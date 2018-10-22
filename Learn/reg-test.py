# -*- coding: utf-8 -*-

import re

'''
line = 'booooooobbby1234'
regex_str = ".*?(b.*?b).*"

# 可以考虑把第二个？去掉变成贪婪模式，去取匹配后的booooo...bbb
# 之前对正则表达式中的贪婪和非贪婪模式不是很理解，其实贪婪匹配有种取巧的理解方式就是
# 从字符串的右侧向左侧匹配，即最后一次匹配。
# ？指的是只匹配一次，因此他会引导贪婪模式，从取巧的角度说就是从左到右匹配
'''

'''
line = "18782902222"
regex_str = "(1[34578][0-9]{9})"
'''

'''
line = "你好"
regex_str = "([\u4e00-\u9fa5]+)"


match_obj = re.match(regex_str,line)
if match_obj:
    print (match_obj.group(1))
    print 'yes'
'''

