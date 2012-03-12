$(document).ready(function() {
    //OpenLayers.ProxyHost = "/cgi-bin/proxy_ol.cgi?url=";
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
                $.getJSON(ajaxURL, function(data) {
                    /*
                    var result = "";
                    for(var i in data[0]) {
                        result += i + " = " + data[0][i] + "\n";
                    };
                    alert(result);
                    */
                    map.addPopup(
                        new OpenLayers.Popup.FramedCloud(
                            'chicken',
                            map.getLonLatFromPixel(evt.xy),
                            null,
                            //map.getLonLatFromPixel(evt.xy),
                            data[0]["fields"]["freguesia"] + "<br />visitantes: " + data[0]["fields"]["visitors"],
                            //evt.text,
                            null,
                            true
                        ),
                        true
                    );
                });
            }
        }
    });
    map.addControl(infoControl);
    infoControl.activate();
    map.zoomToMaxExtent();
    $(function() {
        $("#tabs").tabs();
    });
})
