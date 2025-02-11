<!-- PROJECT LOGO -->
<p align="center">
    <img src="https://github.com/OpenGeoOne/qgis-drone-flight-planner/blob/main/images/GeoFlightPlanner.png" alt="Logo" width="85" height="80">
  <h3 align="center">GeoFlight Planner</h3>
  <p align="center">
    <b><i>A versatile QGIS plugin for drone flight planning, ensuring optimized flight paths and high-quality data capture.</i><b>
    <br />
  </p>
</p>
        
        
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>GeoFlightPlanner</summary>
  <ol>
      <li><a href='#horizontal-flight'>Horizontal Flight</a></li>
         <ul>
           <li><a href="#following-terrain-sensor">Following terrain - Drone Sensor</a></li>
           <li><a href="#following-terrain-manual">Following terrain - Manual Lateral and Frontal Distance</a></li>
        </ul>
      <li><a href='#vertical-flight'>Vertical Flight</a></li>
        <ul>
          <li><a href="#circular">Circular</a></li>
          <li><a href="#facade">Facade</a></li>
       </ul>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#tips">Tips</a></li>
    <li><a href="#how-to-contribute-by-learning-more">How to contribute by learning more</a></li>
    <li><a href="#authors">Authors</a></li>
  </ol>
</details>


## GeoFlight Planner Plugin
<p>A QGIS plugin for precise drone flight planning, designed for photogrammetry, 3D inspections, and building facade mapping. It includes tools for terrain-following flights, circular paths around structures, and vertical facade mapping, generating KML files for 3D visualization and CSV files compatible with Litchi or other flight apps.<br></p>

### Horizontal Flight
It generates KML files for 3D visualization in Google Earth and a CSV file compatible with the Litchi app.
It can also be used with other flight applications by utilizing KML files for flight lines and waypoints.
<div align="center">
</div>

### Following terrain Sensor
This tool enables drone flight planning for photogrammetry, following terrain elevations and calculating lateral and frontal overlaps based on the <b>drone’s sensor parameters</b>.

### Following terrain Manual
This tool enables a simple drone flight planning for photogrammetry, following terrain elevations with manually defined side and front spacing values.

![following-terrain](https://github.com/user-attachments/assets/86042dcb-0d89-4c7b-9789-f989d6d86e91)

### Vertical Flight
Tools for Vertical Flight Plan.
<div align="center">
</div>

### Circular
This tool is designed to plan vertical and circular flights, ideal for 3D inspection and mapping projects around towers and similar objects.<br>
It enables the creation of an optimized flight path to capture detailed images of the object's surroundings.
<p><b>Required configurations:</b></p>
<ul>
  <li><b>Estimated object height:</b><span> Defines the highest point of the structure to be inspected.<o:p></o:p></span></li>
  <li class="MsoNormal" style=""><b><span>Vertical spacing:</span></b><span> Determines the distance between capture levels along the object's height.<o:p></o:p></span></li>
  <li class="MsoNormal" style=""><b><span>Number of photos per base circle (segments):</span></b><span> Specifies the number of photos to be captured at each circular level.<o:p></o:p></span></li>
</ul>
<p><span>The outputs are <b>KML</b> files for 3D visualization in <b>Google Earth</b> and a <b>CSV</b> file compatible with the <b>Litchi app</b>. It can also be used with other flight applications by utilizing the KML files for flight lines and waypoints.</span></p>

![circular](https://github.com/user-attachments/assets/166372ad-0bed-4ca4-be2b-14b03dd5350d)


### Facade
This tool is designed for creating vertical flight plans tailored for mapping building facades, ideal for architectural projects and building inspections.
It enables the planning of a precise vertical trajectory with appropriate overlap and stop times for the drone, ensuring high-quality photographs and detailed mapping.</span></p>
<p class="MsoNormal"><b>Configuration Details:</b></p>
<ul style="margin-top: 0cm;" type="disc">
  <li><b><span>Estimated Facade Height:</span></b><span> Specifies the highest point of the facade to be mapped.</span></li>
  <li><b><span>Flight Base Line:</span></b><span> The path along which the drone will fly in front of the facade.</span></li>
  <li><b><span>Position of the Facade:</span></b><span> A reference point on the facade used to calculate overlap distances.</span></li>
  <li><b><span>Manually entered side and front distance</span></b><span></li>
</ul>
<p class="MsoNormal"><span>The outputs are <b>KML</b> files for 3D visualization in <b>Google Earth</b> and a <b>CSV</b> file compatible with the <b>Litchi app</b>. It can also be used with other flight applications by utilizing the KML files for flight lines and waypoints.</span></p>

![facade](https://github.com/user-attachments/assets/6566854d-cc7a-48f4-9016-2230e5657ddb)


## Requirements
The following plugins must bem installed and activated in QGIS:
<ul style="margin-top: 0cm;" type="disc">
  <li><b>LFTools</b></li>
  <li><b>Open Topography</b></li>
  <li><b>KML Tools</b></li>
</ul>

## Tips
<ul style="margin-top: 0cm;" type="disc">
  <li><a href="https://geoone.com.br/opentopography-qgis/" target="_blank">Obtain the API Key for the Open Topography plugin</a><o:p></o:p></span></li>
  <li><a href="https://geoone.com.br/plano-de-voo-para-drone-com-python/#sensor" target="_blank">Check your drone sensor parameters</a><o:p></o:p></li>
</ul>

## How to contribute by learning more
Purchase one of our online courses or e-book on the GeoOne platform.
<div style="text-align: center;"><a
 href="https://geoone.com.br/pvplanodevoo2"><img
 style="border: 2px solid ;" alt="Plano de Voo"
 title="PLANO DE VOO NO QGIS"
 src="https://geoone.com.br/wp-content/uploads/2025/01/Plano-de-voo-no-QGIS.jpg"></a>
<br>
</div>


## Authors
Prof Cazaroli 
<div style="text-align: center;"><a
 href="https://www.linkedin.com/in/prof-cazaroli-458377274/" target="_blank"><img
 style="border: 0px solid ;width: 20px" alt="GeoCAR no QGIS"
 title="Prof Cazaroli"
 src="https://user-images.githubusercontent.com/52215653/163875911-3ff4d34b-bf67-4b2b-9d2c-8525c1c011a6.png"></a>
<br>

Leandro França
<div style="text-align: center;"><a
 href="https://www.linkedin.com/in/leandro-fran%C3%A7a-93093714b/" target="_blank"><img
 style="border: 0px solid ;width: 20px" alt="GeoCAR no QGIS"
 title="Leandro França"
 src="https://user-images.githubusercontent.com/52215653/163875911-3ff4d34b-bf67-4b2b-9d2c-8525c1c011a6.png"></a>
<br>

