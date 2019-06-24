# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {0[0]} > {0[1]}".format(attr))
    def handle_endtag(self, tag):
        #print("End   :", tag)
        pass
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {0[0]} > {0[1]}".format(attr))
# instantiate the parser and fed it some HTML
whole_text = ''.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(whole_text)
