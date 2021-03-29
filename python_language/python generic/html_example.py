from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for atr in attrs:
            print(f'-> {atr[0]} > {atr[1]}')
    def handle_endtag(self, tag):
        print(f'End   : {tag}')
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for atr in attrs:
            print(f'-> {atr[0]} > {atr[1]}')
        
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(f">>> Single-line Comment\n{data}")
    def handle_data(self, data):
        if data.strip():
            print(f">>> Data\n{data}")

if __name__ == '__main__':
    n = int(input())
    s = ''
    for i in range(n):
        s += input()       
    parser = MyHTMLParser()
    parser.feed(s)

"""
Input 
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
Your Output (stdout)
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
Expected Output

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html

"""
