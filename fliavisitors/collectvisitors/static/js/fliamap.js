$(document).ready(function() {
    var map = new OpenLayers.Map(
        'tabs-mapa',
        {maxExtent: new OpenLayers.Bounds(-9.517029, 36.961710, -6.189159, 42.154311)}
    );
    var wms = new OpenLayers.Layer.WMS(
        "continente",
        "http://localhost/cgi-bin/g2",
        {
            'layers' : 'distritos,municipios,freguesias'
        },
        {
            transitionEffect: 'resize',
            singleTile: true,
            ratio: 1
        });
    map.addLayer(wms);
    infoControl = new OpenLayers.Control.WMSGetFeatureInfo({
        url: 'http://localhost/cgi-bin/g2',
        title: "Identificar freguesias",
        queryVisible: true,
        eventListeners: {
            getfeatureinfo: function(evt) {
                var lon = map.getLonLatFromPixel(evt.xy).lon;
                var lat = map.getLonLatFromPixel(evt.xy).lat;
                var ajaxURL = "xhr/" + lon + "/" + lat + "/";
                $.get(ajaxURL, function(data) {
                    map.addPopup(
                        new OpenLayers.Popup.FramedCloud(
                            'chicken',
                            map.getLonLatFromPixel(evt.xy),
                            null,
                            data,
                            null,
                            true
                        ),
                        true
                    );
                    $("#submit_btn").click(function() {
                        var freg_id = $("#hidden_freg_pk").val();
                        $.ajax({
                            type: "POST",
                            url: "xhr/" + freg_id + "/vote/",
                            //url: "xhr/" + freg_id + "/ok/",
                            data: $("#vote").serialize(),
                            success: function(data) {
                                //alert(data);
                                thePopup = map.popups[0];
                                //thePopup.contentDiv.innerHTML = "<p>Voto contabilizado</p>";
                                thePopup.contentDiv.innerHTML = data;
                            }
                        });
                        return false
                    });

                });
            }
        }
    });
    map.addControl(infoControl);
    infoControl.activate();
    map.zoomToMaxExtent();
    $(function() {
        $("#tabs").tabs();
        $("#radio").buttonset();
    });
    $("#resultados").click(function() {
        $("#dis-radio").click();
    });

    function show_counts(ajaxURL) {
        $.getJSON(ajaxURL, function(data) {
            var counter = 0;
            var toPlot = [];
            var theTicks = [];
            for(var i in data) {
                var thePosition = data[i][0];
                var theValue = data[i][1];
                var theLabel = i;
                toPlot[thePosition] = {label: theLabel, data: [[thePosition, theValue]]};
                theTicks[thePosition] = [thePosition, theLabel];
                counter += 1;
            }
            var plotOptions = {
                legend: {
                    show: false
                },
                series: {
                    lines: {show: false},
                    points: {show: false},
                    bars: {show: true, align: "center"}
                },
                xaxis: {
                    ticks: theTicks
                },
                grid: {
                    backgroundColor: {colors: ["#fff", "#fff"]}
                }
            };
            $.plot("#chart-area", toPlot, plotOptions);
        });
    }
    $("#dis-radio").click(function() {
        show_counts("xhr/topdistritos/");
    });
    $("#mun-radio").click(function() {
        show_counts("xhr/topmunicipios/");
    });
    $("#freg-radio").click(function() {
        show_counts("xhr/topfreguesias/");
    });
})
