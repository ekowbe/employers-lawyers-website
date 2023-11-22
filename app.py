import cloudinary
import cloudinary.api
import cloudinary.uploader

from cloudinary.uploader import upload
from time import strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from datetime import datetime
# from api.models.people import people as peeps
# from api.models.articles import reads

from models.people import people as peeps
from models.articles import reads

cloudinary.config(
  cloud_name = "dmusx7j1c",
  api_key = "365654555955232",
  api_secret = "KfVZ9P9IkwP0q_uAKwdfCqGAwoM"
)

# -----------------------------------------------------------------------

app = Flask(__name__, template_folder='templates')

# -----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    footer_image = cloudinary.api.resource_by_asset_id("8c967f04d4f53f6c17522a3c38e6c9de")
    footer_image_url = footer_image['url']

    html = render_template(
        'index.html',
        footer_image_url = footer_image_url,
        index=True)

    response = make_response(html)
    return response

@app.route('/practice_areas', methods=['GET'])
def practice_areas():
    
    header_image = cloudinary.api.resource_by_asset_id("2f6c474f54d380ff8f07e9db072aaf00")
    header_image_url = header_image['url']
 
    footer_image = cloudinary.api.resource_by_asset_id("2dabdf50b202e606c45df748c6f87edc")
    footer_image_url = footer_image['url']

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
    header_image = cloudinary.api.resource_by_asset_id("8f6866ac860082d7910354662b88915b")
    header_image_url = header_image['url']
 
    footer_image = cloudinary.api.resource_by_asset_id("8c967f04d4f53f6c17522a3c38e6c9de")
    footer_image_url = footer_image['url']

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
    header_image = cloudinary.api.resource_by_asset_id("2f6c474f54d380ff8f07e9db072aaf00")
    header_image_url = header_image['url']
 
    footer_image = cloudinary.api.resource_by_asset_id("2dabdf50b202e606c45df748c6f87edc")
    footer_image_url = footer_image['url']

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
    header_image = cloudinary.api.resource_by_asset_id("a9c3c2506cf6ad522f7add03b23883d2")
    header_image_url = header_image['url']
 
    footer_image = cloudinary.api.resource_by_asset_id("75c0885f21d999901379e2ea69eda030")
    footer_image_url = footer_image['url']

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
    header_image = cloudinary.api.resource_by_asset_id("a9c3c2506cf6ad522f7add03b23883d2")
    header_image_url = header_image['url']
 
    footer_image = cloudinary.api.resource_by_asset_id("75c0885f21d999901379e2ea69eda030")
    footer_image_url = footer_image['url']

    html = render_template(
        'article.html',
        header_image_url=header_image_url,
        footer_image_url=footer_image_url,
        article = reads[article_title],
        index=False
    )

    response = make_response(html)
    return response
