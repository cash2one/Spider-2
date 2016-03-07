import re




pattern_cailiao=re.compile(r"<p>(%s.*?|%s.*?|%s.*?)</p>"%(cailiao1,cailiao2,cailiao3),re.S)

for match in re.finditer(pattern_cailiao,content):
            cailiao=match.group(1)
            file1.write(cailiao)
            file1.write("\n")