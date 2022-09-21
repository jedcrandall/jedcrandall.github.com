with open ('slides.pdf', mode="rb") as myfile:
    message_string=myfile.read()
    print(message_string)
    myfile.close
