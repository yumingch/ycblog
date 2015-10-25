# coding: utf-8
import leancloud
leancloud.init('joNnRs9ookVv9CxLjMzh56Fe', master_key='sx3hWqJkBzNrScjFtmJnNPWl')

from flask import Flask, render_template, Blueprint
from leancloud import Object, Query, LeanCloudError

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', zhengwen=blogpost.content)

#if __name__ == '__main__':
#    app.debug = True
#    app.run()

class BlogPost(Object):
	@property
	def content(self):
		return self.get('main_body')
	@property
	def title(self):
	    return self.get('title')

	
	
query = Query(BlogPost)
blogpost = query.get('562c41f960b2804578347f97')
