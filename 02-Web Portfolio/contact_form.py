from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form (e.g., send an email or save the message)
        return "Thank you for your message!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
