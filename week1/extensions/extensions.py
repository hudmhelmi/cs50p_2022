filename = input("File name: ")
filename = filename.strip().lower().split(".")
if filename[-1] == "gif":
    print("image/gif")
elif filename[-1] == "jpg":
    print("image/jpeg")
elif filename[-1] == "jpeg":
    print("image/jpeg")
elif filename[-1] == "png":
    print("image/png")
elif filename[-1] == "pdf":
    print("application/pdf")
elif filename[-1] == "txt":
    print("text/plain")
elif filename[-1] == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
