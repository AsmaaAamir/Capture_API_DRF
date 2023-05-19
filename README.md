# Capture API in DRF 

** Developer: Asma Aamir 

[Live Link](....)

This repository has the Django REST Framework-based API created for the Capture front-end application. This link will take you to the [Live Website](....) and its [repository](....).

## Table of Contents
- [ User Stories](#user-stories)
- [ Database ](#datebase)
- [ Technologies](#tecnologies)
- [ Validation](#validations)
- [Testing](#testing)
- [Credits](#credits)

## User Stories

This is administrative part of the Capture project is the emphasis of the back-end of the project. As a result, there is just one user story.
- As an Admin, I want to be able create, edit and delete the user's posts, comments, and likes so that, I can regulate the user's content and eliminate any potentially offensive stuff.

## Database
I developed the following models for the application to provide structure to the database model:
<img src="">

#### User Model


#### Profile Model

#### Post Model

#### Like Model

#### Comment Model 

#### Follower Model


## Tecnologies

### Languages & Frameworks

The following languages and framework utilised for this repository:
- Python 
- Django 

### Labraries 

- Django 
- Pillow
- Django REST Framework

### Tools
 
- Git was used to upload the source code to GitHub. 
- GitHub was utilised as a remote repository to keep the code for the Capture project.
- Codeanywhere - It serves as a virtual IDE workspace for the Capture website.
- APITestCase - Using the Django Rest Framework, I conducted automated testing.
- Cloudinary was used to store static files 
- PostgreSQL was used to deployed this repository on Render using PostgreSQL database

## Validations

## Testing

I carried out two different type tests for the Capture_API_DRF:
1. Manual testing - of the user stories 
2. Automated testing  

Additionally, only users who are logged in can do these actions on posts or profiles. If a user wants to like, comment on, or follow something on the website, they must first log in.  

| ** Test ** | ** Action ** | ** Expected result ** | ** Actual Result ** |
| -----------| ------------ | --------------------- | ------------------- |
| User | Create user | user can be created | Works as expected|
| User/Admin | Permission |  Permission can be changed | Works as expected |
| Profile | Update & delete user | A profile can be created, edited and deleted | Works as expected |
| Post | Create, update & delete user | A post can be created, edited and deleted | Works as expected |
| Likes | Like & Unlike | Post can be liked and unliked | Work as expected| 
| Commets | Create, update & delete comments | User can  created, edited and deleted comment on post | Works as expected |
| Follow | Follow & Unfollow | User can follow and un follow profile | Work as expected|

<details><summary>Create User</summary>
     <img src="docs/testing/create-user.png">
</details>

<details><summary>Change Permissons</summary>
    <img src="docs/testing/change-permissions.png">
</details>

<details><summary>Profile</summary>
    <details><summary>Change Profile</summary>
        <img src="docs/testing/updating-profile.png"></details>
    <details><summary>Delete Profile</summary>
        <img src="docs/testing/delete-profile.png"></details>
</details>

<details><summary>Post</summary>
    <details><summary>Create Post</summary>
        <img src="docs/testing/testing-creating-post.png"></details>
    <details><summary>Change Post</summary>
        <img src="docs/testing/test-post-update.png"></details>
    <details><summary>Delete Post</summary>
        <img src=""></details>
</details>

<details><summary>Like</summary>
    <details><summary>Like</summary>
        <img src="docs/testing/testing-liking-post.png"></details>
    <details><summary>Unlike</summary>
        <img src="docs/testing/test-unliking-post.png"></details>
</details>

<details><summary>Comment</summary>
  <details><summary>Adding Comment</summary>
    <img src="docs/testing/test-adding-comment.png"></details>
    <details><summary>Removing comment</summary>
    <img src="docs/testing/tets-delteing-comment.png"></details>
</details>

<details><summary>Follow</summary>
    <details><summary>Following</summary>
        <img src="docs/testing/test-following.png"></details>
    <details><summary>Unfollow</summary>
        <img src="docs/testing/test-unfollowing.png"></details>
</details>



## Credits
