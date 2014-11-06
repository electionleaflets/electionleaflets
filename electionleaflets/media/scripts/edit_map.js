//EDIT MAP
function editMap(){

    this.mode = "draw";
    this.map = null;
    this.oldLinePoints = "";
    this.line = null;
    this.switched = false;
    this.drawFromStart = false;
    this.lastEditedMarker = null;
    this.canDraw = false;
<<<<<<< HEAD
    this.waypointMarkers = new Array();
=======
    this.waypointMarkers = new Array();    
>>>>>>> origin/current_live

    this.setup = function (sMapProvider, nLng, nLat, iZoom){

        //copyright
        var copyOSM = new GCopyrightCollection("<a href=\"http://www.openstreetmap.org/\">OpenStreetMap</a>");
        copyOSM.addCopyright(new GCopyright(1, new GLatLngBounds(new GLatLng(-90,-180), new GLatLng(90,180)), 0, " "));

        //tiles
        var tilesMapnik     = new GTileLayer(copyOSM, 1, 17, {tileUrlTemplate: 'http://tile.openstreetmap.org/{Z}/{X}/{Y}.png'});
        var tilesOsmarender = new GTileLayer(copyOSM, 1, 17, {tileUrlTemplate: 'http://tah.openstreetmap.org/Tiles/tile.php/{Z}/{X}/{Y}.png'});

        //map
        var mapMapnik     = new GMapType([tilesMapnik],     G_NORMAL_MAP.getProjection(), "Mapnik");
        this.map           = new GMap2(document.getElementById("divMapContainer"), { mapTypes: [mapMapnik] });

        this.map.addControl(new GLargeMapControl());
        this.map.addControl(new GMapTypeControl());
        this.map.setCenter( new GLatLng(nLat, nLng), iZoom);
<<<<<<< HEAD

=======
        
>>>>>>> origin/current_live
        //map resize
        this.resizeMap();
        window.onresize = this.resizeMap;

        //reset map for drawing
        //line
        this.line = new GPolyline([]);
        //this.line.enableDrawing();
        this.map.addOverlay(this.line);
        this.canDraw = true;

        //line events
        GEvent.addListener(this.line, "lineupdated", this.onLineChanged);
<<<<<<< HEAD
        GEvent.addListener(this.line, "click", this.wayPointClicked);
        //GEvent.addListener(this.line, "mouseover", oEditMap.onLineMouseOver)
        //GEvent.addListener(this.line, "mouseout", oEditMap.onLineMouseOut);

        //map events
        GEvent.addListener(this.map, "zoomend",
            function(){
                if(oEditMap.mode == 'draw' && oEditMap.map.getZoom() > 10){
                    oEditMap.line.enableDrawing();
                }else{
                    oEditMap.line.enableEditing();
                }
            }
        );


        GEvent.addListener(this.map, "mouseover",
            function() {
                if(oEditMap.mode == 'draw' && oEditMap.map.getZoom() > 10){
=======
        GEvent.addListener(this.line, "click", this.wayPointClicked);    
        //GEvent.addListener(this.line, "mouseover", oEditMap.onLineMouseOver)
        //GEvent.addListener(this.line, "mouseout", oEditMap.onLineMouseOut);                    

        //map events
        GEvent.addListener(this.map, "zoomend", 
            function(){
                if(oEditMap.mode == 'draw' && oEditMap.map.getZoom() > 10){                    
                    oEditMap.line.enableDrawing();
                }else{
                    oEditMap.line.enableEditing();                    
                }                
            }
        );    


        GEvent.addListener(this.map, "mouseover", 
            function() {
                if(oEditMap.mode == 'draw' && oEditMap.map.getZoom() > 10){                    
>>>>>>> origin/current_live
                    oEditMap.line.enableDrawing();
                }
            }
        );
<<<<<<< HEAD

        GEvent.addListener(this.map, "mouseout",
=======
        
        GEvent.addListener(this.map, "mouseout", 
>>>>>>> origin/current_live
            function() {
               oEditMap.line.enableEditing();
            }
        );

    }
<<<<<<< HEAD

=======
    
>>>>>>> origin/current_live
    //set mode
    this.setMode = function(sMode){
        this.mode = sMode;
        if(this.mode == 'draw'){
<<<<<<< HEAD
            this.line.enableDrawing();
=======
            this.line.enableDrawing();  
>>>>>>> origin/current_live
            this.line.enableEditing();
            this.disableAddInstruction();
        }else{
            this.line.disableEditing();
            this.line.enableEditing();
            this.enableAddInstruction();
        }
    }
<<<<<<< HEAD

=======
    
>>>>>>> origin/current_live
    this.modeSelectionChanged = function(){
        if($('radMode_Draw').checked == true){
            this.setMode('draw');
        }else{
            this.setMode('instruction');
        }
    }

    //reset
    this.reset = function(bConfirm){
<<<<<<< HEAD

=======
        
>>>>>>> origin/current_live
        //confirm?
        var bProceed = true;

        if(bConfirm != undefined){
            bProceed = confirm("Are you sure you want to reset your map?");
        }

        if(bProceed == true){
            //clear existing overlays
            this.map.clearOverlays();

            //line
            this.line = new GPolyline([]);
            this.map.addOverlay(this.line);
            this.canDraw = true;
<<<<<<< HEAD

            //line events
            GEvent.addListener(this.line, "lineupdated", this.onLineChanged);
=======
    
            //line events
            GEvent.addListener(this.line, "lineupdated", this.onLineChanged);      
>>>>>>> origin/current_live
            GEvent.addListener(this.line, "click", this.wayPointClicked);

            this.map.addOverlay(this.line);

<<<<<<< HEAD
            //reset vars
            this.waypointMarkers = new Array();
            this.oldLinePoints = "";
            this.lastEditedMarker = null;

=======
            //reset vars       
            this.waypointMarkers = new Array();
            this.oldLinePoints = "";
            this.lastEditedMarker = null;         
            
>>>>>>> origin/current_live
            //remove waypoints
            $('divEditTextShrink').innerHTML = '';
        }
    }
<<<<<<< HEAD

=======
    
>>>>>>> origin/current_live
    //jump to place
    this.jump = function (){
        var sSearch = $('txtJump').value;
        if(sSearch != ''){
            var oGeoCoder = new GClientGeocoder();
            oGeoCoder.getLatLng(sSearch, oEditMap.jumpCallback);
        }
    }

    this.jumpCallback = function(oLatLong){
        oEditMap.map.setCenter(oLatLong);
        oEditMap.map.setZoom(12);
    }

    //map resize
    this.resizeMap = function(){
        var iPageHeight = window.innerHeight - ($('divPage').offsetTop + 50);
        iMapHeight = iPageHeight - ($('divHeader').offsetHeight + $('divEditHeader').offsetHeight);
<<<<<<< HEAD
        var iWaypointHeight = iMapHeight - $('divWayPoint').parentNode.offsetHeight;
=======
        var iWaypointHeight = iMapHeight - $('divWayPoint').parentNode.offsetHeight;        
>>>>>>> origin/current_live

        $('divPage').style.height = iPageHeight + "px";
        $('divEditMap').style.height = iMapHeight + "px";
        //$('divEditTextWrapper').style.height = iWaypointHeight + "px";
    }

    //on  line change
    this.onLineChanged = function(){
        oEditMap.checkChangedPoint();
        oEditMap.copyOldLineDetails();
    }
<<<<<<< HEAD

    this.onLineMouseOver = function(oPoint){
        oEditMap.line.enableEditing();
=======
    
    this.onLineMouseOver = function(oPoint){      
        oEditMap.line.enableEditing();       
>>>>>>> origin/current_live
    }

    this.wayLineMouseOut = function(){
        oEditMap.line.enableDrawing();
    }
<<<<<<< HEAD

=======
        
>>>>>>> origin/current_live
    //way point mouse events
    this.wayPointClicked = function(oPoint){

        //check if clicked on a vertex of the line
        var bFound = false;
        for (var i=0; i < oEditMap.line.getVertexCount(); i++) {
            if(oPoint.equals(oEditMap.line.getVertex(i))){
                bFound = true;
                break;
            }
        }

        if(bFound == true){
            //set last way point and scroll if required
            oEditMap.setLastEditedPoint(oPoint);
<<<<<<< HEAD
            oEditMap.scrollToWayPoint(oPoint);
        }

    }

    this.wayPointMouseOver = function(oPoint){
        oEditMap.line.enableEditing();
=======
            oEditMap.scrollToWayPoint(oPoint);    
        }
         
    }
    
    this.wayPointMouseOver = function(oPoint){      
        oEditMap.line.enableEditing();       
>>>>>>> origin/current_live
    }

    this.wayPointMouseOut = function(){
        oEditMap.line.enableDrawing();
    }

    //set last edited point
    this.setLastEditedPoint = function (oPoint){
<<<<<<< HEAD

        if(oEditMap.lastEditedMarker == null){
           oEditMap.lastEditedMarker = new GMarker(oPoint);
		   oEditMap.map.addOverlay(oEditMap.lastEditedMarker);
        }else{
            oEditMap.lastEditedMarker.setLatLng(oPoint);
        }

        this.enableAddInstruction();
    }

    //scroll to waypoint
    this.scrollToWayPoint = function(){

=======
          
        if(oEditMap.lastEditedMarker == null){
           oEditMap.lastEditedMarker = new GMarker(oPoint); 
		   oEditMap.map.addOverlay(oEditMap.lastEditedMarker);           
        }else{
            oEditMap.lastEditedMarker.setLatLng(oPoint);    
        }
        
        this.enableAddInstruction();
    }
    
    //scroll to waypoint
    this.scrollToWayPoint = function(){
        
>>>>>>> origin/current_live
    }

    //near existing point?
    this.nearExistingPoint = function (oPoint){

        var oReturn = false;
        for (var i=0; i < oEditMap.line.getVertexCount(); i++) {
            oLinePoint = oEditMap.line.getVertex(i);
            if(oLinePoint.distanceFrom(oPoint) < 100){
                oReturn = oLinePoint;
            }
        }
<<<<<<< HEAD

=======
        
>>>>>>> origin/current_live
        return oReturn;
    }

    //check if weypoint text needs handling
    this.saveWeypointText = function(){

        if($('txtWaypoint').value != ""){

            //make element for sidebar
        	var oNewWaypoint = document.createElement("div");
        	oNewWaypoint.className = "waypoint";

            //add location and text to hidden inputs
            var oDirections = document.createElement("input");
<<<<<<< HEAD
            var oEditedPointLatLong = oEditMap.lastEditedMarker.getLatLng();
=======
            var oEditedPointLatLong = oEditMap.lastEditedMarker.getLatLng();                        
>>>>>>> origin/current_live
            oDirections.type = "hidden";
            oDirections.name = "hidDirection_" + oEditedPointLatLong.lng() + ',' + oEditedPointLatLong.lat();
            oDirections.value = 'direction@|@' + oEditedPointLatLong.lng() + ',' + oEditedPointLatLong.lat() + '@|@' + $('txtWaypoint').value;
            oDirections.className = "directionposition";
<<<<<<< HEAD

            //set display text
        	oNewWaypoint.innerHTML = '<img src="" style="class:hidden;"/><p>' + $('txtWaypoint').value + '</p>';
        	oNewWaypoint.appendChild(oDirections);

=======
   
            //set display text
        	oNewWaypoint.innerHTML = '<img src="" style="class:hidden;"/><p>' + $('txtWaypoint').value + '</p>';
        	oNewWaypoint.appendChild(oDirections);
        	
>>>>>>> origin/current_live
        	var iInsertPosition = this.getPathWaypointPosition(oEditedPointLatLong.lng(), oEditedPointLatLong.lat());

            //add to page in correct position
        	if(iInsertPosition < 1){
<<<<<<< HEAD
        	    $('divEditTextShrink').appendChild(oNewWaypoint);
        	}else{
        	    $('divEditTextShrink').insertBefore(oNewWaypoint, $('divEditTextShrink').childNodes[iInsertPosition + 1]);
=======
        	    $('divEditTextShrink').appendChild(oNewWaypoint);        	    
        	}else{
        	    $('divEditTextShrink').insertBefore(oNewWaypoint, $('divEditTextShrink').childNodes[iInsertPosition + 1]);        	            	            	    
>>>>>>> origin/current_live
    	    }

            //work out how far to scroll
          //var iOffset = $('divEditTextScroll').offsetTop - ($('divEditTextShrink').offsetHeight - oNewWaypoint.offsetHeight);
<<<<<<< HEAD

=======
          
>>>>>>> origin/current_live
            var iOffset = 0;
            if($('divEditTextShrink').offsetHeight > $('divEditTextWrapper').offsetHeight){
                iOffset = oNewWaypoint.offsetHeight;
            }
<<<<<<< HEAD

            Effect.MoveBy('divEditTextScroll', 0 - iOffset, 0);

            $('txtWaypoint').value = "";

            //redraw
            this.redrawWayPoints();

=======
            
            Effect.MoveBy('divEditTextScroll', 0 - iOffset, 0);
              
            $('txtWaypoint').value = "";
            
            //redraw
            this.redrawWayPoints();
            
>>>>>>> origin/current_live
            //diable adding controls
            this.disableAddInstruction();
        }
    }
<<<<<<< HEAD

    this.disableAddInstruction = function(){
        $('txtWaypoint').disabled = true;
        $('btnSaveWayPoint').disabled = true;
    }

    this.enableAddInstruction = function(){
        $('txtWaypoint').disabled = false;
        $('btnSaveWayPoint').disabled = false;
    }

=======
    
    this.disableAddInstruction = function(){
        $('txtWaypoint').disabled = true;
        $('btnSaveWayPoint').disabled = true;   
    }
    
    this.enableAddInstruction = function(){
        $('txtWaypoint').disabled = false;
        $('btnSaveWayPoint').disabled = false;   
    }
    
>>>>>>> origin/current_live
    //redraw the way points
    this.redrawWayPoints = function(){

        //remove all weypoint markers
        for (var i=0; i < this.waypointMarkers.length; i++) {
            this.map.removeOverlay(this.waypointMarkers[i]);
        };

        //get all waypoints
        var aDirectionPositions = document.getElementsByClassName('directionposition');
        for (var i=0; i < aDirectionPositions.length; i++) {

            //get positions
            var aSplit = aDirectionPositions[i].value.split('@|@');
            aSplit = aSplit[1].split(',')

            //setup icon
<<<<<<< HEAD
            var baseIcon = getBaseIcon();
=======
            var baseIcon = getBaseIcon(); 
>>>>>>> origin/current_live

            // create marker
            var letter = String.fromCharCode("A".charCodeAt(0) + i);
            var letteredIcon = new GIcon(baseIcon);
            letteredIcon.image = "http://www.google.com/mapfiles/marker" + letter + ".png";
            markerOptions = { icon:letteredIcon };
            var oMarker = new GMarker(new GLatLng(aSplit[1], aSplit[0]), markerOptions);
<<<<<<< HEAD

            //events
            GEvent.addListener(oMarker,"mouseover", this.wayPointMouseOver);
            GEvent.addListener(oMarker,"mouseout", this.wayPointMouseOut);
            GEvent.addListener(oMarker,"click", this.wayPointClick);

=======
            
            //events
            GEvent.addListener(oMarker,"mouseover", this.wayPointMouseOver);
            GEvent.addListener(oMarker,"mouseout", this.wayPointMouseOut);
            GEvent.addListener(oMarker,"click", this.wayPointClick);            
            
>>>>>>> origin/current_live
            //add to map and store in array
            this.map.addOverlay(oMarker);
            this.waypointMarkers.push(oMarker);
        };

        //update the markers in the sidebar
        var aWayPoints = document.getElementsByClassName('waypoint');
        for (var i=0; i < aWayPoints.length; i++) {
<<<<<<< HEAD

	        var oImage = document.createElement("img");
            var letter = String.fromCharCode("A".charCodeAt(0) + i);

            aWayPoints[i].childNodes[0].src = oImage.src = "http://www.google.com/mapfiles/marker" + letter + ".png";
            aWayPoints[i].childNodes[0].style.display = "block";

        };

=======
	        
	        var oImage = document.createElement("img");
            var letter = String.fromCharCode("A".charCodeAt(0) + i);	        

            aWayPoints[i].childNodes[0].src = oImage.src = "http://www.google.com/mapfiles/marker" + letter + ".png";
            aWayPoints[i].childNodes[0].style.display = "block";
            
        };
        
>>>>>>> origin/current_live
    }

    //get the position of a waypoint along the path
    this.getPathWaypointPosition = function(iLng, iLat){
<<<<<<< HEAD

        var aWayPoints = this.getWayPointLatLongs();
        var iPosition = 0;

        for (var i=0; i < oEditMap.line.getVertexCount(); i++) {

=======
        
        var aWayPoints = this.getWayPointLatLongs();
        var iPosition = 0;
        
        for (var i=0; i < oEditMap.line.getVertexCount(); i++) {
            
>>>>>>> origin/current_live
            //get current point
            var oPoint = oEditMap.line.getVertex(i);

            //loop though waypoints
            for (var ii=0; ii < aWayPoints.length; ii++) {
<<<<<<< HEAD

                if(aWayPoints[ii][0] == oPoint.lng() && aWayPoints[ii][1] == oPoint.lat()){
=======
                
                if(aWayPoints[ii][0] == oPoint.lng() && aWayPoints[ii][1] == oPoint.lat()){                    
>>>>>>> origin/current_live
                    iPosition +=1;
                }
                if(iLng == oPoint.lng() && iLat == oPoint.lat()){
                    return iPosition;
                }
            }
<<<<<<< HEAD

        }

        return iPosition - 1;
    }

=======
            
        }
        
        return iPosition - 1;
    }
    
>>>>>>> origin/current_live
    //get teh last & longs of thee waypoints
    this.getWayPointLatLongs = function (){
        var aReturn = new Array();
        var aDirectionPositions = document.getElementsByClassName('directionposition');
        for (var i=0; i < aDirectionPositions.length; i++) {

            //get positions
            var aSplit = aDirectionPositions[i].value.split('@|@');
            aSplit = aSplit[1].split(',');
            aReturn.push(aSplit);
        }
<<<<<<< HEAD

=======
        
>>>>>>> origin/current_live
        return aReturn;
    }

    //check if any points have been added
    this.checkChangedPoint = function(){

        for (var i=0; i < oEditMap.line.getVertexCount(); i++) {

            var oPoint = oEditMap.line.getVertex(i);
<<<<<<< HEAD
            var bFound = false;

            for (var ii=0; ii < oEditMap.oldLinePoints.length; ii++) {

                 var oOldPoint = oEditMap.oldLinePoints[ii];
                 if(oOldPoint.lng == oPoint.lng() && oOldPoint.lat == oPoint.lat()){
                     bFound = true;
                 }
=======
            var bFound = false;            

            for (var ii=0; ii < oEditMap.oldLinePoints.length; ii++) {
            
                 var oOldPoint = oEditMap.oldLinePoints[ii];
                 if(oOldPoint.lng == oPoint.lng() && oOldPoint.lat == oPoint.lat()){                    
                     bFound = true;
                 } 
>>>>>>> origin/current_live
            }

            //if not found
            if(bFound == false){
<<<<<<< HEAD
                this.setLastEditedPoint(oPoint);
=======
                this.setLastEditedPoint(oPoint);     
>>>>>>> origin/current_live
                return // assumes only one has changed
            }
        }

    }

    //check if any points have been added
    this.getLineGeometry = function(){

        var sReturn = "";
        for (var i=0; i < oEditMap.line.getVertexCount(); i++) {
             var oPoint = oEditMap.line.getVertex(i);
            sReturn += (oPoint.lng() + "," + oPoint.lat() + "|");
        }

        var oBounds = oEditMap.line.getBounds();
        var oSouthWest = oBounds.getSouthWest();
<<<<<<< HEAD
        var oNorthEast = oBounds.getNorthEast();

        //$('hidBounds').value = oSouthWest.lng() + "," + oSouthWest.lat() + ',' + oNorthEast.lng() + "," + oNorthEast.lat();

        return sReturn;
    }

=======
        var oNorthEast = oBounds.getNorthEast();        
        
        //$('hidBounds').value = oSouthWest.lng() + "," + oSouthWest.lat() + ',' + oNorthEast.lng() + "," + oNorthEast.lat();
        
        return sReturn;
    }
    
>>>>>>> origin/current_live
    //copy old line details so we can compare when teh line changes
    this.copyOldLineDetails = function(){
        var aOldLine = new Array;
        for (var i=0; i < oEditMap.line.getVertexCount(); i++) {
            var oPoint = oEditMap.line.getVertex(i);
            var oSimplePoint = new SimplePoint(oPoint.lng(), oPoint.lat());
<<<<<<< HEAD
            aOldLine[aOldLine.length] = oSimplePoint;
        };
        oEditMap.oldLinePoints = aOldLine;
    }

=======
            aOldLine[aOldLine.length] = oSimplePoint;            
        };
        oEditMap.oldLinePoints = aOldLine;
    }
    
>>>>>>> origin/current_live
    this.addDetail = function(){
        showGreyOut();
        $('divWalkDetails').style.display = "block";
    }

    this.saveWalk = function (){
        $('hidPolyline').value = this.getLineGeometry();
        postBackForm('frmEditWalk');
    }

}
