$('#form').submit(function(e){
    var data=$(this).serializeArray();
    console.log(data)
    $.ajax({
        url:"/SaveContactForm/",
        type:'POST',
        data:data,
        success: function(){  
            swal("Successfully Submitted!", "Message successfully updated", "success")
            $('#form').trigger("reset")
        },
        error: function() { 
            swal("Error!", "Form validation error", "error") 
        }       
    })
    return false
      
})
