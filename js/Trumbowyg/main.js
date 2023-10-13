//$(function(){
//    $('#editor').trumbowyg({
//        lang:'ja', //言語設定
//        autogrow: true //入力に合わせてテキストエディタ入力欄を広げる
//    });
//});

$(document).ready(function () {
    $("#add_element").on("click",function(){
        let elements_box = document.getElementById('elements');

        let new_element = document.createElement("p")
        new_element.textContent = "added element"
        new_element.classList.add("added_element")
        elements_box.appendChild(new_element)
        $(new_element).on("click",function(){
            console.log("clicked")
        })
    })
    $(".added_element").on("click",function(){
        console.log("clicked")
    })
});
