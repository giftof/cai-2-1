import base64
from datetime import datetime
from flask import Flask, request, Response, jsonify, render_template
import os
from io import BytesIO
from gtts import gTTS
from enum import Enum

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

class LANGS(str, Enum):
    KO = 'ko'
    EN = 'en'
    JA = 'ja'
    ES = 'es'

LOG_FILE = 'input_log.txt'

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html")
    
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        lang = request.form.get('lang', 'ko')
        
        if lang not in [l.value for l in LANGS]:
            return render_template("index.html", error=f"언어 설정 오류 received: [{lang}]", selected_lang='ko')
        
        if not input_text:
            return render_template("index.html", error="입력된 문장이 없습니다.", selected_lang=lang)
        else:
            try:
                with open(LOG_FILE, 'a', encoding='utf-8') as f:
                    log_entry = f"{datetime.now().isoformat()} | lang={lang} | input_text={input_text}\n"
                    f.write(log_entry)
            except ValueError as e:
                return render_template("index.html", error=e, selected_lang=lang)
        
        print(f"[PID {os.getpid()}] received ({lang}):_{input_text}")

        try:
            fp = BytesIO()
            gTTS(input_text, "com", lang).write_to_fp(fp)
            audio_data = base64.b64encode(fp.getvalue()).decode("utf-8")
        except ValueError as e:
            return render_template("index.html", error=e, selected_lang=lang)

        return render_template("index.html", audio=audio_data, selected_lang=lang)

    return render_template("index.html", selected_lang='ko')


if __name__ == '__main__':
    app.run('0.0.0.0', 8090)