var TodayDate = new Date();
var d = TodayDate.getDate();
var temp_prev_day = d; 
var temp_next_day = d; 
var m = TodayDate.getMonth()+1;
var y = TodayDate.getFullYear();

$(document).ready(function () { // wait until the document is ready
//Click on previous day
$('#previous_day').click(function(){
temp_prev_day--;
$.post({
    url: 'http://api.reimaginebanking.com/enterprise/customers/58a7effd1756fc834d904a75?key=4068fb9868181126f8b7bd67a0dd9306',
    data:temp_prev_data,
    success: function(response) {
        $('#result').html(response['_id']);
        alert(m);
       
    },
    error: function(){
        alert('Fuuuuuuuuuuuuuu');
    }
}); // End Ajax  

});
//Click on present day
$('#present_day').click(function(){
$.post({
    url: 'http://api.reimaginebanking.com/enterprise/customers/58a7effd1756fc834d904a75?key=4068fb9868181126f8b7bd67a0dd9306',
    data:d,
    success: function(response) {
        $('#result').html(response['_id']);
        alert(m);
       
    },
    error: function(){
        alert('Fuuuuuuuuuuuuuu');
    }
}); // End Ajax  

}); // End onclick

//Click on next day
$('#next_day').click(function(){
$.post({
    url: 'http://api.reimaginebanking.com/enterprise/customers/58a7effd1756fc834d904a75?key=4068fb9868181126f8b7bd67a0dd9306',
    data:d+1,
    success: function(response) {
        $('#result').html(response['_id']);
        alert(m);
       
    },
    error: function(){
        alert('Fuuuuuuuuuuuuuu');
    }
}); // End Ajax  

});
//Click on Present Month 
$('#month').click(function(){
$.post({
    url: 'http://api.reimaginebanking.com/enterprise/customers/58a7effd1756fc834d904a75?key=4068fb9868181126f8b7bd67a0dd9306',
    
     data : m,
    success: function(response) {
        $('#result').html(response['_id']);
       
    },
    error: function(){
        alert('Fuuuuuuuuuuuuuu');
    }
}); // End Ajax  

}); // End onclick

});