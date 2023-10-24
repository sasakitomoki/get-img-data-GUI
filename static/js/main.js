let folder_name = "" //フォルダ名
let column_name = "" //作成するcsvファイルの列名
let img_num = 1 //選択中の画像番号
let max_num = 1 //画像の総数
// ここに最初に実行する処理を書きます
document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event occurred! This code runs first.");
});


//決定ボタン押したとき
document.getElementById("confirm-btn").addEventListener("click", function(){
    folder_name = document.getElementById("folder_name").value
    column_name = document.getElementById("column_name").value
    document.getElementById("imageNumber").value=img_num
    document.querySelector(".slide-show img").src="./static/img/" + folder_name + "/" + folder_name +"_"+ img_num+ ".jpg"
    //画像枚数取得, csvファイル作成
    fetch('/select', {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({"folder_name": folder_name})
      }).then(
        response => response.json()
      ).then(
        json => {
            max_num = json.max_num;
            Swal.fire({
                icon: 'success',
                title: '送信完了',
                timer: 1500, // 1.5 seconds
                timerProgressBar: true,
                showConfirmButton: false
            });
         }
      ).catch(
        e => console.error(e)
      );
});

function changeImage(){
  img_num=Number(document.getElementById("imageNumber").value)
  document.querySelector(".slide-show img").src="./static/img/" + folder_name + "/" + folder_name +"_"+ img_num+ ".jpg"
}

// 前ボタン
document.getElementById("next_btn").addEventListener("click", function(){
    img_num = img_num + 1
    if (!(img_num >= 1 && img_num <= max_num)) {
        img_num = img_num - 1
    }
    document.getElementById("imageNumber").value=img_num
    document.querySelector(".slide-show img").src="./static/img/" + folder_name + "/" + folder_name +"_"+ img_num+ ".jpg"
});
//後ボタン
document.getElementById("back_btn").addEventListener("click", function(){
    img_num = img_num - 1
    if (!(img_num >= 1 && img_num <= max_num)) {
        img_num = img_num + 1
    }
    document.getElementById("imageNumber").value=img_num
    document.querySelector(".slide-show img").src="./static/img/" + folder_name + "/" + folder_name +"_"+ img_num+ ".jpg"
});

//画像内をクリックしたときの処理
document.querySelector(".slide-show img").onclick = function(event) {
    //クリック座標取得
    img = event.target

    //correct_position.csvに座標を書き込み
    fetch('/img_click', {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({"column_name": column_name,"frame": img_num,"x":event.offsetX/img.width,"y":event.offsetY/img.height})
      }).then(
        response => response.json()
      ).then(data => {
        if (data.error === 'True'){
          Swal.fire({
            icon: 'error',
            title: '書き込みエラー',
            timer: 1500, // 1.5 seconds
            timerProgressBar: true,
            showConfirmButton: false
        });
      }else{
        document.getElementById("next_btn").click();
      }
    })
};

//キーボードの処理
document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowRight") {
        document.getElementById("next_btn").click();
    }else if(event.key === "ArrowLeft") {
        document.getElementById("back_btn").click();
    }else if(event.key === "ArrowUp"){
        document.getElementById("imageNumber").value = img_num + 1;
    }else if(event.key === "ArrowDown"){
      document.getElementById("imageNumber").value = img_num - 1;
    }else if(event.key === "Enter"){
      document.getElementById("confirm-btn").click();
    }
  });