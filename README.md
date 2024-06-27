Project- Content management system-Api in Django restframework
 
1)The system have 2 types of user role, admin and author , admin user are created seeding
2)Author should be able to register and login using username to the cms
3)Admin can create, view, edit and delete contents created by multiple author
4)Author can create ,view, update(edit),delete post by him only
5)user should search content by matching term in title, body
6) user can see all blogs created from other user .

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Acknowledgements
1)External libraries and Tools and Resources:
@postman - for testing code
@https://www.django-rest-framework.org/ - understanding about libraries, function of rest framework, 
syntax etc.
@chatgpt- for solving errors of project.
@Arcitech.AI assignment- using this assignment instruction and try develop project according this 
provided assignment instructions.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Installation
@open cmd or terminalpip install django, 
pip install djangorestframework and useful libraries installing etc.
CMS Project Structure:
Deployment:-
For testing of code I did use postman.
@After completion of my project simply I go to in terminal and give command :-
python.manage.py runserver
@test code on postman:-
---POST http://127.0.0.1:8000/api/account/register/ -------for registeration of user




---POST http://127.0.0.1:8000/api/account/login/ --------for login authorized user
(Generate tokens here during authorized user login)



---POST http://127.0.0.1:8000/api/home/blog/ - for posting or create blog from authorized user
“Here authorized user must be give valid tokens when generate login time”
Note--- authorization token are must be time to time its updated , therefore against go to login and send request 
and get new token and mention it.
----firstly go to above header and mentioned on it Authorization and value coloum mention “Bearer” word and 
give space and add token then you get allowed permission and simply click on send , then you found blog 
format , and simply you can follow, go to above body and type according format information and you post 
successfully your blog (see above image)


GET http://127.0.0.1:8000/api/home/blog/ - for author can see all post created by him
Note--- authorization token are must be time to time its updated , therefore against go to login and send request 
and get new token and mention it.
----firstly go to above header and mentioned on it Authorization and value coloum mention “Bearer” word and 
give space and add token then you get allowed permission and simply click on send , then you get your blog
(see above image)



PUT http://127.0.0.1:8000/api/home/blog/3/ - for authorized user update only created blog by him
Note--- authorization token are must be time to time its updated , therefore against go to login and send request 
and get new token and mention it.
----firstly go to above header and mentioned on it Authorization and value coloum mention “Bearer” word and 
give space and add token then And go to header and add on key Content-Type and value give application/json you get 
allowed permission and simply update and click on send , then you get your updated blog (see above image)
http://127.0.0.1:8000/api/home/blog/3/-----> here type blogid of which you want update blog



DELETE http://127.0.0.1:8000/api/home/blog/3/  for user can delete post only created by him
authorization token are must be time to time its updated , therefore against go to login and send request and get 
new token and mention it.
----firstly go to above header and mentioned on it Authorization and value coloum mention “Bearer” word and 
give space and add token then you get allowed permission and http://127.0.0.1:8000/api/home/blog/3/--> here type blogid of
which you want delete blog simply delete and click on send , then your blog deleted (see above image)




GET http://127.0.0.1:8000/api/home/blog/?search=arcitech - for user can search particular word from blog
authorization token are must be time to time its updated , therefore against go to login and send request and get 
new token and mention it.
----firstly go to above header and mentioned on it Authorization and value coloum mention “Bearer” word and 
give space and add token then you get allowed permission and http://127.0.0.1:8000/api/home/blog/?search=arcitech--> here 
type word which you want and you find blog associated word simply click on send , then your text found in blog (see above 
image)



GET http://127.0.0.1:8000/api/home/blog/?random=true - for authorized user view random blogs
See 2
nd output
See above 2 images difference, you can see. authorized user can see all blogs created by other user




Admin :-
Open your browser and paste link ----http://127.0.0.1:8000/admin/login/?next=/admin/

Username- admin
Password- 123

Admin handle all blogs created by user, admin can update, post, delete, create, see all blogs







@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
output___
![registration](https://github.com/thechamp710/arcitech.ai/assets/135342237/2d4c2a95-d61d-4f2c-9a47-308f4481373a)- Registeration user




![login](https://github.com/thechamp710/arcitech.ai/assets/135342237/3ef5c550-4ef7-46cb-97d3-2a459bb68aa1)---login



![addblog](https://github.com/thechamp710/arcitech.ai/assets/135342237/7169d178-56f3-489f-bde9-add4eb2aeed1)---create blog from authorized user


![viewallpostcreated by him](https://github.com/thechamp710/arcitech.ai/assets/135342237/9efdf3c2-2b3c-4343-abf8-c1e603cbfb3c) 
----user view all post created by him






















introduction (myself)
Hello, 
This is a sahil siddheshwar kamble
Currently, I am pursuing bachelors of engineering in computer science (artificial intelligence and data science) 
at new horizon Institute of technology and management thane, 
I have completed my intermediate education (diploma in computer engineering) at VPM polytechnic thane with 
an aggregation 76.97%
I have good knowledge about python programming language as well as SQL, 
I know about HTML, CSS and some machine learning algorithms. 
Now I am searching internship for gaining real experience in IT industry. And with the help of this internship 
opportunitie i make my bright future in IT career, therefore I have need of internship for proving my works in 
your company.
I want to do internship, because I want to get experience in this field, I am eager to experience all the aspects of 
how it works in actual company, how they handle, also after internship I will get its certificate, recommendation 
letter, my cv will be stronger.
