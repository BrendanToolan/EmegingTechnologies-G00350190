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
        ctx.strokeStyle = $('#Color').val();
        ctx.lineWidth = $('#Width').val();
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

function submit(){
    canvas = document.getElementById("canvas");
    console.log(canvas.toDataURL());
    $.post("uploadimage", {"theimage": canvas.toDataURL})
}