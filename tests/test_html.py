from html.parser import HTMLParser
import sys
import pytest

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise ValueError(f"Mismatched closing tag </{tag}>")

def test_hello_html_is_valid():
    parser = MyHTMLParser()
    with open('hello.html', 'r') as f:
        parser.feed(f.read())
    assert not parser.stack
