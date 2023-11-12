from time import strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from datetime import datetime
from models.people import people as peeps
from models.articles import reads


# -----------------------------------------------------------------------

app = Flask(__name__, template_folder='templates')

# -----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    footer_image_url = '/static/img/footer/water.jpg'
    html = render_template(
        'index.html',
        footer_image_url = footer_image_url,
        index=True)
    response = make_response(html)
    return response

@app.route('/practice_areas', methods=['GET'])
def practice_areas():
    header_image_url = '/static/img/header/pillar.jpg'
    footer_image_url = '/static/img/footer/pillar.jpg'
    practice_areas = [
        {'title': 'Workplace Investigations', 'url': '/work/workplace_investigations', 'blurb': 'The Firm offers not for profit as well as private and public sector employers assistance in performing independent workplace investigations...'},
        {'title': 'Workplace Issues', 'url': '/work/workplace_issues', 'blurb': 'In an effort to assist our clients in avoiding disputes in the workplace, Ryan & Ryan, LLC offers counseling on the day-to-day issues that inevitably arise...'},
        {'title': 'Litigation', 'url': '/work/litigation', 'blurb': 'If litigation occurs, Ryan & Ryan first seeks to understand a particular client’s goals, and then creates a litigation strategy to fit those goals...'},
        {'title': 'Labor Law', 'url': '/work/labor_law', 'blurb': 'Our attorneys have extensive experience representing employers who have unionized workplaces...'},
        {'title': 'Employment Law', 'url': '/work/employment_law', 'blurb': 'We recognize that it is often difficult for employers to be assured that they are in compliance with the frequently changing, and sometimes conflicting laws and regulations that govern the workplace...'}
    ]

    html = render_template(
        'practice_areas.html',
        header_image_url=header_image_url,
        footer_image_url=footer_image_url,
        practice_areas=practice_areas
    )

    response = make_response(html)
    return response


@app.route('/people/<person>', methods=['GET'])
def people(person):
    person = peeps[person]
    header_image_url = '/static/img/header/lighthouse.jpg'
    footer_image_url = '/static/img/footer/water.jpg'

    # print(person)

    html = render_template(
        'people.html',
        person=person,
        header_image_url=header_image_url,
        footer_image_url=footer_image_url,
        index=False
    )

    response = make_response(html)
    return response

@app.route('/work/<topic>', methods=['GET'])
def work(topic):
    header_image_url = '/static/img/header/pillar.jpg'
    footer_image_url = '/static/img/footer/pillar.jpg'

    html = render_template(
        f'{topic}.html',
        header_image_url=header_image_url,
        footer_image_url=footer_image_url,
        index=False
    )
    response = make_response(html)
    return response

@app.route('/articles', methods=['GET'])
def articles():
    header_image_url = '/static/img/header/bridge.jpg'
    footer_image_url = '/static/img/footer/bay.jpg'

    html = render_template(
        'articles.html',
        articles = reads,
        header_image_url=header_image_url,
        footer_image_url=footer_image_url,
        index=False
    )

    response = make_response(html)
    return response

@app.route('/articles/<article_title>', methods=['GET'])
def show_article(article_title):

    header_image_url = '/static/img/header/bridge.jpg'
    footer_image_url = '/static/img/footer/bay.jpg'

    html = render_template(
        'article.html',
        header_image_url=header_image_url,
        footer_image_url=footer_image_url,
        article = reads[article_title],
        index=False
    )

    response = make_response(html)
    return response
