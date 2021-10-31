# PataParivartanBackend

### THEME - ADDRESS UPDATE
### CHALLENGE - Address Update using supporting documents

## Challenges
1. There is no specific timeline that when an individual will receive his or her updated Aadhaar card after application.
2. There have been quite a few reported cases of individuals not receiving their updated Aadhaar because of rejected applications, lost in transit, delivery negligence, or the centre does not facilitate delivery.

## Solution
The solution uses the assistance of the mobile aadhaar operator. The operator will be provided by a portal/app. The operator using his mobile would scan the supporting document like electricity or water bill to extract the address and validate its accuracy by using GPS. There should be a provision to edit the address and add the left-out locality name to the address. This addition of street name or any other field should be validated so that it doesn't refer to an altogether new address. Validation of the new address is to be performed electronically and the outcome must be stored in a data structure, so that it can be uploaded to the UIDAI servers for further analysis. 

## Our Hack
**PataParivartan**
PataParivartan is an app/portal developed for mobile Aadhaar operators. It allows the operator to scan the document, extract the address, edit the address, validate the address using GPS, and store the corrected address in the UIDAI database.

## Overall Workflow
**1. Frontend and Backend**
The frontend is built using React Native web framework and backend using Flask. 

**2. Tesseract OCR in use**
For extracting the address from the scanned document PataParivartan uses open-source Tesseract OCR. 

**3. [PostalPincode API](http://www.postalpincode.in/Api-Details)**
Pincode is extracted from the JSON output of the tesseract-ocr. This pincode is passed as a query to postalpincode API to extract details of the place like city, state etc. The response from this API are then validated with the OCR extracted response, if it matches then the process is carried on else terminated.

**4. Provision to edit the address**
The extracted address then automatically got entered in the address fields, which further provides a provision to edit the address and add the left-out locality name to the address.

**5. Forward Geocoding**
The edited address is then converted into the geo-coordinates(latitude and longitude) using the forward geocoding method of Positionstack API. [Positionstack](https://positionstack.com/) provides 25,000 requests per month for free.

**6. Locating mobile operator's position**
The app asks for accessing the location of the mobile device and then HTML5 Geolocation API is used to locate the operator's position. The geo-coordinates are extracted from the JSON response of the API. 

**7. Comparing the two coordinates**
Distance between the current coordinates and coordinates we got using forward geocoding is done using Mapbox Matrix API. This step is done to ensure that the edited address doesn't refer to an altogether new address. Mapbox Matrix API returns the distance between two points as JSON respone.

**8. Stored in UIDAI Database**
If the distance between two locations is less than 4 metres then the address is stored in the UIDAI  database else the process of updating the address is terminated and started from scanning the document again.

**9. Google Lighthouse**
Lighthouse which is an free open-source chrome extension is used to generate audit reports.

## Concept Note(Blueprint)
![WhatsApp Image 2021-10-30 at 18 23 28](https://user-images.githubusercontent.com/69745609/139577963-c51fcbc2-76ab-44ce-9e08-63c7e4974d37.jpeg)

## Tech Stack
* Frontend - React Native
* Backend - Flask
* API - HTML5 GeolocationAPI, Positionstack API, Mapbox Matrix API
* Hosting - 

## A step beyond...
* Using [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics) to get clear actionable insight into app issues with this powerful realtime crash reporter.
* Improving the logging.cfg file to make the application more robust.
* Using computer vision algorithms to create OCR API to make it more accurate.

## Audit Report
![Screenshot 2021-10-31 170534](https://user-images.githubusercontent.com/69745609/139581400-b42de443-1010-4e32-9022-be7454603063.png)

[Auditlogs.pdf](https://github.com/MPUATFORCES/PataParivartanBackend/files/7448532/Auditlogs.pdf)

## Presentation-Slides
[Presentation-Slides](https://www.canva.com/design/DAEuH3MhCrU/share/preview?token=Ic546kbhcW22ZJP5prKIKA&role=EDITOR&utm_content=DAEuH3MhCrU&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)
