var mic;
function setup() {
    mic = new p5.AudioIn();
    mic.start();
    frameRate(2);
}
function draw() {
    background('#3339ff')
    var vol = mic.getLevel();
    // send vol to the server every frame. The framerate is 2 fps so this is every 500ms.
    // If you increrase the framerate, maybe you should use setTimeout instead
    d = {
        "volume": vol
    }
    $.get("/publish", data=d, crossdomain=false)
    //also using jquery for requests is like using an elephant gun to kill gophers
}
