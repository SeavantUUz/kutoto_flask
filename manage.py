import os
from flask.ext.script import Manager,Server
from config import db
from app import create_app
from kutoto.form import NewTopic
from kutoto.models import Post,Topic
from flask import redirect,render_template

app = create_app()
manager = Manager(app)
manager.add_command("runserver",Server("localhost",port=8000))


@app.route("/")
def index():
    topics = Topic.query.all()
    return render_template('index.html',topics=topics)

@app.route("/new_topic",methods=('GET','POST'))
def new_topic():
    form  = NewTopic()
    if form.validate_on_submit():
        form.save()
        return redirect('/success')
    return render_template('form.html',form=form)

@app.route('/success')
def success():
    return 'Success'

@manager.command
def init():
    dfile = 'database.db'
    if os.path.exists(dfile):
        os.remove(dfile)
    db.create_all()

if __name__ == "__main__":
    manager.run()
