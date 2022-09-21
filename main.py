#Flask api for generating prime numbers using normal method and prime sieve
#For input use postman app to check for this api and provide json data as input
#Create a database with num1,num2,prime_number as column with JSON datatype and date with int datatype
#attach this database with flask using SQLAlchemy and follow rest steps

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLAlchemy_DATABASE_URI'] = 'mysql://root: @localhost/primedb'           #URI for SQLalchemy
db = SQLAlchemy(app)

class Primedb(db.Model):                                                            #database model

    '''num1,num2,date,prime_numbers'''
    sno= db.Column(db.Integer, primary_key=True)
    num1= db.Column(db.JSON, unique= False, nullable=False)
    num2=db.Column(db.JSON,unique= False, nullable=False)
    date=db.Column(db.String(20),unique= False,)
    prime_numbers=db.Column(db.JSON,unique= False,)


@app.route("/primegen", methods= ["POST","GET"])            #add "/primegen" after local host
def primegen():                                        #function for generating prime numbers between two numbers
    output =request.get_json()

    if len(output.keys())<2:
        return {"Status":"BAD response"}

    num1 =int(output["num1"])
    num2= int(output["num2"])
    if(request.method=="POST"):
        '''add entry to db'''
        num1=request.form.get('num1')
        num2=request.form.get('num2')
        entry= Primedb(num1=num1,num2=num2,date=datetime.now)               #enter num1,num2,date to databse
        db.session.add(entry)
        db.session.commit()




    cal =[]                             #list that stores all the prime numbers

    for num in range(num1, num2 + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                cal.append(num)

    db.session.add(cal)                                  #enter cal list as json data to the database
    db.session.commit()
    return (cal)




@app.route("/sieve", methods= ["POST","GET"])           #add "/sieve" after localhost ip
def sieve():                                            #function to implement prime sieve
    output =request.get_json()

    if len(output.keys())<2:
        return {"Status":"BAD response"}

    num1 =int(output["num1"])
    num2= int(output["num2"])
    if (request.method == "POST"):
        '''add entry to db'''
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        entry = Primedb(num1=num1, num2=num2,date=datetime.now)              #enter num1,num2,date to databse
        db.session.add(entry)
        db.session.commit()

    cal =[]

    prime = [True for i in range(num2 + 1)]
    p = 2
    while (p * p <= num2):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, num2 + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num2 + 1):
        if prime[p] and p>num1:

            cal.append(p)
    db.session.add(cal)                             #enter cal list as json data to the database
    db.session.commit()

    return (cal)




if __name__== "__main__":
    app.run(debug=True)