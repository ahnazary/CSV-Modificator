# CSV-Modificator
### A brief explanation about each method and its arguments <br/> <br/>

**createFormattedAddressColumn method :<br/>**
<img src="README_Docs/method call_createFormattedAddressColumn.png" width="350">
<br/>
Calling this classmethod on CSV files which include data referring to a physical location (E.g. "latitude" and "longitude" as the initial data of a location) will add a new column called: "Formatted Address" containing the formatted address of the initial location. An example of this method's function is given below:
<br/> <br/>
initial .CSV file :
<br/>
<img src="README_Docs/geolocation_initialCSV.png" width="450">

final .CSV file :
<br/>
<img src="README_Docs/geolocation_finalCSV.png" width="450">
<br/> 

A SQL database containing initial and formatted addresses of location is created for higher effiency:
<br/>
<img src="README_Docs/SQLAddress.png" width="450">
<br/> 

------------------------------------------------------
