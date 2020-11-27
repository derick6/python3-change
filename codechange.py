import base64
from urllib.parse import quote, unquote
import html
def base64encode():
    a = input('请输入明文：')
    a = str(base64.b64encode(a.encode("utf-8")), "utf-8")
    print(a)

def base64decode():
    try:
        a = input('请输入密文：')
        a = a+'=='
        a = str(base64.b64decode(a), "utf-8")
        print(a)
    except:
        print('恕在下不能解码：')


def asciiencode():
    try:
        a = input('请输入想要转换的字符：')
        a = ord(a)
        print(a)
    except:
        print('恕在下不能转换：')


def asciidecode():
    try:
        a = int(input('请输入ascii码值：'))
        a = chr(a)
        print(a)
    except:
        print('恕在下不能转换：')

def uniencode():
    b = input('请输入要转的内容：')
    print(b.encode("unicode_escape"))


def unidecode():
    b = input('请输入unicode编码')
    print(b.encode('utf-8').decode("unicode_escape"))


def urlencode():
    a = input('请输入：')
    print(quote(a, 'utf-8'))


def urldecode():
    a = input('请输入需要解码的：')
    print(unquote(a, 'utf-8'))


def htmlencode():
    a = input('请输入需要编码的内容：')
    a = html.escape(a)
    print(a)


def htmldecode():
    a = input('请输入需要解码的内容：')
    a = html.unescape(a)
    print(a)

def chose():
    print('''
    1. 编码
    2. 解码   
        ''')


def main():
    print('''
    选择您的编码方式：
    1.Base64
    2.Ascii
    3.unicode
    4.url编码
    5.html编码
    6.退出
    ''')
    a = input('请选择：')
    if a == '1':
        chose()
        b = input('请选择')
        if b == '1':
            base64encode()
        elif b == '2':
            base64decode()
    if a == '2':
        chose()
        b = input('请选择')
        if b == '1':
            asciiencode()
        elif b == '2':
            asciidecode()
    if a == '3':
        chose()
        b = input('请选择')
        if b == '1':
            uniencode()
        elif b == '2':
            unidecode()
    if a == '4':
        chose()
        b = input('请选择')
        if b == '1':
            urlencode()
        elif b == '2':
            urldecode()
    if a == '5':
        chose()
        b = input('请选择：')
        if b == '1':
            htmlencode()
        elif b == '2':
            htmldecode()
    if a=='6':
        exit()
if __name__ == "__main__":
    while True:
        main()
