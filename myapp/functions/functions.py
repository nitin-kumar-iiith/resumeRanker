def handle_uploaded_file(f):  
#change f.name as userID to store pdf file as user ID
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
