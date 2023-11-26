# Mobile Trade

[Link to deployed site](https://mobiletrade-2f5fcc81b06c.herokuapp.com/)

<hr>
Mobile Trade is a full stack E-Commerce website which allows its users to buy and sell mobile phones. This project is made using Django framework and incorporates other technologies including HTML, CSS, Bootstrap and Javascript. The website enables its users to perform CRUD functionalities post creation of their individual user accounts. This project is made as a part of Code Institute’s Full Stack Portfolio milestone project.

![mobiletrade Image](./assets/readme/)

# Table Of Content

- [User Experience & Design](#user-experience)

  - [Site Goals](#site-goals)
  - [Scope](#scope)
  - [User Stories](#user-stories)
  - [Developer Tasks](#developer-tasks)
  - [Wireframes](#Wireframes)
  - [Database Schema](#Database-Schema)
  - [Colour Scheme](#colour-scheme)
  - [Fonts](#Fonts)
  - [Github and Agile Methodology](#Github-and-Agile-Methodology)
    - [Introduction](#introduction)
    - [EPICS(Milestones)](<#epics(milestones)>)
    - [User Stories issues](<#user-stories-(issues)>)
    - [MoSCoW prioritization](<#moscow-prioritization-(Labels)>)
    - [GitHub Projects](#github-projects)

- [Features](#features)
  - [Navbar](#Navbar)
  - [Footer](#Footer)
  - [Home](#Home)
    - [Hero Section](#hero-section)
    - [New Additions](#new-additions)
    - [Mobile Card](#mobile-card)
  - [Mobiles Page](#mobiles-page)
    - [Search Form](#search-form)
    - [Results Section](#results-section)
  - [Mobile Details Page](#mobile-details-page)
    - [Images](#images)
    - [Mobile Details](#mobile-details)
    - [Seller Details](#seller-details)
    - [Favourites](#favourites)
  - [Profile Page](#profile-page)

## User Experience

### Site Goals

1. To provide users with a platform to buy and sell mobile phones.
2. To provide users understanding of current second hand market for mobile phones with exposure to prices and availability.
3. To provide a platform for the users to maintain record of their own mobile phones which they wish to sell as well as the ones they may be interested in buying.
4. To ensure avalability of website across devices.

### Scope

The project focuses on developing a responsive web app which would allow its users to list , view, manage and delete mobile phones. The app is aimed to be/ provide

- Responsive and User friendly
- Easy to navigate through
- Easy to use and understand
- Essential features like Profile and Listing management
- Notifications for various actions
- User centric design
- Options to contact/ get in touch for assistance via E-mail, Phone or Social media

### User Stories

1. As a Site User I can visit home page of the website,  so that i can know more about the purpose of the website.

2. As a Site User I want the website to be responsive,  so that I can view it on multiple devices of different resolutions.

3. As a Site User I can navigate through website,  so that I can proceed to any section as per my preference.

4. As an Unregistered Site User I can SignUp/register on website,  so that I can create a User Account.

5. As a Registered User I can login using my credentials,  so that I can access my user profile page and other functionalities

6. As a Logged in User I can view my profile page,  so that I can access all available functionalities for a registered user

7. As a Registered User I can delete my profile,  so that I can remove all my personal info including my listings and favourites from the website.

8. As a Registered User I can reset my profile password,  so that I can regain access to my user account if I forget my password.

9. As a Registered User I can manage my favourite listings,  so that I can Add to, View and Delete from my favourites list.

10. As a Registered User I can manage my listings,  so that I can Add to and View products from My Listings.

11. As a Registered User I can manage my listings,  so that I can Update and Delete items from My Listings.

12. As a Site User I can see the recent mobile phone additions to website,  so that I know whats newly available.

13. As a Site User I can visit Listings Page,  so that I can see all the listed mobile phones on the website.

14. As a Site User I can search for a mobile phone based on Brand, Model, Maximum and Minimum Price,  so that I can find mobile phones as per my preferences.

15. As a Site User I can view/visit Product Details Page,  so that I can see all details of the product I am interested in.

16. As a Registered Site User I want an option to contact Mobile Trade,  so that seller is informed if I am interested in buying or for any other queries related to phone.

### Developer Tasks

1. Project Design and Installing Django
2. Setting up Database and File storage
3. Initial Deployment on Heroku
4. Testing
5. Documentation

### Wireframes

Wireframes were made with the help of Balsamiq.

- Home
  ![Home](./assets/readme/wireframes/)
- Profile
  ![profile](./assets/readme/wireframes/)
- Mobiles
  ![mobiles](./assets/readme/wireframes/)
- Mobile Details
  ![mobile-details](./assets/readme/wireframes/)
- Log in
  ![login](./assets/readme/wireframes/)
- My Listings
  ![my listings](./assets/readme/wireframes/)
- My Fovourites
  ![my listings](./assets/readme/wireframes/)

### Database Schema

![database schema](./assets/readme/)

### Colour Scheme

The website incorporates shades of black, grey, with complementary neutrals. This scheme ensures professional and user-friendly appearance and enhances visual appeal of the website.

The colour scheme effectively compliments the content of the website without pulling away user attention from them.
![Colour Scheme](./assets/readme/)

### Fonts

The font used in this project is default Oswald, which very well compliments the content and design of the website.

#### Models

The Project comprises of below models

1. User

This model is imported from Django Allauth. The predefined fields which were used were username, first name, last name, email, name and password. User model is associated with Profile model with one to one relationship and is used for user authentication.

2. Profile

This model handles the user profile details. Autosave is used to create user profile whenever a new User registers. Auto deletion of user profile happens in the event user account deletion.

3. Mobile

The mobile model is connected to the User with a Foreign Key : seller. On deletion of user, mobile details are deleted automatically.

6. Favourites

This model saves all favourites associated to a Profile. The model is connected to User and Mobile models (Foreign Keys : seller and mobile. On deletion of either favorutes is deleted automatically.

### Github and Agile Methodology

#### Introduction

This project was developed using agile principles on GitHub. All functions and features were broken down into Issues(User Stories). Depending on their nature Issues were grouped under Milestones (Epics). Each Issue had its own acceptance criteria and assigned tasks. Depending on importance and requirement, each Issue were given a Label basis MoSCoW prioritization. The entire development was monitored using a Kanban board available under Projects on GitHub.

#### EPICS (Milestones)

The project was diveded into 6 Milestones (Epics). All Issues (User Stories) were initially put under product backlog initially and moved to their respective Millestones. All new Issues and bugs were added to Product Backlog Milstone <br>
![Milestones](./assets/readme/)

#### User Stories (Issues)

Issues were comprised of User Story and its Acceptance criteria along with relevant Tasks <br>
![Issues](./assets/readme/)

#### MoSCoW prioritization (Labels)

GitHub's Labels were used to implement MoSCoW Prioritization (Must have, Should have, Could have, and Won't have) of User Stories. Along with these two more Labels Developer Task and Bugs were also used. This helped in categorisation and prioritisation of different Issues. <br>
![Labels](./assets/readme/)

#### GitHub Projects

GitHub Projects was user to keep track of workflow. This was done with the help of basic kanban board which clearly divided the Issues into three different stages of development which were Todo, Doing and Done <br>
![Projects](./assets/readme/)

## Features

### Navbar

The Navigation bar was built using bootstrap and is responsive across devices. It is present on all pages and has brand name and logo which when clicked redirects user to home page. Unautheticated users of the website will be able to see three links which are Home, Mobiles and Login. For authenticated users there will be 4 links which are Home, Mobiles, My Profile and Logout. On small devices user will see hamburger menu with same options.

![nav logged out](./assets/readme/features/)
![nav logged in](./assets/readme/features/)
![nav mobile collapsed](./assets/readme/features/)
![nav mobile expanded](./assets/readme/features/)

### Footer

The footer is common accross pages and commucates Website name, Purpose, Address, Contact details, Social Media links and copyrights.

![Footer](./assets/readme/features/)

### Home

#### Hero Section

The Hero section comprises of an image of mobile phones and a tag line "Buy and Sell Mobiles" which immediately communicates the purpose of website to its user. The image and tag perfectly compliments the design and rest of the components on the home page.

![Hero section](./assets/readme/features/)

#### New Additions

New Addition section displays the latest four mobiles added to the website. These are displayed using cards.

![Recent Listings](./assets/readme-images/features/recent-listings.PNG)

#### Mobile Card

The mobile card was made with bootstrap and consisits of mobile phone's Brand name, Model, Image, Price and a Link to go to mobile details page.

![Listing Card](./assets/readme/features/)

### Mobiles Page

#### Search Form

The search section allows users to filter mobiles basis Brand, Minimum Price and Maximum Price.

![Search Form](./assets/readme/features/)

#### Results Section

This section display the results of the search done by the user.

![Results Section](./assets/readme/features/)

### Mobile Details Page

#### Images

This section displays all images uploaded by user. If user has not uploaded any images it will display "Sorry, No Images Available." message.

![Images Section](./assets/readme/features/)
![No Images](./assets/readme/features/)

#### Mobile Details

This section displays mobile specifications provided by user

![Images Section](./assets/readme/features/)

#### Seller Details

This section displays Seller details and mobile listed date. There is a link which changes as per 3 different scenarios.

1. If a authenticated user visits his own listing : Browse More Phones (Redirects to Mobiles Page)

![Images Section](./assets/readme/features/)

2. If a authenticated user visits another user's listing : Interested? Contact Us (Triggers mailto response to MobileTrade)

![Images Section](./assets/readme/features/)

3. If a unauthenicated user visits : Interested ? Sign In to Contact Us (Redirects to login page)

![Images Section](./assets/readme/features/)

#### Favourites

This link changes as per 4 different scenarios.

1. If a authenticated user visits his own listing : Edit Mobile Details (Redirects to Edit Mobile details Page)

![Images Section](./assets/readme/features/)

2.1 If a authenticated user visits another user's listing : Add to Favourites (Adds mobile to user's favourites Page)

![Images Section](./assets/readme/features/)

2.2 If mobile is already added to user's favourites list : Remove From Favourites (Removes mobile from user's favourites Page)

![Images Section](./assets/readme/features/)

3. If a unauthenicated user visits : Add to Favourites (Redirects to login page)

![Images Section](./assets/readme/features/)

### Profile

The profile page displays details of the user like Name, Email-id, Profile Picture and 4 different links which are.

1. Edit Profile (redirects to profile editing page)
2. My Listings (redirects to user's listing page)
3. My Favourites (redirects to user's favourites page)
4. Delete Account (redirects to deletion confirmation page)