1. What are the various features you would like your project to offer?
The features my project will offer is interacting with formula 1 data to look at race times, points in the driver/team championship, race results, and location of the races.

2. What are the API endpoints that you would need to set up for each feature? List them along with the respective HTTP verb, endpoint URL, and any special details (query parameters, request bodies, headers).
GET - Race Results
GET - Driver Points
GET - Team Points
GET - Location of Race
GET - Race Times
POST - Races
POST - Driver Results
PUT - Driver Results

3. Provide a description of the database tables required for your application, including column names, data types, constraints, and foreign keys. Include your database name. You can optionally include an ER diagram.
Races - ID, Race Times, Race Position, Location of Race, Driver ID, Results ID
Results - ID, Driver Results, Team Results, Team Points, Driver Points, Driver ID, Races ID