# coding: utf-8
from flask import Blueprint,render_template,redirect,url_for,flash
from lolipop.models import Notice
from lolipop.form import NoticeForm
from views.account import admin_required
from _helpers import cache

bp = Blueprint('notice',__name__)

@bp.route('/create',methods=('GET','POST'))
@admin_required
def create():
    form = NoticeForm()
    if form.validate_on_submit():
        form.save()
    else:
        flash(('Missing content'),'error')
    return redirect(url_for('admin.dashboard'))

@bp.route('/delete/<int:uid>')
@admin_required
def delete(uid):
    notice = Notice.query.get_or_404(uid)
    notice.delete()
    return redirect(url_for('admin.dashboard'))

@bp.route('/<int:uid>')
@cache.cached(timeout=86400)
def view(uid):
    notice = Notice.query.get_or_404(uid)
    return render_template('notice/view.html',notice=notice)
