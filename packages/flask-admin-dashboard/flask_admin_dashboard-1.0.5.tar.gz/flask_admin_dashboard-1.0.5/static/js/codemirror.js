$(document).ready(function(){

    CodeMirror.defineMode("customMode", function() {
        return {
            token: function (stream, state) {

                if (stream.match("INFO")) {
                    return "info";
                } else if (stream.match("ERROR")) {
                    return "error";
                } else if (stream.match("WARNING")){
                    return "warning"
                } else if (stream.match(/\d+(?=\.)\.(?<=\.)\d*/g)) {
                    return "number"
                }
                // } else if (stream.match(/\d\d:\d\d:\d\d,\d\d\d/g)) {
                //     return "time"
                // } else if (stream.match(/([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/g)){
                //     return "date"
                // }

                else {
                    stream.next();
                    return null;
                }
            }
        };
    });

    window.myCodeMirror = CodeMirror.fromTextArea(document.getElementById("txtScript"), {
       lineNumbers: true,
        mode: 'customMode',
        readOnly: true,
        viewportMargin: Infinity,
    });

});