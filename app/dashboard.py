from flask import Flask, render_template
from app.database import session, Tweet
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Função para gerar gráficos
def create_plot():
    tweets = session.query(Tweet).all()
    tweet_times = [tweet.created_at for tweet in tweets]
    plt.hist(tweet_times, bins=24)
    plt.xlabel('Hour')
    plt.ylabel('Tweet Count')
    plt.title('Tweets over Time')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/')
def index():
    plot_url = create_plot()
    return render_template('dashboard.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
