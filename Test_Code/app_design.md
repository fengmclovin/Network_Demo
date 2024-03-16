### Summary
To fulfil the specified requirements for a social network application using Python (Django), JavaScript, HTML, and CSS, 
I'll need to create various components such as models, views, templates, and front-end logic. 

Below, I'll outline the steps and components needed to implement for each requirement:

### New Post:
Create a form or textarea on a webpage where users can input their new posts.
Implement a Django view to handle the form submission and create a new post in the database.
Use JavaScript to handle form submissions asynchronously (e.g., using the fetch API).

### All Posts:
Create a Django view to fetch all posts from the database and pass them to a template.
Display the posts on the webpage in reverse chronological order using HTML/CSS.
Implement pagination using Django's Paginator class and Bootstrap's Pagination features.

### Profile Page:
Create a Django view to display a user's profile page with their posts, followers count, and the following count.
Implement a "Follow" or "Unfollow" button for other users (excluding the current user).
Use JavaScript to handle follow/unfollow actions asynchronously.

### Following:
Create a Django view to display posts from users that the current user follows.
Implement pagination for the following page similar to the "All Posts" page.

### Edit Post:
Implement an "Edit" button or link for each user's own posts on the profile page or all posts page.
Use JavaScript to toggle between displaying the post content and a textarea for editing.
Handle post editing asynchronously using JavaScript and fetch API.

### Like and Unlike:
Implement a "Like" button or link for each post on the profile page or all posts page.
Use JavaScript to asynchronously update the like count on the server and update the displayed count without reloading the page.

#### Below is a general structure of how you can organize your Django application:

models.py: Define Django models for users, posts, likes, etc.

views.py: Implement Django views for handling HTTP requests and rendering templates.

urls.py: Define URL patterns for different views and actions.

templates/: Create HTML templates for rendering pages.

static/: Store CSS and JavaScript files for frontend styling and functionality.

This is a high-level overview, and I'll dive deeper into each component based on the specific application requirements and design. 

Django's documentation and tutorials can always provide me with more detailed guidance on each aspect of development.
