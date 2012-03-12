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
		$.get("xhr/" + map.getLonLatFromPixel(evt.xy).lon + "/" + map.getLonLatFromPixel(evt.xy).lat + "/", function(data) {
			alert(data);
		});
                map.addPopup(
                    new OpenLayers.Popup.FramedCloud(
                        'chicken',
                        map.getLonLatFromPixel(evt.xy),
                        null,
                        //map.getLonLatFromPixel(evt.xy),
                        '<strong>type:</strong> ' + evt.type + '<br /><strong>coords:</strong>' + map.getLonLatFromPixel(evt.xy) + '<br /><strong>text:</strong>' + evt.text,
                        //evt.text,
                        null,
                        true
                    ),
                    true
                );
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
