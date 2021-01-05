import pyrebase

class DataBase:
    def __init__(self,local_path):
        config={
            "apiKey": "AIzaSyDwCT4Ke27JXSjW6Y2sRfsYpNtzI094PJ4",
            "authDomain": "yazlab3-80738.firebaseapp.com",
            "databaseURL": "https://yazlab3-80738-default-rtdb.firebaseio.com",
            "projectId": "yazlab3-80738",
            "storageBucket": "yazlab3-80738.appspot.com",
            "messagingSenderId": "1046884850783",
            "appId": "1:1046884850783:web:1bb0da9ddf26f0b0ad4fea",
            "measurementId": "G-FF0S2RB0JK"
        }

        firebase=pyrebase.initialize_app(config)
        #auth=firebase.auth()
        #auth.create_user_with_email_and_password("berkay@gmail.com","123456")
        
        """db=firebase.database()
        data={"name":local_path}
        db.child("image").push(data)
        #db.child("image").child("OwnKey").push(data)
        db.child("image").child("OwnKey").set(data) # if OwnKey exists, it only creates one
        #db.child("image").child("OwnKey").update({"name":local_path})
        #db.child("image").child("OwnKey").remove()

        images=db.child("image").get()
        print(images.val())"""

        db=firebase.database()
        data={"name":local_path}
        db.child("image").push(data)

        storage=firebase.storage()
        storage.child(f"images/{local_path}").put(local_path)
        #storage.child(f"images/{local_path}").download("downloadedImg.jpg")


if __name__=="__main__":
    db=DataBase(local_path="imagee.jpg")