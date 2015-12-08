from PyPDF2 import PdfFileReader

class Parser:
    def __init__(self):
        document = PdfFileReader(open("vhsl-districts-01.pdf", "rb"))
        pages = []
        for i in range(0, document.getNumPages()):
            pages.append(document.getPage(i))

        text = str(pages[0].extractText()).replace('\n', ' ')
        wordList = text.split()

        ans = []
        answers = []
        inAnswer = False
        for w in wordList:
            if set('[') & set(w):
                answers.append(ans)
                ans = []
                inAnswer = False
            if inAnswer == True:
                ans.append(w)
            if w == "ANSWER:":
                inAnswer = True

        print(answers)

start = Parser()