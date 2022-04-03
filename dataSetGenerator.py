import cv2
import sqlite3
cap = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def insertOrUpdate(Id,Name,Vd):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1;
    if(isRecordExist==1):
        cmd="UPDATE people SET Name='"+str(name)+"'Vd='"+str(vd)+"'WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO people(ID,Name,Vd) Values("+str(Id)+",'"+str(name)+"','"+str(vd)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()
id=input('enter user id')
name=input('enter your name')
vd=input('enter vaccination detail')
insertOrUpdate(id,name,vd)
sampleNum=0;
while(True):
    ret, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img(x,y),(x+w,y), gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
        cv2.waitKey(100);
        cv2.imshow('Face',img)
        cv2.waitKey(1);
    if(sampleNum>20):
         break;
cap.release()
cv2.destroyAllWindows()