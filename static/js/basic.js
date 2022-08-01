$(document).ready(function()
{
    $('#subbtn').click(function()
    {
       var str=$('#inputmov').val();
       if(str.trim().length === 0)
       {
            alert("Please fill the field.")
       }
    })
});
