filenames = ['doc.txt','presentation.txt','report.txt']
for i in filenames:
    file = open(f"./files/{i}", 'r')
    content = file.read()
    print(content)
