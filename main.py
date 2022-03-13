from flask import Flask,render_template,request

import contacts

app=Flask(__name__)

contactss = contacts.ContactBook()

@app.route(r'/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route(r'/add', methods=['GET','POST'])
def add_contact():
    if  request.form:
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        contactss.add(name=name,phone=phone,email=email)
    return render_template('add_contact.html')

@app.route(r'/list', methods=['GET','POST'])
def generateList():
    lists= contactss.show()
    return render_template('contact_book.html',lists=lists)

@app.route(r'/delete/<name>', methods=['GET'])
def delete(name):
    contactss.delete(name)
    lists = contactss.show()
    return render_template('contact_book.html',lists=lists)

if __name__=='__main__':
    print('Init app in port 2103')
    app.run(debug=True,port=2103)