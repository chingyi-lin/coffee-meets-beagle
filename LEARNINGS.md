#Project Description

From a high level, Coffee Meets Beagle is a service that allows users to discover and match with different animals from the shelter. We envisioned two different types of users using our API. These are:

* Users potentially interested in adopting a dog
* Shelter staff who take care of the dogs

Below, we've outlined the functionality that we believe is crucial towards addressing the needs from both interested users and staff members.


#Functionality
*Sign Up - POST /user/signup*

User will send their sign up information to this endpoint to create their accounts on this service. We require users to provide unique email addresses and username. We also ask users to enter the age because mostly shelters require people to be 18 years old or above to schedule an appointment or become a volunteer.

*Log in:  POST /user/login*

Users’ login request will be sent to this endpoint to be verified. If the information is incorrect, the user will be notified.

*Sending donation: POST /donate*

This endpoint will handle the donation request to the animal at a given id with a default amount of customized amount in USD. If there is no pet at the pet ID or if there is no user at the user ID, an error will be returned.

*Sending visit intention: POST /visit*

Users’ visiting intention will send to this endpoint to indicate their interest of scheduling a visit and/or a volunteering session. If there is no pet at the entered pet ID or if there is no user at the entered user ID, an error will be returned.

*Sending preferable timeslots for visiting: POST/PUT /visit/date*

User can use this endpoint to indicate their availability for scheduling a visit and/or a volunteering session. If there is no user ID at the entered user ID, an error will be returned.

*Create animal information and availability: POST /animal*

Staff members will be able to add animals to the database as well as their availability. If they don't enter required values in the missing fields, an error will be returned.

*Call API to insert animal information and availability: POST /animal*

The GetYourPet API is called in order to get data on 25 different dogs. Documentation can be found here: https://getyourpet.com/api-documentation/

*Update animal information, availability and activity: Put /animal/<id>*

Staff accounts will be able to edit existing values for the animals information, availability, activity, and other fields. If there is no pet at the pet ID, an error will be returned.

*Retrieving animal’s availability:  Get /animal/availability/{Pet_id}*

Users will be able to retrieve an animals availability by entering the pet ID to choose their preferred time slot. If there is no pet at the pet ID requested, an error will be returned.

*The animal’s activity: Get /animal/activity/{Pet_id}*

Users will be able to retrieve the animals activity by using the pet ID. If there is no pet at the pet ID requested, an error will be returned.


#Implementation
We divided our application into a couple layers:

* A web service that manages the end points from the frontend
* An data-api layer that extracts and transforms the data and send it to the web service layer.

For the web service and data-api layers (also called backend layers), we used Flask as the major development framework. SQLight was chosen as the method for deploying our database. We also used SQLAlchemy.

While building out separate endpoints in a group, we used dummy data individually in order to test the success of our code. Once successful, we combined our endpoints together and extracted data on 25 different dogs by using the GetYourPet API. 
