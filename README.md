**QA Ltd Project 1 – CRUD Application**

QuidProQuo lets the user track their net worth in investments, property and cash in one place. QuidProQuo also tracks debt. This allows users to easily get a clear and complete view of their finances.

**Contents**

 - Features
 - Objective and tech stack
 - My method to meet the objective
 - User stories
 - Project Architecture
 - Database structure
	 - Entity Relationship Diagram (ERD)
	 -  CI pipeline
 - Project management
 - Risk assessment
 - Testing reports
 - Further analysis
 - Difficulties faced
 - Future development options including ERD
 - Licence
 - Acknowledgements

**Features**

Users can create a profile, including their:

 - Username
 - Password
 - Assets in property
 - Cash in accounts
 - Investments of stock, shares and cryptocurrencies

Users can see details of their loans, including:

 - Amount borrowed
 - User ID
 - The name of the lender
 - Loan ID

**Tech stack**

The overall objective of this project is to create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate:

 - Project Management – using the Kanban system which means I can create
   tasks and break them down into even smaller tasks. I have used the
   Kanban Board Trello due to its responsive design and the fact that it
   uses real-time. 
  
 - Python as the programming language because it’s beginner friendly and
   extensible.
 - Python Testing – I have used Pytest, which allows for automated
   testing
 - Integration testing with Python (Selenium)
 - The front-end uses Flask (HTML)
 - Git for version control
 - Basic Linux
 - Continuous Integration with Jenkins as the server (not used)
 - The Cloud server used is GCP Compute Engine
 - Databases – I have used GCP SQL Server

**My method to meet the objective**

The following lays out how my app meets each element of CRUD:

CREATE – users create their usernames and passwords, they create an outline of their property, cash and investments and an outline of their loans.

READ – users can read their net worth.

UPDATE – if users buy more property or more stocks and shares, for example, they can update their entry in these categories. When they pay off some of their debt they can amend the amount borrowed.

DELETE – users can delete their profiles.

**User Stories**

1. As a user, I want to create a username, so that I can create a profile.

2. As a user, I want to create an encrypted password, so that I can keep my account secure.

3. As a user, I want to enter and update my assets comprised of property, so my net worth can be updated.

4. As a user, I want to enter and update my assets comprised of cash, so my net worth can be updated.

6. As a user, I want to enter and update my assets comprised of investments, so my net worth can be updated.

7. As a user, I want to enter and update the amount I have borrowed, so my net worth can be updated.

8. As a user, I want to view my net worth, so that I am aware of the amount.

**Project Architecture**

**ERDS:**

The initial ERD was as follows:

However, this became too complicated considering time constraints. So the databases were simplified as can be seen by the following ERD:

![**https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/ERD_Current.png**](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/ERD_Current.png)

As shown in the ERD, there is a one to one relationship between the User Table and the Loans Table, with both tables having a user_id to create a profile with loan and positive equity details and also to create details about the loan. They share a relationship in respect of the loan amount.

**CI Pipeline:**

CI Pipeline Diagram

Please follow the link to the Continuous Integration (CI) Pipeline Diagram:

![https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/CI-Pipeline_Diagram.png](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/CI-Pipeline_Diagram.png)

This diagram shows how my code is developed on my local machine and then pushed to GitHub, then automatically pushed to Jenkins and then installed on the cloud virtual machine. Tests are automatically run from the cloud and reports produced. This automation means that development to deployment is quick and simple.

**Project Management**

The project management tool that I used to track the progress of the project was Trello, specifically the Kanban Board. Here is a link to the board: ![https://trello.com/invite/b/wvmkq4Ex/4caa1ad1754a42f9d7f24d8584876dc8/kanban-board-for-qa-project-1](https://trello.com/invite/b/wvmkq4Ex/4caa1ad1754a42f9d7f24d8584876dc8/kanban-board-for-qa-project-1).

Below is a link to screen shots of the board mid project:

![https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/Trello-Board-1.png](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/Trello-Board-1.png)

![https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/Trello-Board-2.png](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/Trello-Board-2.png)

![https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/Trello-Board-3.png](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/testing-two/git-images/Trello-Board-3.png)

The board was designed to move from left to right:

 - with the _backlog_ first, for things that were not urgent, but would
   be nice to add 
 - to the _design_ list, which contains the ERD and the CI Pipeline
   diagram. The ERD was vital to complete first in order to model the
   minimal viable product (MVP) that is required.
 - I then had a _to do_ list for any miscellaneous but important tasks
   such as the risk assessment, which didn’t fit neatly into another
   category on the board.
 - Then came _user stories_. For every feature of the app, there is a
   user story which breaks down and prioritises what needs to be done
   for the MVP for the project. This forces the developer to always see
   things from the user point of view, putting user experience (UX)
   first.
 - Next was a _doing_ table to move any tasks that I was currently
   working on it to.
 - Then there was _testing._
 - Finally, there is _done_ for tasks which have been completed and
   features implemented and tested.

**Risk Assessment**
![risk assessment table](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/main/git-images/risk-assessment.png)

**Testing Reports**
![URL End Points Coverage](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/main/git-images/URL-Endpoints_Cov.png)

![Coverage Report After Integration Testing](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/main/git-images/cov-report-after-integr-test.png)

![Missing In Coverage Report](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/main/git-images/missing-in-cov.png)


**Further Analysis**

Difficulties Faced

As mentioned above, unfortunately, I misunderstood the testing category on my Trello Kanban Board and listed what tests were to be used. Instead, I should have moved each feature through the board, to _doing_ and then _testing_ and when at the testing stage, I should have tested that feature. I was caught up in developing the app at once and tested at the end, which is the wrong approach and one I will not take in the future. Testing should have been done continuously and will be done continuously in the future.

Further, I ran out of time and GCP credits and did not have a chance to use Jenkins.

ERD of possible developments

A future, much more developed app, could include seven database tables. Please see the image below of the ERD for this future app:

![Future ERD](https://github.com/VickyKR37/QALtd-QuidProQuoApp/blob/main/git-images/future-erd.png)


**Licencing**

No licence.

**Acknowledgments**

I used the following project on GitHub for reference: [https://github.com/TheEarlOfGray/EliteTracker](https://github.com/TheEarlOfGray/EliteTracker)
