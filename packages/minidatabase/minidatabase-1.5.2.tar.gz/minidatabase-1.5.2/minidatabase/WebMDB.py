from flask import Flask
import minidb
#MiniDataBase Web Server Service
#Develop By HansenL
if __name__ == "__main__":
    print("Welcome to use WebMDB Server.")
    p=int(input("Please enter the service port->"))
    nzm=input("Please enter the MiniDataBase File name->")
    passwd=input("Please enter the Database Password ->")
    cursor=minidb.connect(nzm)
    app=Flask(__name__)
    @app.route('/')
    def status():
        return 'WebMDB Services has been opened.'
    @app.route('/%s/append/<tag>/<value>'%passwd)
    def append(tag,value):
        cursor.append(tag,value)
        return 'successful'
    @app.route('/%s/delete/<tag>'%passwd)
    def deleted(tag):
        cursor.delete(tag)
        return 'successful'
    @app.route('/%s/len'%passwd)
    def lentht():
        return str(cursor.len())
    @app.route('/%s/items'%passwd)
    def list_db():
        l=cursor.items()
        return str(l)
    @app.route('/%s/clean'%passwd)
    def clearn():
        cursor.clean()
        return 'successful'
    @app.route('/%s/get/<tag>'%passwd)
    def get_data(tag):
        return str(cursor.get(tag))
    @app.route('/%s/commit'%passwd)
    def commita():
        cursor.commit()
        return 'successful'
    @app.route('/%s/search/<keyword>'%passwd)
    def search_all(keyword):
        return str(cursor.search(keyword))
    @app.route('/%s/search_tag/<keyword>'%passwd)
    def search_tags(keyword):
        return str(cursor.search_tag(keyword))
    @app.route('/%s/search_value/<keyword>'%passwd)
    def search_values(keyword):
        return str(cursor.search_value(keyword))
    app.run(port=p)

