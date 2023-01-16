$("#post_zero").click(function(){
    $.ajax({
        url:"/post_zero",
        method:"GET",
        //contentType:"application/json",
        //dataType:"json",
        //data: JSON.stringify({}),
        success:function(result){
            console.log("success")
        }
    })
})