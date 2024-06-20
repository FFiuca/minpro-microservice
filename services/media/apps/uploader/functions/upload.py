from django.core.files.storage import FileSystemStorage
from uploader.models import Files
import uuid
import os

class Upload():
    base_path = 'upload/'

    def __init__(self) -> None:
        pass

    def upload(self, files: list):
        uploaded_files = []
        fs = FileSystemStorage()

        if len(files)==0:
            raise Exception('files leng is zero')

        for f in files:
            print('this is f', f, f.name, dir(f), f.content_type_extra, f.content_type)

            id = str(uuid.uuid4())
            ext = os.path.splitext(f.name)[1]
            filename = f.content_type+ '/'+ id+ ext
            filename = fs.save(self.base_path+ filename, f)
            type = f.content_type
            size= f.size
            url = fs.url(filename)
            path = fs.path(filename)

            uploaded_files.append(Files(
                id= id,
                filename= filename,
                url= url,
                path= path,
                type= type,
                size= size,
            ))
        # print(uploaded_files)
        insert = Files.objects.bulk_create(uploaded_files)
        print('insert', insert)
        return insert



