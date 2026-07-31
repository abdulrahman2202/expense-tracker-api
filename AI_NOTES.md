# AI_NOTES.md

## 1. Which parts of the code were AI-generated vs. written by you

### AI-assisted
I used ChatGPT to assist with:
- Initial FastAPI project structure.
- Suggested folder organization (`routers`, `services`, `models`, `utils`).
- Initial CRUD endpoint templates.
- Pydantic model suggestions.
- Swagger/OpenAPI documentation improvements.
- Pytest test case templates.
- README structure and documentation.

### Implemented and integrated by me
I implemented and integrated the project by:
- Connecting all routers, services, and utility modules.
- Implementing the complete expense management workflow.
- Writing the business logic for creating, filtering, summarizing, and deleting expenses.
- Configuring JSON file storage.
- Setting up the FastAPI application.
- Running, debugging, and fixing errors during development.
- Writing, running, and verifying all automated tests.
- Implemented an expense search endpoint to search by title and category.

---

## 2. What you validated, tested, or changed in the AI's output, and why

I reviewed, modified, and tested every AI-generated suggestion before integrating it into the project.

The following changes were made:

- Modified the project structure to better separate routers, services, models, and utilities for maintainability.
- Added proper request validation using Pydantic (`Field`, positive amount, required fields, valid date).
- Added response models to improve API documentation and response consistency.
- Changed category filtering to be case-insensitive.
- Improved the summary endpoint to omit the `category` field when not filtering.
- Configured automated tests to use a separate JSON file instead of the production data file.
- Configured appropriate HTTP status codes (201, 404, and 422) to follow REST API conventions.

All endpoints were manually tested through Swagger UI, and the automated test suite was executed successfully before submission.

---

## 3. Any AI suggestion you decided not to use, and why

I chose not to use the following AI suggestions:

- Using PostgreSQL or MongoDB because the assignment specifically requested JSON or in-memory storage.
- Using SQLAlchemy because it was unnecessary for the assignment requirements.
- Adding JWT authentication because user authentication was outside the project scope.

These suggestions were intentionally excluded to keep the implementation aligned with the assignment requirements and focused on the requested functionality.