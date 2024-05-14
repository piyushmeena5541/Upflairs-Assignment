from flask import Flask , render_template , url_for , request
import smtplib
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('sign.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/userdata')
def userdata():
    return render_template('user_data.html')

@app.route('/submitdata', methods=['GET', 'POST'])
def submitdata():
    if request.method == "POST":
       Profession = request.form['Profession']
       name = request.form['name']
       email = request.form['email']
       password = request.form['password']
       user_data = {"user_profession":Profession ,
                  "user_name":name , "user_email":email,
                  "user_password":password}
       
       return user_data

@app.route("/emailsend")
def uemailsend():
    return render_template("emailsend.html")
    

@app.route("/emaildata",methods=['GET','POST'])
def emaildata():
    
    if request.method == "POST":
        Email1 =request.form['email']
        Subject1 = request.form['subject']
        message = request.form['message']
        try:
            server = smtplib.SMTP(host='smtp.gmail.com',port=587)
            server.starttls()
            sender_email ="piyushmeena020@gmail.com" 
            sender_password = "khda icsf tvev ctxw"

            reciever_email = Email1
            subject = Subject1
            body = message

            server.login(sender_email,sender_password)
            print("You have been logged in succesfully!!")

            message = f"subject :{subject}\n\n{body}"

            server.sendmail(sender_email,reciever_email,message)
            print("email succesfully send")
            server.quit()
            complete_message="""email fetched\n
            subject fetched\n
            message fetched\n
            You have been logged in succesfully!!\n
            email succesfully send
            """

        except Exception as e:
            print(e)

    return complete_message



if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=2525 ,debug=True)