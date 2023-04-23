
$("#bp_rule").click(function(){
    $.ajax({
        type:"GET",
        url:"/bp/test_rule",
        success: function(result){
            console.log(result)
        }
    })
})
$("#bp_get").click(function(){
    $.ajax({
        type:"GET",
        url:"/bp/get",
        success: function(result){
            console.log(result)
        }
    })
})

const test_data = {
    id: 229,
    name: "Sammy",
    email: "Sammy@test.com"
};

$("#json").click(function(){
    $.ajax({
        url:"/basic/json",
        method:"POST",
        contentType:"application/json",
        dataType:"json",
        data: JSON.stringify(test_data),
        success:function(result){
            console.log("return json")
            console.log(result)
        },
        error:function(result){
            console.log("error")
        }
    })
})

$("#request_data").click(function(){
    $.ajax({
        url:"/basic/request_data",
        method:"GET"
    })
})

$("#get_value").click(function(){
    const value=document.getElementById("value").value
    console.log(value)
    var url = "/basic/get_value/"+value
    console.log(url)
    $.ajax({
        url:url,
        method:"GET"
    })
})

$("#cookie_value").click(function(){
    console.log("now cookie")
    console.log(document.cookie)
    $.ajax({
        url:"/cookie/value"
    })
    console.log("after cookie")
    console.log(document.cookie)
})

$("#cookie_dict").click(function(){
    console.log("now cookie")
    console.log(document.cookie)
    $.ajax({
        url:"/cookie/dict"
    })
    console.log("after cookie")
    console.log(document.cookie)
})

$("#jsonify_code0").click(function(){
    $.ajax({
        url:"/basic/jsonify_code/0",
        method:"GET",
        success:function(result, status, xhr){
            console.log(result)
            console.log(status)
            console.log(xhr.status)
        }
    })
})
$("#jsonify_code1").click(function(){
    $.ajax({
        url:"/basic/jsonify_code/1",
        method:"GET",
        success:function(result, status, xhr){
            console.log(result)
            console.log(status)
            console.log(xhr.status)
        }
    })
})

$("#post_zero").click(function(){
    $.ajax({
        url:"/basic/post_zero",
        method:"GET",
        //contentType:"application/json",
        //dataType:"json",
        //data: JSON.stringify({}),
        success:function(result){
            console.log("success")
        }
    })
})

$("#raise_exception").click(function(){
    $.ajax({
        url:"/basic/raise_exception",
        method:"GET",
        success:function(result){
            console.log(result)
        }
    })
})

$("#return_code").click(function(){
    const code = document.getElementById("code").value

    var url = "/basic/return_code/"+code
    $.ajax({
        url:url,
        method:"GET",
        success:function(data,status){
            console.log("in success")
            console.log(data.msg)
        },
        error: function(jqXHE, status){
            console.log("in error")
            console.log(status)
            console.log(jqXHE)
        }
    })
})

$("#paths").click(function(){
    $.ajax({
        url:"/basic/paths?x=123&y=test_arg",
        method:"GET",
        success:function(result){
            console.log("success")
        }
    })
})