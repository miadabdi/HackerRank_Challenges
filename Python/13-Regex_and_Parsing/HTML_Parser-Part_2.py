from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment\n" + data)
        else:
            print(">>> Single-line Comment\n" + data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data\n" + data)
  
html = ''.join([input().rstrip() + '\n' for i in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()
