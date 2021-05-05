$(document).ready(function () {
    $('#cid').append($('<option>').text("-Select Categories-"))

    $.getJSON('http://127.0.0.1:8000/menucategorydatajson/',{ajax:true},function (data) {
       // alert(data)

       $.each(data,function (index,item) {
           // alert(item)
           $('#cid').append($('<option>').text(item[1]).val(item[0]))

       })

   })

})