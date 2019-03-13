import random

from app import app
from flask import session, render_template, flash, redirect, url_for
from app.forms import GuessNumberForm


@app.route('/')
def index():
    # generate a random number in 0~1000, store it into session.
    session['number'] = random.randint(0, 1000)
    session['times'] = 10
    return render_template('index.html')


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    times = session['times']
    result = session['number']
    form = GuessNumberForm()
    if form.validate_on_submit():
        times -= 1
        session['times'] = times  # update session value
        if times < 0:
            flash(u'你输啦', 'danger')
            return redirect(url_for('index'))
        answer = form.number.data
        if answer > result:
            flash(u'太大了，你还剩下%s次机会。' % times, 'warning')
        elif answer < result:
            flash(u'太小了，你还剩下%s次机会。' % times, 'info')
        else:
            flash(u'你赢啦', 'success')
            return redirect(url_for('index'))
        return redirect(url_for('guess'))
    return render_template('guess.html', form=form)
