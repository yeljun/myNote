# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:21:16 2018

@author: Administrator
"""

s="""<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
		</p>
		<p class="contents">
    		Two tigers two tigers run fast
		</p>
</div>
<div class="animal">
   <p class="name">
        <a title="Rabbit"></a>
		</p>
		<p class="contents">
					Small white rabbit white and white
		</p>
</div>
"""
#			[("Tiger","Two tigers two tigers run fast"),
#			("Rabbit","Small white rabbit white and white")]
import re
p3 = re.compile("""class="animal".*?title="(.*?)"></a>.*?class="contents">\s+(.*?)\s+</p>""",re.S)
ulist = p3.findall(s)
for x in ulist:
    print("title:",x[0]," aaa:",x[1])

#p = re.compile(r"title=\"([A-Z][a-z]+)\"")
#print(p.findall(s))
#p2 = re.compile(r"contents\">\s+(.*?)\s+</p>",re.S)
#print(p2.findall(s))









