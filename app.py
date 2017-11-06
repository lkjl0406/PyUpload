import os
from flask import Flask, render_template, request

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# abspath로 입력받은 경로를 절대경로로 바꿔줌
# abspath로 바꿔준 절대경로를 dirname으로 경로 반환해줌

@app.route('/')
def index():
    return render_template("upload.html")
# templates 폴더에 있는 upload.html 가져옴

@app.route('/upload', methods=['POST'])
# 경로를 /upload로 설정후 post방식으로 설정
def upload():
    target = os.path.join(APP_ROOT, 'uploadfile/')
    # target=C:\Users\lkjl0\Documents\pyupload\uploadfile
    print(target)
    if not os.path.isdir(target):
    # 해당 경로가 디렉토리인지 아닌지 검사
    # 디렉토리인 경우는 true 아니면 false 반환 
        os.mkdir(target)
    for file in request.files.getlist("file"):
    	# for문 사용한 이유는 여러개의 파일을 동시에 업로드 하기 위해
    	# file 은 upload.html 의 input태그의 name="file"
        print('===filename check===')
        print(file)
        filename = file.filename
        destination = ''.join([target, filename])
        # destination = C:\Users\lkjl0\Documents\pyupload\uploadfile\filename
        print('===destination check===')
        print(destination)
        file.save(destination)

    return render_template("complete.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
