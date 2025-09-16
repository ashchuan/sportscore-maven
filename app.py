from flask import Flask, render_template
import feedparser
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the RSS feed
    rss_url = "https://static.cricinfo.com/rss/livescores.xml"
    try:
        response = requests.get(rss_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        feed = feedparser.parse(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        feed = None

    matches = []
    if feed and feed.entries:
        for entry in feed.entries:
            matches.append({
                'title': entry.title,
                'link': entry.link,
                'description': entry.description
            })

    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
