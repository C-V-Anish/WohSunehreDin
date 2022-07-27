$(document).ready(function(){
    $('#subbtn').click(function()
    {
        $('input[type="search"]').each(function()
        {
            if ($(this).val() == " ") {
               alert("Empty")
               document.location='/movies';
            }
         })
    })
});
