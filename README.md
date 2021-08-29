# gym_manager_app

This is my first solo project undertaken during the Professional Software Development course at CodeClan. 
It is written in python and is intended to be a gym manager web app that uses Flask as a framework and postgreSQL for the database.

The brief given included the following goals:

- Allow the gym to create and edit members
- Allow the gym to create and edit activities
- Allow the gym to book members on specific activities
- Show a list of all upcoming activities
- Should show all members that are booked in for a particular activity

I included some extra features as extensions to the app:

- Activities have a maximum capacity, and members can only be added while there is space remaining.
- Premium membership where only premium members can join premium tier activities.

To run the app:

- create a database called "gym"
- run "gym.sql" to setup tables
- run "console.py" to add some initial entries to the database
- run "app.py" with command "Flask run" in terminal

Further development:

- Date and time stored as strings rather than datetime.
- some sort of calendar to allow for a more practical booking system.
- footer obscures lower entries in displayed tables due to how it has been anchored.
