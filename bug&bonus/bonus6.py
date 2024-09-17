contents = ["The name os this doc is the title","The name of this report is the title","The General names for this files i the title"]
filenames = ["doc.txt","report.txt","presentation"]

for contents, filenames in zip(contents, filenames):
    files = open(f"./files/{filenames}", 'w')
    files.write(contents)