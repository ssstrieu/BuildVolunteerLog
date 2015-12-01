$( document ).ready(function(){
    console.log('=======document is now ready!!!!!======');
    
    $('#clearFormBtn').on('click', function(){
        //This returns the form to default entries
        console.log('=======Clear Form clicked======');
        $('#logForm')[0].reset();
    });

    // When the absence button is clicked, this code prefills the form with 'N/A' or absences values
    $('#studentAbsentBtn').on('click', function(){
        console.log('=======Absence clicked======');
        $('#matchedStudent').prop('checked',true);
        $('#absenceCheck').css('display','inline').prop('checked', true);
        $('#math_topic').val('N/A');
        $('#duration').val('0');
        $('#mentor_rank').val('0');
        $('#scholar_rank').val('0');
        $('#notes').val('Student absent.')
        
    });
    
    // sets Absence to 0 if Dropin Student is selected
    $('#dropinStudent').on('click', function(){
        console.log('=======Dropin student cannot be absent. Absence reset======');
        $('#absenceCheck').prop('checked', false); 
    });
        
   
 }); //document-ready close

