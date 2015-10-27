# -*- coding: utf-8 -*-
def happy_birthday():
    import time
    t = time.ctime()
    open('/tmp/happy_birthday_file','w').write('today is your birhday  \n' %str)
    return t
def generate_status():
    import random, time
    t = time.ctime()
    sentence = ['I am happy at ', 'I am sad at ', 'I am excited at ', 'I am depressed at ']
    open('/tmp/myStatus','a').write(random.choice(sentence) + t + '\n')
    db.new_temp_table.insert(name=random.choice(sentence))
    db.commit()
    return t

def resizeimg():
    import time
    from PIL import Image
    import urllib, cStringIO
    import os
    t = time.ctime()
    imageUploaded = db(db.imagestore.checkfield.like('false')).select().first()
    if imageUploaded:
        name_image_dupli=imageUploaded.name.split(',')[0]
        name_image_992558=name_image_dupli+"992*558.jpeg"
        name_image_330185625=name_image_dupli+"330*186.jpeg"
        name_image_16090=name_image_dupli+"160*90.jpeg"
        open('/tmp/myPictureget2','a').write(name_image_992558 + t + '\n')
        imageURL = URL('default', 'download', args=[imageUploaded.picture],host=True)
        file1 = cStringIO.StringIO(urllib.urlopen(imageURL).read())
        #file2 = cStringIO.StringIO(urllib.urlopen(imageURL).read())
        #file3 = cStringIO.StringIO(urllib.urlopen(imageURL).read())
        newImage1 = Image.open(file1)
        (width1, height1)=newImage1.size
        if width1>=992 and height1>=558:
            #newImage2 = Image.open(file2)
            #newImage3 = Image.open(file3)
            size1=(992,558)
            #size2=(330,185)
            #size3=(160,90)
            newImage1.thumbnail(size1,Image.ANTIALIAS)
            #newImage2.thumbnail(size2,Image.ANTIALIAS)
            #newImage3.thumbnail(size3,Image.ANTIALIAS)
            newImage1.save(name_image_992558,'jpeg')
            #newImage2.save(name_image_330185625,'jpeg')
            #newImage3.save(name_image_16090,'jpeg')
            imageDupliFileOpen1=open(name_image_992558, 'rb')
            #imageDupliFileOpen2=open(name_image_330185625, 'rb')
            #imageDupliFileOpen3=open(name_image_16090, 'rb')
            #db.imagestore.insert(name = imageUploaded.name, picture = imageDupliFileOpen)
            #db(db.imagestore.id == imageUploaded.id).update(picture992558=imageDupliFileOpen1, picture330185625=imageDupliFileOpen2,         picture16090=imageDupliFileOpen3)
            updateStatus=db(db.imagestore.id == imageUploaded.id).update(picture992558=imageDupliFileOpen1)
            imageDupliFileOpen1.close()
            #imageDupliFileOpen2.close()
            #imageDupliFileOpen3.close()
            os.remove(name_image_992558)
            #os.remove(name_image_330185625)
            #os.remove(name_image_16090)
            if updateStatus:
                db(db.imagestore.id == imageUploaded.id).update(checkfield='True')
            else:
                db(db.imagestore.id == imageUploaded.id).update(checkfield='Failed')
            db.commit()
            return imageUploaded.id
        else:
            db(db.imagestore.id == imageUploaded.id).update(checkfield='Failed')
            db.commit()
            return 'error uploading image of size less than 1600*900'
        
    else:
        open('/tmp/myPictureget2','a').write('Successfully updated' + t + '\n')
        stop_task(39)
from gluon.scheduler import Scheduler
scheduler = Scheduler(db,dict(our_function=happy_birthday, status = generate_status, getimg = resizeimg))
