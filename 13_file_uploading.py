from flask import Flask, flash, redirect, render_template, request, url_for, send_from_directory, session
from werkzeug.utils import secure_filename
import os
import time

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = 'C:/Users/user/Desktop/develop/prect_11/data'

# 라우터
@app.route('/')
def upload_file():
    return render_template('13_upload.html')

# 파일 업로드
@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    # 파일 보내기 코드
    # if request.method == 'POST':
    #     file = request.files['file']
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    #     return 'file uploaded successfully'

    # 폴더 업로드 코드
    if request.method == 'POST':
        files = request.files.getlist('file[]')
        print(files)
        pass_image = ['JPG', 'PNG']
        for fil in files:
            print(fil)
            time.sleep(0.01)
            fil.save(os.path.join(app.config['UPLOAD_FOLDER'], fil.filename))
        return 'file uploaded successfully'

#파일 업로드 처리
# @app.route('/fileUpload', methods = ['GET', 'POST'])
# def realy_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       #저장할 경로 + 파일명
#       f.save(secure_filename(f.filename))
#       return 'uploads 디렉토리 -> 파일 업로드 성공!'

if __name__ == '__main__':
    app.run()