from flask import Flask, url_for, request
import os.path

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    avatar_name=url_for('static', filename=f'img/avatar.jpg')
    if request.method == 'GET':
        if not os.path.exists('static/img/avatar.jpg'):
            avatar_name=url_for('static', filename=f'img/dummy.jpg')
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/avatar.jpg', 'wb') as fo:
            fo.write(f.read())
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Загрузка фотографии</title>
                        </head>
                        <body>
                        <h1>Загрузка фотографии</h1>
                        <h2>для участия в миссии</h2>
                        <form method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <p>Приложите фотографию</p>
                                <label for="photo">Выберите файл</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                                <img src="{avatar_name}" width='420'> 
                            <button type="submit" class="btn btn-primary">Отправить</button>
                                                            </div>
                        </form>
                        </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')