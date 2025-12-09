🚀 User Authentication API (FastAPI + SQLModel + JWT)

A clean, minimal, production-ready backend for user authentication, built using:

FastAPI

SQLModel

SQLite

JWT Authentication

Password hashing with bcrypt

Fully protected routes

Clean folder structure

Validations + error handling

This project was built as part of a backend learning roadmap.
It focuses on core fundamentals: routing, CRUD, middleware, security, hashing, JWT, and auth protection.

📌 Features
✅ User CRUD

Create User

Get User by ID

List Users

Update User (partial updates supported)

Delete User

✅ Authentication

Login with email + password

Password hashing using passlib[bcrypt]

JWT generation

JWT verification & decoding

Token expiry support

✅ Protected Routes

/auth/me → Returns the logged-in user

Any route can be protected using Depends(current_user)

✅ Middleware

Request logging (method, path, response time)

Global exception handler for uncaught errors

🗂 Project Structure
app/
│
├── core/
│   ├── config.py          # SECRET_KEY, ALGORITHM, token expiry
│   ├── jwt.py             # create + verify token helpers
│   └── security.py        # password hashing + verification
│
├── db/
│   ├── database.py        # DB engine + session provider
│   ├── models.py          # SQLModel User model (DB)
│   └── crud.py            # Create, Read, Update, Delete logic
│
├── routers/
│   ├── users.py           # User CRUD routes
│   └── auth.py            # Login + /me route
│
├── schemas/
│   └── user.py            # Pydantic schemas (UserCreate, UserRead, UserUpdate)
│
└── main.py                # App initialization, middleware, router mounting

⚙️ Installation
1️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the server
uvicorn app.main:app --reload


Server runs at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

🔐 Authentication Flow
1. Login

Send a POST request to:

POST /auth/login


Query Params:

email=your_email
password=your_password


Response:

    {
      "access_token": "your.jwt.token",
      "token_type": "bearer"
    }

2. Access Protected Routes

Include the token as:

Authorization: Bearer <your_token>


Example protected route:

GET /auth/me


Returns the authenticated user's data.

🛡 Security

Passwords are hashed using bcrypt

Tokens follow HS256 JWT standard

Expired or invalid tokens trigger 401 responses

Backend performs strict input validation (never trusts frontend)

🧪 Testing Endpoints

Use:

Swagger UI → Quick testing

Postman → For manual header/token testing

cURL (optional)

Example login via Postman:

POST /auth/login?email=test@gmail.com&password=abcdef


Example authenticated request:

Headers:

Authorization: Bearer eyJhbGciOiJI...

🚀 Deployment (Render)

This project is fully deployed on Render Web Services using:

Build Command:

pip install -r requirements.txt


Start Command:

uvicorn app.main:app --host 0.0.0.0 --port 10000


SQLite file (app.db) is created automatically in Render's disk.

📄 License

This project is open-source.
Use it, improve it, break it, rebuild it — do whatever helps you grow.

🙌 Author

Built by Rito, grinding backend development with discipline, debugging skills, and actual understanding — not tutorial-copy nonsense.
