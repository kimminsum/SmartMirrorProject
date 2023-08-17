function wttrinfo() {
    $.get("/wttrinfo", function (data) {
        $(".wttrinfo_icon").attr("src", data.forecast_icon);
        $("#forecast").text(data.forecast);
        $("#tmp_min_max").text(data.temperature["temp_min"]+"~"+data.temperature["temp_max"]+" °C");
        $("#temp_tmp").text(data.temperature["temp"]+" °C");
        $("#temp_feelslike").text(data.temperature["feels_like"]+" °C");
    });
}
function clock() {
    $.get("/clock", function (data) {
        $("#date").text(data.date);
        $("#times").text(data.times);
    });
}
wttrinfo();
clock();
var wttrinfo_update = setInterval(wttrinfo, 10000);
var clock_wttrinfo = setInterval(clock, 1000);