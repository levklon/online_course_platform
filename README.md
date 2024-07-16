# Online Course Platform

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-3.2%2B-green)
![React](https://img.shields.io/badge/React-17%2B-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange)
![Docker](https://img.shields.io/badge/Docker-19.03%2B-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow)
![Node.js](https://img.shields.io/badge/Node.js-14%2B-green)
![Vercel](https://img.shields.io/badge/Vercel-Production-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Description

The Online Course Platform is a comprehensive solution for creating, managing, and participating in online courses. Designed with a modern architecture, this platform offers a seamless experience for both instructors and students. Users can register, purchase courses, view video lessons, and engage in real-time communication through chat. The platform integrates Stripe for secure payment processing and WebSocket for real-time notifications and chat functionality.
 
## Technologies
  
- **Frontend**: React
- **Backend**: Django
- **Database**: MySQL
- **Docker**: For application containerization
- **Additional**:
  - WebSocket for real-time features (chat and notifications)
  - Stripe for payment processing

## Features

- **User Authentication**: Secure registration and login functionality.
- **Course Management**: Instructors can create, edit, and delete courses.
- **Video Lessons**: Students can watch video lessons associated with each course.
- **Real-time Chat**: Students can interact with each other and instructors in real-time.
- **Payment Processing**: Secure course purchase using Stripe.

## Installation and Setup

### Prerequisites

- Python 3.8+
- Node.js 14+
- Docker and Docker Compose

### Local Installation

1. **Clone the repository:**
   
   ```sh
   git clone https://github.com/levklon/online_course_platform.git

2. **Navigate to the project directory:**
   
   ```sh
   cd online_course_platform

3. **Install dependencies:**
   
- For backend:
  
   ```sh
  pip install -r requirements.txt

- For frontend:
  
  ```sh
  npm install --prefix frontend

4. **Set up environment variables:**
- Create a .env file in the backend directory and add the necessary environment variables:
  
  ```sh
  SECRET_KEY=your_secret_key
  DEBUG=True
  DB_NAME=yourdatabase
  DB_USER=youruser
  DB_PASSWORD=yourpassword
  DB_HOST=db
  DB_PORT=3306
  STRIPE_SECRET_KEY=your_stripe_secret_key

## Docker Installation

1. **Build and run Docker Compose:**
   
   ```sh
   docker-compose up --build

2. **Check Docker containers:**

- Ensure that the containers are running correctly:
  
   ```sh
   docker ps
   
3. **Apply database migrations:**

- Run the following command inside the web container to apply Django migrations:
  
   ```sh
   docker-compose exec web python manage.py migrate

4. **Create a superuser:**

- If you need to access the Django admin interface, create a superuser:

  ```sh
  docker-compose exec web python manage.py createsuperuser

5. **Collect static files:**

- Collect static files for Django:

  ```sh
  docker-compose exec web python manage.py collectstatic --noinput
  
## Usage

### Running the Application

1. **Start the backend server:**

   ```sh
   python backend/manage.py runserver
   
2. **Start the frontend server:**

   ```sh
   npm start --prefix frontend

## Deployment

### Deployment on Vercel

1. **Install Vercel CLI:**

   ```sh
   npm install -g vercel

2. **Navigate to the frontend directory:**

   ```sh
   cd frontend

3. **Deploy the application:**

   ```sh
   vercel

### Production Setup

- Environment Variables: Ensure all environment variables are set correctly for production.
- Security: Implement security measures such as HTTPS, secure cookies, and CSRF protection.
- Performance: Optimize performance by enabling caching and using a content delivery network (CDN).

## Contributing

I am welcome contributions! Please follow these steps:

1. **Fork the repository.**
   
2. **Create a new branch:**
   
   ```sh
   git checkout -b feature-branch

3. **Make your changes and commit them:**

   ```sh
   git commit -m 'Add some feature'

4. **Push to the branch:**

   ```sh
   git push origin feature-branch

5. **Create a pull request.**


## License

This project is licensed under the MIT License - see the [LICENSE] file for details.
