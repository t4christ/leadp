$(function () {
  
 
  
    /* Functions */
  /* Score Load Form */
    var loadForm = function () {
      var btn = $(this);
      
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-book").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
          

        }
      });
    };
  


/* Info Load Form */
    var infoForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-book").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
        }
      });
    };
  




/* Student Assess Submit Load Form */
    var studentAssessForm = function () {
      var btn = $(this);
      
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-book").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
      
        }
      });
    };




    /* Assess Load Form */
    var assessForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-book").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
        }
      });
    };
 


   /* Class Load Form */
   var classForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  };


/* Scored Form */
    var saveForm = function () {
      var pri=$("#pri").val()
      var pritest=$("#editapk").val()
      var prinfo=$("#editipk").val()
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {

            $(".scoreview").fadeOut(800,function(){
              $(".scoreview").load(" .scoreview").fadeIn().delay(2000)
            });

            $("#tr_" + pri).fadeOut(1000);
            $("#tr_" + pritest).fadeOut(1000);
            $("#tr_" + prinfo).fadeOut(1000);
            
            $("#modal-book").modal("hide").fadeOut(1000);
        
        }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };








    /* Student Submit Updated Form */
    var studentAssessSaveForm = function (event) {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $(".studentview").fadeOut(800,function(){
              $(".studentview").load(" .studentview").fadeIn().delay(2000)
            
            });

            
            $("#modal-book").modal("hide").fadeOut(1000);
        
        }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };








  

    /* Info Updated Form */
    var infoSaveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $(".infoview").fadeOut(800,function(){
              $(".infoview").load(" .infoview").fadeIn().delay(2000)
            });

            
            $("#modal-book").modal("hide").fadeOut(1000);
        
        }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };



    /* Assess Updated Form */
    var assessSaveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $(".assessview").fadeOut(800,function(){
              $(".assessview").load(" .assessview").fadeIn().delay(2000)
            });

            
            $("#modal-book").modal("hide").fadeOut(1000);
        
        }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };

  

/* Class Updated Form */
var classSaveForm = function () {
  var form = $(this);
  var data= new FormData($(this).get(0))
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    dataType: 'json',
    success: function (data) {
      if (data.form_is_valid) {
        $(".classview").fadeOut(800,function(){
          $(".classview").load(" .classview").fadeIn().delay(2000)
        });

        
        $("#modal-book").modal("hide").fadeOut(1000);
    
    }
      else {
        $("#modal-book .modal-content").html(data.html_form);
      }
    }
  });
  return false;
};



    /* Binding */
  
    // Create book
 //   $(".js-create-book").click(loadForm);
   // $("#modal-book").on("submit", ".js-book-create-form", saveForm);
  
    // Update score
    $("body" ).on("click", ".js-update-score", loadForm);
    $("#modal-book").on("submit", ".js-update-scores", saveForm);

  //Update Info

    $("body" ).on("click", ".js-update-info",infoForm);
    $("#modal-book").on("submit", ".js-update-infos", infoSaveForm);


  //Update assess

  $("body" ).on("click", ".js-update-assess", assessForm);
  $("#modal-book").on("submit", ".js-update-tests", assessSaveForm);


  //Update class

  $( "body").on("click",".js-update-class", classForm);
  $("#modal-book").on("submit", ".js-update-classes", classSaveForm);

//Delete Lecture Class
$("body").on("click", ".js-delete-class", loadForm);
$("#modal-book").on("submit", ".js-class-delete-form", saveForm);


//Delete Lecture Test
$("body").on("click", ".js-delete-test", loadForm);
$("#modal-book").on("submit", ".js-test-delete-form", saveForm);



//Delete Lecture Info
$("body").on("click", ".js-delete-info", loadForm);
$("#modal-book").on("submit", ".js-info-delete-form", saveForm);


  //Update student test

  $("body").on("click", ".js-update-student-test", studentAssessForm);
  $("#modal-book").on("submit", ".js-update-student-tests", studentAssessSaveForm);




  });

  



/* Assess Edit */

