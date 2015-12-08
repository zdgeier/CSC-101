from docx import *

class DocxReader:
    def __init__(self):
        document = Document('vhsl-districts-01.docx')

        answers = []
        inAnswer = False

        for paragraph in document.paragraphs:
            for word in paragraph.runs:
                if '[' in word.text:
                    #print('==========')
                    inAnswer = False
                if inAnswer:
                    #print(word.text)
                    answers.append(word.text)
                if 'ANSWER' in word.text:
                    #print('====!====')
                    inAnswer = True

        print(answers)

start = DocxReader()