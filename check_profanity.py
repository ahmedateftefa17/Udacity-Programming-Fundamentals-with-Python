import urllib

def read_text():
    myfile = open(r"path/to/file.txt")
    content = myfile.read()
    print content
    myfile.close()
    check_profanity(content)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    response = connection.read()
    if "true" in response:
        print "Profanity Alert!!!"
    elif "false" in response:
        print "You're good to go."
    else:
        print "Connection fails"
    connection.close()
    
read_text()

