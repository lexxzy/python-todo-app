filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for i in filenames:
    file = open(f"./files/{i}", 'w')
    file.write("Hello")