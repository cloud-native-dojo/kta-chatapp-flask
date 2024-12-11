from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
	"fmervo000001gsle.jpg",
	"rn2ola000000lk6e.jpg",
	"rn2ola000001gogf.jpg",
	"6fujishigai_s_s.jpg",
	"rn2ola000000lk6r.jpg",
	"5fujikawarakuza_s_s.jpg"
	]

url_base = "https://www.city.fuji.shizuoka.jp/page/gazou/fmervo000001dsro-img/"



@app.route('/')
def index():
	url = url_base + random.choice(images) 
	return render_template('index.html', url=url)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
