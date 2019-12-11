var mousePressed = false;
var Lastx, Lasty;
var ctx;

function Init() {
    ctx = document.getElementById('canvas').getContext("2d");
    
    $('#canvas').mousedown(function (e) {
        mousePressed = true;
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top,
        false);
    })

    $('#canvas').mousemove(function (e) {
        if (mousePressed) {
            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
        }
    });

    $('#canvas').mouseup(function (e) {
        mousePressed = false;
    });
	    $('#canvas').mouseleave(function (e) {
        mousePressed = false;
    });

}

function Draw(x, y, isDown) {
    if(isDown) {
        ctx.beginPath();
        ctx.strokeStyle = "white";
        ctx.lineWidth = 10;
        ctx.lineJoin = "round";
        ctx.moveTo(Lastx, Lasty);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    Lastx = x; Lasty= y;
}

function clearArea() {
    ctx.setTransform(1,0,0,1,0,0);
    ctx.clearRect(0,0, ctx.canvas.width, ctx.canvas.height);
}

//j query 
function submit(){
    var canvas = document.getElementById("canvas");
  //  console.log(canvas.toDataURL());
    var dataURL = canvas.toDataURL();
    console.log(dataURL);

    $.post("predict", {"theimage": canvas.toDataURL()})

    $.ajax({
        type: "POST",
        url: "/predict",
        data: {
            imgBase64: dataURL
        }
    }).done(function(result){
        console.log('SENT' + result);
        $("#result").empty().append(result);
    });
};

/*function submit(){
    canvas = document.getElementById("canvas");
    console.log(canvas.toDataURL());
    $.post("predict", {"theimage": canvas.toDataURL()})
}*/