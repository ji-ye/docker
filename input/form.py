from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def form():
    return '''
    <h1>Rate a country's Personal Freedom Score</h1>
    <a href="https://www.cato.org/human-freedom-index">using data from Cato's Human Freedom Index Description</a>
    <p>The dataset covers 133 countries for 2015, the most recent year with sufficient data available.</p>
    <p>
       (All feature fields can accept input within a 10-point scale, i.e. integer from 0 to 10) <br>
  	</p>

    <form action="http://localhost:5000" method="POST">
                  Rule of Law: <input type="number" name="feature1" step="1" min="0" max="10"> <br><br>
                  Security & Safety: <input type="number" name="feature2" step="1" min="0" max="10"> <br><br>
                  Movement: <input type="number" name="feature3" step="1" min="0" max="10"> <br><br>
                  Religion: <input type="number" name="feature4" step="1" min="0" max="10"> <br><br>
                  Association Assembly & Civil Society: <input type="number" name="feature5" step="1" min="0" max="10"> <br><br>
                  Expression & Information: <input type="number" name="feature6" step="1" min="0" max="10"> <br><br>
                  Identity & Relationships: <input type="number" name="feature7" step="1" min="0" max="10"> <br><br>
                  <input type="submit" value="Submit"><br>
     </form>
     '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3838)
