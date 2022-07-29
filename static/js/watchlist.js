$(document).ready(function()
{
    $(".btnt").click(function()
    {
        $("#app").append('<tr id="rowc"><th scope="row">1</th><td id="pleft1">Mark</td><td id="pleft2">Otto</td></tr>');
    })
});
$(document).ready(function()
{
    $(".btnd").click(function()
    { 
        $('#rowc:last-child').remove();
    })
});