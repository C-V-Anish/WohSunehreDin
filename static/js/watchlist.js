$(document).ready(function()
{
    $(".btnt").on("click",function()
    {
        $("#app").append('<tr id="rowc"><th scope="row">1</th><td id="pleft1">Mark</td><td id="pleft2">Otto</td></tr>');
    })
});
$(document).ready(function()
{
    $(".btnd").on("click",function()
    { 
        $('#rowc:last-child').remove();
    })
});