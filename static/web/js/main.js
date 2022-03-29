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



$('#whatsapp-form').submit(function () {

    var phone = '917306481304';
    var username = $('#name').val()
    var product = $('#product').val()
    var address = $('#address').val()
    var content = $('#content').val()
    const text = [
        'Name:' + username,
        'Product: ' + product,
        'Address: ' + address,
        'Content: ' + content,

    ].join("\n") // change to what you want sep to be
    const action = "https://wa.me/" + phone + "?text=" + encodeURIComponent(text);
    window.location.href = action;

    return false
})