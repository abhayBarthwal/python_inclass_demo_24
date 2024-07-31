from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__) 

# configuration to be able to connect to the database
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "batch_4"

#my flask app
mysql = MySQL(app)

#my home endpoint
@app.route('/') 
def hello_world(): 
    return render_template("home.html", home_message = "Welcome to our home page, This data is from the server!", home_para = "A para for the home page!")


@app.route('/contact/') 
def contact(): 
    my_list = ["Apples", "Mango", "Cherry", "Grapes", "Banana"]
    my_dictionary = {'phy':50,'che':60,'maths':70, 'coding':90}
    return render_template("contact.html", user_age = 15, the_list = my_list, the_dictionary = my_dictionary)

#my login page
@app.route('/login/', methods=['POST', 'GET']) 
def login():
    # a method that takes post request and processes the data
    if request.method == "POST": 
        cur = mysql.connection.cursor()
        user_name = request.form["us_name"]
        user_age = request.form["us_age"]
        user_city = request.form["us_city"]
        user_hobby = request.form["us_hobby"]
        user_file = request.files["us_file"]
        user_file.save("static/uploads/" + user_file.filename)
        print(user_file)
        print("user info = ", user_name, user_age, user_city, user_hobby)
        my_insert_query = "INSERT INTO user_info VALUES ('{0}', {1}, '{2}', '{3}');".format(user_name, user_age, user_city, user_hobby)
        cur.execute(my_insert_query)
        mysql.connection.commit()
        return 'Login Successful'
    else:
        return render_template('my_form.html')
    
@app.route('/my_data/') 
def data_world(): 
    select_query = "SELECT * FROM user_info;"
    cur = mysql.connection.cursor()
    cur.execute(select_query)
    all_data = cur.fetchall()
    return render_template("data.html", the_data = list(all_data))

@app.route('/my_data_filtered/<city>') 
def data_world_filtered(city): 
    select_query = "SELECT * FROM user_info WHERE user_city = '{0}';".format(city)
    cur = mysql.connection.cursor()
    cur.execute(select_query)
    all_data = cur.fetchall()
    return render_template("data.html", the_data = list(all_data))



if __name__ == '__main__': 
	app.run(port=4005, debug=True)
