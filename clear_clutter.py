import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":
        
    files = os.listdir()
    files.remove("clear_clutter.py")

    createIfNotExist('Images')
    createIfNotExist('Documents')
    createIfNotExist('Media')
    createIfNotExist('Others')
    createIfNotExist('Codes')
    createIfNotExist('Codes/websites')
    createIfNotExist('Codes/python')
    createIfNotExist('Codes/apps')

    imgExts = [".png", ".jpg", ".jpeg", ".gif"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", ".doc", ".pdf", ".ppt", ".pptx", ".xlsx", ".xls"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp4", ".mp3", ".flv", ".wav", ".avi"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    codeExts = [".py", ".html", ".css", ".js"]
    websites = [file for file in files if os.path.splitext(file)[1].lower() in [".html", ".css", ".js"]]
    python = [file for file in files if os.path.splitext(file)[1].lower() == ".py"]
    apps = [file for file in files if os.path.splitext(file)[1].lower() == ".exe"]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in codeExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Documents", docs)
    move("Media", medias)
    move("Codes/websites", websites)
    move("Codes/python", python)
    move("Codes/apps", apps)
    move("Others", others)
