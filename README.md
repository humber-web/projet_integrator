# Project Integrator

## Description
This project integrates multiple services using Docker:
- **Django** web service (`web`)
- **Postgres** database (`db`)
- **Email service** (`email_service`)
- **Micro integrator** (`micro_integrator`)

## Technologies Used
- Python (Django)
- Postgres 15
- Node.js (Email service, if applicable)
- Docker & Docker Compose
- Git & GitHub
- AWS (Lambda, API Gateway)

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:humber-web/projet_integrator.git
   cd projet_integrator
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the project root with the necessary settings:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

3. **Deploy with Docker Compose**:
   ```bash
   docker-compose pull
   docker-compose up -d
   ```

## Project Flow

1. **Order Submission**:  
   The micro integrator exposes an API endpoint at `/pedidos` which receives new orders via a POST request.

2. **Logging & Order Submission**:  
   The incoming order payload is logged, and the micro integrator calls the Django backend to save the order.

3. **Extracting Order Details**:  
   After receiving the backend response, key properties such as order id, email, value, type, company name, and description are extracted using a JavaScript mediator.

4. **AWS Lambda Validation**:  
   The extracted order details are formatted into a payload and sent to an AWS Lambda API for order validation. The Lambda response is then parsed.

5. **Decision & Notification**:  
   - If the response indicates **AUTO** approval:
     - The order status is updated via a PUT call back to the Django backend.
     - An email notification is sent via the Email service.
   - Otherwise, a manual approval flow is triggered and an appropriate notification email is sent.

6. **Response Delivery**:  
   Finally, the micro integrator completes the flow and returns a response to the client.

## Access the Services

- **Django App**: Open your browser and navigate to [http://localhost:8000](http://localhost:8000) to access the Django web application.
- **Email Service**: Access the email service at [http://localhost:3000](http://localhost:3000) to view its interface.
- **Micro Integrator**: Check your Docker Compose configuration for the port mappings, then access the service via the appropriate URL (e.g., [http://localhost:8290](http://localhost:8290) if that port is used).


## Contributing

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push the branch.
4. Open a Pull Request for review.

## License


This project is licensed under the [MIT License](LICENSE.md).  
For more details, see the [MIT License](https://opensource.org/licenses/MIT).
