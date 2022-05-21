<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Booking;

class BookingController extends Controller
{
    function all(Request $request)
    {
        // $bookings = Booking::createBooking();
        // return ["data" => $bookings];

        $booking = new Booking();

        // $booking->name = $request->name;
        // $booking->email = $request->email;

        $booking->from_airport_id = $request->input("from_airport_id");
        $booking->to_airport_id = $request->input("to_airport_id");
        $booking->date = $request->input("date");
        $booking->lastname = $request->input("lastname");
        $booking->firstname = $request->input("firstname");
        $booking->email = $request->input("email");

        $booking->save();

        return $booking;
    }
}


// {
//     "from_airport_id": "123456",
//     "to_airport_id": "456789",
//     "date": "2022-03-09 21:42:43",
//     "lastname": "testlastname",
//     "firstname": "testfirstnam",
//     "email": "testemail@test.com"
// }