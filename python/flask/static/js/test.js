
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
        url:"/json",
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
        url:"/request_data",
        method:"GET"
    })
})

$("#get_value").click(function(){
    const value=document.getElementById("value").value
    var url = "/get_value/"+value
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