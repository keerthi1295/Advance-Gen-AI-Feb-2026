🎬 Movie Booking API

This is a simple Movie Ticket Booking API built using FastAPI and Python.

🚀 Features
View all movies
Search and filter movies
Sort and paginate movies
Book movie tickets
Apply promo codes (SAVE10, SAVE20)
Hold and confirm seats
Add, update, delete movies

▶️ How to Run
1. Install requirements:
pip install fastapi uvicorn

2. Run the server:
uvicorn main:app --reload

3. Open in browser:
http://127.0.0.1:8000/docs

📌 Main APIs
1. Movies
GET /movies → Get all movies
GET /movies/{id} → Get movie by ID
GET /movies/search → Search movies
GET /movies/filter → Filter movies

2. Bookings
POST /bookings → Book tickets
GET /bookings → View bookings

3. Seat Hold
POST /seat-hold → Hold seats
POST /seat-confirm/{id} → Confirm hold
DELETE /seat-release/{id} → Release hold

🎟️ Example Booking
{
  "customer_name": "John",
  "movie_id": 1,
  "seats": 2,
  "phone": "9876543210",
  "seat_type": "premium",
  "promo_code": "SAVE10"
}

📌 Notes
Max 10 seats per booking
Promo codes: SAVE10, SAVE20
Cannot delete movies with bookings

👨‍💻 Author
Your Name
