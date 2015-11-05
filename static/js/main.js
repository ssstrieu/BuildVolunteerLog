$( document ).ready(function(){
    console.log('=======document is now ready!!!!!======');
    
    // $( "#datepicker" ).datepicker();
    
    $('#clearFormBtn').on('click', function(){
        //This returns the form to default entries
        console.log('=======Clear Form clicked======');
        $('#logForm')[0].reset();
    });

    
    $('#studentAbsentBtn').on('click', function(){
        // When the absence button is clicked, this code prefills the form with 'N/A'
        console.log('=======Absence clicked======');
        $('#matchedStudent').prop('checked',true);
        $('#absenceCheck').css('display','inline').prop('checked', true);
        $('#math_topic').val('N/A');
        $('#duration').val('0');
        $('#mentor_rank').val('0');
        $('#scholar_rank').val('0');
        $('#notes').val('Student absent.')
        
    })
        
   
 }); //document-ready close

