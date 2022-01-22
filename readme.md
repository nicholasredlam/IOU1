# I.O.U. 1
#### Video Demo:  https://www.youtube.com/watch?v=kghir8uGp9s
#### Hands-On Demo: https://share.streamlit.io/nicholasredlam/iou
#### Description: Users can create, read, update, and delete requests for help in this app designed to be a "marketplace" for favours.

#####Building the App
This app was built using Python and [Streamlit](https://streamlit.io/), which streamlines a lot of the front-end design when it comes to functions such as dropdown boxes and submit buttons.
At its heart, it is a CRUD app - much like a simple web blog - albeit employed in a different context. For creating a CRUD app in Python and Streamlit, I followed JCharisTech's tutorial,
available at https://www.youtube.com/watch?v=i6gt2OKezOQ.

#####Design
It was important to me that the app was sleek and intuitive - after all, if users are busy enough to need to ask for favours, they'll be too busy to bother figuring out something complex and tedious.
For this reason, I decided to limit myself to 3 - 4 functional pages. Admittedly, only three should be in constant use - Add a Favour, Favour List, and Tackle a Favour - deletion, ideally, shouldn't happen, but exists as a safety measure.
Text inputs are also kept simple and trim. I did debate extensively about having the date function - as it added an extra step that didn't feel like it added much value. However, I decided to add it in noting that an expiry does assist users in connoting the actual urgency of their favour, and might also provide an opportunity in the future to create a feature by which expired favours are marked as such (and users should be notified of their expiry in advance for their own follow-up).

#####Explanation of Files
db_fxns.py was the file in which I collected all the different functions I intended to call - for example, get_task , edit_task_data , and delete_data. These functions are rather neutral in that they are standard in many CRUD app setups.
streamlit_app.py was the file in which I cobbled these functions together into a coherent programme that had a "narrative flow" imposed upon it by the context that this was a "favour request" form.

#####Towards I.O.U. 2
I hope to improve the application in several ways.
Now, admittedly, the app functions on an honor system. It would have been better with a username and password implemented, which will remove the need to key in your name when adding a favour, or taking on a task. Furthermore, it adds an added layer of security if a rule is added that only the owner of the favour can delete their own favours.
Alas, Streamlit is limited in that it reruns the code with every submission of a form - so I might have to find an alternative to Streamlit. As painful as it sounds, HTML will certainly afford me this ability as demonstrated in some of the later CS50 lectures.
Streamlit's capabilities are also terribly underutilised in this app - it offers a suite of analytical tools, which could be used to make a very visually appealing leaderboard - with a simple Favours Requested / Completed ratio displaying the top few users of the month.
This would truly be a step towards actually gameifying goodwill.
I.O.U. 1 was certainly an exciting project, and I'm definitely not done with it - but for now I'm happy to present what I have produced in the journey so far.
Thanks, CS50!
