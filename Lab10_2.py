def getTextFromFile(path):
    with open(path,) as f:
        text = f.read();
        if len(text) == 0:
            raise Exception("Empty file");
        return text


try:
    text = getTextFromFile("./resources/FileText.txt");
    print(text);
    text = getTextFromFile("./resources/emptyFile.txt");
    print(text);
except Exception as e:
    print(e)
