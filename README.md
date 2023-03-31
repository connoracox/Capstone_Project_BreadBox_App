# capstone-project-flask
Capstone Project: Flask app: BreadBox. Food waste reducing application by Connor Cox.

For my capstone project at Coding Temple, I created the BreadBox app using Flask, Python, HTML(jinja) and CSS with a database from ElephantSQL.
The app takes 2 different types of users, Vendors and Users.
Vendors (local restaurants, bakeries, cafes, etc. register and sign into their account. 
They then have the options to "Post Boxes" (make posts about boxes of extra food that the shop has at the end of the day, 
that would normally get thrown out at the end of the day (bagels, donuts, pizza, etc.)
After posting boxes, the boxes are generated on their profile.

The other option is to register as a User (someone who would buy the boxes).
After register and sign in, the User has the option to "Explore Food" 
which is a page of every box posted by every Vendor. (query all in "Posts" db model).
They can then select "Reserve Box" on a box of food they want to buy and they are taken to 
a "My Boxes" page where they can view their Order Confirmation Number and QR Code.

I want to continue to build out the functionality to make the "My Boxes" page 
populate the actualy box of food that was clicked with the box info, 
instead of just a generic order confirmation page.

Languages/Framework/database: Python, HTML(jinja), CSS, Flask, ElephantSQL
