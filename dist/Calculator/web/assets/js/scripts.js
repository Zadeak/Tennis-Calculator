
// uses python  to get htmlcode with use of template system
async function newHtml(mode,type){
  let result = await eel.getHtmlcode(mode,type)();
  document.getElementById('loadhere').innerHTML = result;
};
//uses python to calculate total bet for one set
async function calculate_TotalOneSet(x1,x2,vector,bet){
  let res = await eel.TotalOneSet(x1,x2,vector,bet)();
  $("#here").html(res).css("display","none");
  $("#here").fadeIn("fast");
};
// uses python to calculate handycap bet for one set
async function calculate_H1set(x1,x2,P1P2,bet){
  let res = await eel.H1set(x1,x2,P1P2,bet)();
  $("#here").html(res).css("display","none");
  $("#here").fadeIn("fast");
};


// uses python to calculate handycap bet for match
async function calculate_Hfullset(x1,x2,x3,x4,x5,x6,P1P2,bet){
  let res = await eel.Hfullset(x1,x2,x3,x4,x5,x6,P1P2,bet)();
  $("#here").html(res).css("display","none");
  $("#here").fadeIn("fast");
};
// uses python to calculate total bet for match
async function calculate_TotalMatch(x1,x2,x3,x4,x5,x6,vector,bet){
  let res = await eel.TotalMatch(x1,x2,x3,x4,x5,x6,vector,bet)();
  $("#here").html(res).css("display","none");
  $("#here").fadeIn("fast");
};

// controll elements display and calls calculate function for handycap set bet settelment
function HandycapOneSet () {
  var $main_column = $(".content-wraper");
  if ($('.content').length) {
    $('.content').fadeOut("slow",function(){
      $(".content").remove();
      var $content = $("<div id='loadhere' class='content'></div>")
      let mode = "handycap"
      let type = "Set"
      newHtml(mode,type);
      $main_column.append($content).css("display","none");
      $main_column.fadeIn("slow",function(){
        $('#login').submit(function(e){
          e.preventDefault();
          var fscore = $("select[name='firstScore']").val();
          var sscore = $("select[name='secondScore']").val();
          var radioValue = $("input[name='vector']:checked").val();
          var quantity = $("input[name='quantity']").val();
          calculate_H1set(fscore,sscore,radioValue,quantity);
        });
      });

    })
  }
}
// controll elements display and calls calculate function for total set bet settelment

function TotalOneSet () {
    var $main_column = $(".content-wraper");
    if ($('.content').length) {
        $('.content').fadeOut("slow",function(){
            $(".content").remove();
            var $content = $("<div id='loadhere' class='content'></div>")
            let mode = "total"
            let type = "Set"
            newHtml(mode,type);
            $main_column.append($content).css("display","none");
            $main_column.fadeIn("slow",function(){
            $('#login').submit(function(e){
                e.preventDefault();
                var fscore = $("select[name='firstScore']").val();
                var sscore = $("select[name='secondScore']").val();
                var radioValue = $("input[name='vector']:checked").val();
                var quantity = $("input[name='quantity']").val();
                calculate_TotalOneSet(fscore,sscore,radioValue,quantity);
        });
      });
    });
  };
}

// controll elements display and calls calculate function for handycap match bet settelment
function HandycapMatch () {
  var $main_column = $(".content-wraper");
  if ($('.content').length) {
    $('.content').fadeOut("slow",function(){
      $(".content").remove();
      var $content = $("<div id='loadhere' class='content'></div>")
      let mode = "handycap"
      let type = "match"
      newHtml(mode,type);
      $main_column.append($content).css("display","none");
      $main_column.fadeIn("slow",function(){
        $('#login').submit(function(e){
          e.preventDefault();
          var s1Fscore = $("select[name='s1Fscore']").val();
          var s1Sscore = $("select[name='s1Sscore']").val();
          var s2Fscore = $("select[name='s2Fscore']").val();
          var s2Sscore = $("select[name='s2Sscore']").val();
          var s3Fscore = $("select[name='s3Fscore']").val();
          var s3Sscore = $("select[name='s3Sscore']").val();
          var radioValue = $("input[name='vector']:checked").val();
          var quantity = $("input[name='quantity']").val();
          calculate_Hfullset(s1Fscore,s1Sscore,s2Fscore,s2Sscore,s3Fscore,s3Sscore,radioValue,quantity);
        });
      });
    });
  }
}
// controll elements display and calls calculate function for total match bet settelment

function TotalMatch () {
    var $main_column = $(".content-wraper");
    if ($('.content').length) {
      $('.content').fadeOut("slow",function(){
        $(".content").remove();
        var $content = $("<div id='loadhere' class='content'></div>")
        let mode = "total"
        let type = "match"
        newHtml(mode,type);
        $main_column.append($content).css("display","none");
        $main_column.fadeIn("slow",function(){
          $('#login').submit(function(e){
            e.preventDefault();
            var s1Fscore = $("select[name='s1Fscore']").val();
            var s1Sscore = $("select[name='s1Sscore']").val();
            var s2Fscore = $("select[name='s2Fscore']").val();
            var s2Sscore = $("select[name='s2Sscore']").val();
            var s3Fscore = $("select[name='s3Fscore']").val();
            var s3Sscore = $("select[name='s3Sscore']").val();
            var radioValue = $("input[name='vector']:checked").val();
            var quantity = $("input[name='quantity']").val();
            calculate_TotalMatch(s1Fscore,s1Sscore,s2Fscore,s2Sscore,s3Fscore,s3Sscore,radioValue,quantity);
          });
        });
      });
    }
  }
// when page is loaded attaches even handlers
$(document).ready(function () {
  console.log("Ready!");
  var $welcome_content = $('.content')
  var $main_column = $(".content-wraper")
  const methods = { 'handyset': HandycapOneSet,
                  'handymatch' : HandycapMatch,
                  'totalset' : TotalOneSet,
                  'totalmatch' : TotalMatch
  }
  var buttons = $(".nav-link")
  buttons.each(function (e){

    var $this = $(this);
    e.preventDefault;

    $this.click(function (){
      findClass = $this.attr('class').split(" ")[1];
      methods[findClass]();
    });

  });

});
