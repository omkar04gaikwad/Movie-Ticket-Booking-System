def test_book_seat(client):
    headers = {"Authorization": "Bearer 1"}  # Replace with a valid user_id
    response = client.post(
        "/bookings/",
        headers=headers,
        data={"showtime_id": 1, "seat_number": "A1"}  # Form data
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Seat A1 booked! Payment required."

