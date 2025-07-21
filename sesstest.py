from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return  redirect('/cookie-test')

@app.route('/cookie-test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count:
        res = make_response(f'Вы посетили эту страницу {visit_count} раз(а).')
        res.set_cookie('visit_count', str(visit_count + 1), max_age=60*60*24*30)
    else:
        res = make_response(f'Вы впервые посетили эту страницу за последние 30 дней.')
        res.set_cookie('visit_count', '1', max_age=60*60*24*30)
    return res



if __name__ == '__main__':
    app.run(host='localhost', port=8000)