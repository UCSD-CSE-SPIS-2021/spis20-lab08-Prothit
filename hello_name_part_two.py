from flask import Flask

app = Flask(__name__)



@app.route("/")

def hello():

   return "Hello from Prothit's server!"

def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)


@app.route('/ftoc/<ftemp_str>')

def convert_ftoc(ftemp_str):

    ftemp = 0.0

    try:

        ftemp = float(ftemp_str)

        ctemp = ftoc(ftemp)

        return "In Farenheit: " + ftemp_str + " In Celsius " + str(ctemp) 

    except ValueError:

        return "Sorry.  Could not convert " + ftemp_str + " to a number"

def miles_to_km(miles):
    return miles * 1.60934


@app.route('/mtokm/<miles_str>')

def convert_mtokm(miles_str):
  try:
    fmiles = float(miles_str)
    fkm = miles_to_km(fmiles)
    return "In miles: " + miles_str + " In KM: "+ str(fkm)   
  
  except ValueError:
    return "could not convert"+ miles_str+ "."



if __name__ == "__main__":

   app.run(host='0.0.0.0')