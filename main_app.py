#Flask api for generating prime numbers using normal method and prime sieve
#For input use postman app to check for this api and provide json data as input

from flask import Flask, request
app = Flask(__name__)

@app.route("/primegen", methods= ["POST","GET"])            #add "/primegen" after local host
def primegen():                                        #function for generating prime numbers between two numbers
    output =request.get_json()

    if len(output.keys())<2:
        return {"Status":"BAD response"}

    num1 =int(output["num1"])
    num2= int(output["num2"])

    cal =[]                     #list that stores all the prime numbers

    for num in range(num1, num2 + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                cal.append(num)


    return (cal)


@app.route("/sieve", methods= ["POST","GET"])           #add "/sieve" after localhost ip
def sieve():                                            #function to implement prime sieve
    output =request.get_json()

    if len(output.keys())<2:
        return {"Status":"BAD response"}

    num1 =int(output["num1"])
    num2= int(output["num2"])

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


    return (cal)




if __name__== "__main__":
    app.run(debug=True)
