from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def home():
    # URL of the RSS feed
    rss_feed_url = "https://static.cricinfo.com/rss/livescores.xml"
    
    # Parse the RSS feed
    feed = feedparser.parse(rss_feed_url)
    
    # Extract entries (match scores)
    matches = []
    for entry in feed.entries:
        matches.append({
            'title': entry.title,
            'link': entry.link,
            'description': entry.description
        })
    
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)