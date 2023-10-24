from flask import Flask,render_template,request,jsonify
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/select',methods=['POST'])
def select():
    global csv_path
    folder_name = request.json["folder_name"]
    csv_path = f"./static/data/{folder_name}/correct_position_data.csv"
    #画像の総数取得
    max_num = len(os.listdir(f"./static/img/{folder_name}"))

    # correct_position.csv無ければ作成
    if not os.path.exists(csv_path):
        column_names = [
        "frame", "NOSE_x", "NOSE_y", "NOSE_z", "LEFT_EYE_INNER_x", "LEFT_EYE_INNER_y", "LEFT_EYE_INNER_z","LEFT_EYE_x", "LEFT_EYE_y", "LEFT_EYE_z", "LEFT_EYE_OUTER_x", "LEFT_EYE_OUTER_y", "LEFT_EYE_OUTER_z",
        "RIGHT_EYE_INNER_x", "RIGHT_EYE_INNER_y", "RIGHT_EYE_INNER_z", "RIGHT_EYE_x", "RIGHT_EYE_y", "RIGHT_EYE_z","RIGHT_EYE_OUTER_x", "RIGHT_EYE_OUTER_y", "RIGHT_EYE_OUTER_z", "LEFT_EAR_x", "LEFT_EAR_y", "LEFT_EAR_z",
        "RIGHT_EAR_x", "RIGHT_EAR_y", "RIGHT_EAR_z", "MOUTH_LEFT_x", "MOUTH_LEFT_y", "MOUTH_LEFT_z", "MOUTH_RIGHT_x","MOUTH_RIGHT_y", "MOUTH_RIGHT_z", "LEFT_SHOULDER_x", "LEFT_SHOULDER_y", "LEFT_SHOULDER_z","RIGHT_SHOULDER_x",
        "RIGHT_SHOULDER_y", "RIGHT_SHOULDER_z", "LEFT_ELBOW_x", "LEFT_ELBOW_y", "LEFT_ELBOW_z","RIGHT_ELBOW_x", "RIGHT_ELBOW_y", "RIGHT_ELBOW_z", "LEFT_WRIST_x", "LEFT_WRIST_y", "LEFT_WRIST_z",
        "RIGHT_WRIST_x", "RIGHT_WRIST_y", "RIGHT_WRIST_z", "LEFT_PINKY_x", "LEFT_PINKY_y", "LEFT_PINKY_z","RIGHT_PINKY_x", "RIGHT_PINKY_y", "RIGHT_PINKY_z", "LEFT_INDEX_x", "LEFT_INDEX_y", "LEFT_INDEX_z",
        "RIGHT_INDEX_x", "RIGHT_INDEX_y", "RIGHT_INDEX_z", "LEFT_THUMB_x", "LEFT_THUMB_y", "LEFT_THUMB_z","RIGHT_THUMB_x", "RIGHT_THUMB_y", "RIGHT_THUMB_z", "LEFT_HIP_x", "LEFT_HIP_y", "LEFT_HIP_z",
        "RIGHT_HIP_x", "RIGHT_HIP_y", "RIGHT_HIP_z", "LEFT_KNEE_x", "LEFT_KNEE_y", "LEFT_KNEE_z","RIGHT_KNEE_x", "RIGHT_KNEE_y", "RIGHT_KNEE_z", "LEFT_ANKLE_x", "LEFT_ANKLE_y", "LEFT_ANKLE_z",
        "RIGHT_ANKLE_x", "RIGHT_ANKLE_y", "RIGHT_ANKLE_z", "LEFT_HEEL_x", "LEFT_HEEL_y", "LEFT_HEEL_z","RIGHT_HEEL_x", "RIGHT_HEEL_y", "RIGHT_HEEL_z", "LEFT_FOOT_INDEX_x", "LEFT_FOOT_INDEX_y", "LEFT_FOOT_INDEX_z",
        "RIGHT_FOOT_INDEX_x", "RIGHT_FOOT_INDEX_y", "RIGHT_FOOT_INDEX_z"
        ]

        df = pd.DataFrame(columns=column_names)
        df["frame"] = range(1, max_num + 1)
        # フォルダ,csvを作成
        os.makedirs(f"./static/data/{folder_name}", exist_ok=True)
        df.to_csv(csv_path, index=False)

    return jsonify({"max_num":max_num})

#画像内をクリックしたときの処理
@app.route('/img_click',methods=['POST'])
def img_click():
    try:
        column_name = request.json["column_name"]
        x = request.json["x"]
        y = request.json["y"]
        frame = request.json["frame"]

        df = pd.read_csv(csv_path,index_col="frame")
        df[f"{column_name}_x"][frame] = x
        df[f"{column_name}_y"][frame] = y

        df.to_csv(csv_path)
        return jsonify({"error":"False"})
    
    except Exception as e:
        # エラーが発生した場合、エラーメッセージとステータスコードを返す
        return jsonify({"error":"True"})

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=5000)