/* Score Edit 

$(document).ready(function(){
var edit = $('.edita').attr("id")
var use = $('.user').val()
var std = $('.std').val()
var assign_del = $('#assign-del').val()
var id = $('#editapk').val()
var pk = $('#priscore').val()

$("body").on('click','.edit',function(){
 scoreSee();
});

});


function scoreSee(){
  var edit = $('.edita').attr("id")
  var use = $('.user').val()
  var std = $('.std').val()
  var assign_del = $('#assign-del').val()
  var id = $('#editapk').val()
  var pk = $('#priscore').val()
// AJAX Request
$.ajax({
  url:  edit ,
  type: 'GET',
  dataType:"json",
  data: { id: pk},
  beforeSend: function () {
    $("#modal-book").modal("show");
  },
  success: function (data) {
    $("#modal-book .modal-content").html(data.html_form);
  }

  /*success: function(response){
     data=$(response).find("#score");
    $('#tr_' + pk ).html(data).fadeIn();
     }
     });
    }





/* Score Student Submitted 
function scoreStudent(){
  
    var edita = $('#edita').val()
    var assign= $('#editauser').val()
  
    var assigndiv= $('#assign-del').val()
    var pk = $('#editapk').val()
    var std = $('.std').val()
  $('#modal-book').on('submit','.submita',function(event){
    event.preventDefault();
    var pathscore=$(this).attr("action")
    var methscore=$(this).attr("method")
    var datscore=$(this).serialize()
   // AJAX Request
          $.ajax({
            url: pathscore ,
            type: methscore,
            data:datscore,
            dataType:"json",
            /*data: { pk: pk,'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()},
            headers:{'X_METHODOVERRIDE': 'UPDATE'},
            success: function (data) {
              if (data.form_is_valid) {
               // $("#submission").html(data.html_form_detail);  // <-- Replace the table body
                //$("#modal-book").modal("hide");
                alert("Score Given!");  // <-- This is just a placeholder for now for testing
              }
              else {
                $("#modal-book .modal-content").html(data.html_form);
              } 
              
               }
               });
               return false;
  
  });
  
  }
*/












/* Lecture Class Remove */
$(document).ready(function(){

  $('#delete').click(function(){

	var del = $('#classdel-value').val()




    var post_arr = [];
    $('#recordsTable input[type=checkbox]').each(function() {
      if (jQuery(this).is(":checked")) {
        var id = this.id;
        var splitid = id.split('_');
        var postid = splitid[1];

        post_arr.push(postid);

      }
    });

    if (confirm("Are you sure you want to delete this Class Schedule")){
    if(post_arr.length > 0){

        // AJAX Request
        $.ajax({
          url: '/' + del + '/',
          type: 'POST',
          data: { pk: post_arr, 'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()},
          success: function(response){
             $.each(post_arr, function( i,l ){
                $("#tr_"+l).remove().fadeOut(2000);
             });
          }

        });
    }
}
  });

});


/*Lecture Test Remove */
$(document).ready(function(){
  
    $('#remove').click(function(){
  
    var testdel = $('#testdel').val()
  
  
  
  
      var post_arr = [];
      $('#recordsTable input[type=checkbox]').each(function() {
        if (jQuery(this).is(":checked")) {
          var id = this.id;
          var splitid = id.split('_');
          var postid = splitid[1];
  
          post_arr.push(postid);
  
        }
      });
  
      if (confirm("Are you sure you want to delete this Class Schedule")){
      if(post_arr.length > 0){
  
          // AJAX Request
          $.ajax({
            url: '/' + testdel + '/',
            type: 'POST',
            data: { pk: post_arr, 'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()},
            success: function(response){
               $.each(post_arr, function( i,l ){
                  $("#tr_"+l).remove().fadeOut(2000);
               });
            }
  
          });
      }
  }
    });
  
  });
  



$(document).ready(function(){

  $('#deleteinfo').click(function(){

  var del = $('#delete-value').val()




    var post_arr = [];
    $('#recordsTable input[type=checkbox]').each(function() {
      if (jQuery(this).is(":checked")) {
        var id = this.id;
        var splitid = id.split('_');
        var postid = splitid[1];

        post_arr.push(postid);

      }
    });

    if (confirm("Are you sure you want to delete this Info Schedule")){
    if(post_arr.length > 0){

        // AJAX Request
        $.ajax({
          url: '/' + del + '/',
          type: 'POST',
          data: { pk: post_arr, 'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()},
          success: function(response){
             $.each(post_arr, function( i,l ){
                $("#tr_"+l).remove().fadeOut(1000);
             });
          }

        });
    }
}
  });

});
