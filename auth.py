from flask import Flask, render_template, redirect, url_for, request, session
import db ,string, random
from datetime import timedelta

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_letters, k=256))

@app.route('/', methods=['GET'])
def index():
    msg = request.args.get('msg')   # Redirect された時のパラメータ受け取り

    if msg == None:
        # 通常のアクセスの場合
        return render_template('index.html')
    else :
        # register_exe() から redirect された場合
        return render_template('index.html', msg=msg)

# @app.route('/', methods=['POST'])
# def login():
#     error = 'ログインに失敗しました。'
#     return render_template('index.html', error=error)

@app.route('/register')
def register_form():
    return render_template('login.html')

@app.route('/register_exe', methods=['POST'])
def register_exe():
    user_name = request.form.get('username')
    password = request.form.get('password')

    # バリデーションチェック
    if user_name == '':
        error = 'ユーザ名が未入力です'
        return render_template('register.html', error=error)

    if password == '':
        error = 'パスワードが未入力です'
        return render_template('register.html', error=error)

    count = db.insert_user(user_name, password)

    if count == 1:
        msg = '登録が完了しました。'
        return redirect(url_for('index', msg=msg))  # Redirect で index()に Get アクセス
        # return render_template('index.html', msg=msg)
    else:
        error = '登録に失敗しました。'
        return render_template('login.html', error=error)


    
@app.route('/', methods=['POST'])
def login():
    user_name = request.form.get('username')
    password = request.form.get('password')
    # ログイン判定
    if db.login(user_name, password):
        session['user'] = True
        session.permanent=True# session の有効期限を有効化
        app.permanent_session_lifetime = timedelta(minutes=5) # session の有効期限を 5 分に設定
        return redirect(url_for('mypage'))
    else :
        error = 'ユーザ名またはパスワードが違います。'
        
        input_data = {'user_name':user_name, 'password':password}
        return render_template('index.html', error=error)
    
@app.route('/mypage', methods=['GET'])
def mypage():
    if'user'in session:
        return render_template('mypage.html') # session があれば mypage.html を表示
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/logout')
def logout():
    session.pop('user', None) # session の破棄
    return redirect(url_for('index')) # ログイン画面にリダイレクト

@app.route('/')
def index():
    return render_template('mail.html')

@app.route('/send', methods=['GET'])
def navigateSend():
    return render_template('send.html')