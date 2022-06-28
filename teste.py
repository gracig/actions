import re

readme=open('README.md', encoding='UTF-8').read()
pattern = re.compile(r"(.*?)<!--BEGIN_DOC-->.*<!--END_DOC-->(.*)", flags = ( re.DOTALL | re.MULTILINE ) )
if pattern.match(readme):
    print("Found doc")
    readme = pattern.sub(r"\1<!--BEGIN_DOC-->\nSecond Text\n<!--END_DOC-->\2", readme)
else:
    print("Did not find doc")
    readme = "{}\n<!--BEGIN_DOC-->\nFirst Text\n<!--END_DOC-->\n".format(readme)

open("README.md", 'wb').write(readme.encode("utf-8"))

