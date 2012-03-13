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
                    var pp = map.addPopup(
                        new OpenLayers.Popup.FramedCloud(
                            'chicken',
                            map.getLonLatFromPixel(evt.xy),
                            null,
                            //map.getLonLatFromPixel(evt.xy),
                            //data[0]["fields"]["freguesia"] + "<br />visitantes: " + data[0]["fields"]["visitors"],
                            data,
                            //evt.text,
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
                            data: $("#vote").serialize(),
                            success: function(data) {
                                /*
                                alert("Voto contabilizado!"); 
                                */
                                alert(data);
                                pp["contentHTML"] = data;
                            }
                        });
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
    });
})
