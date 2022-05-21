<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Airport;


class AirController extends Controller
{

    function all()
    {
        $airports = Airport::all();
        return ["airports" => $airports];
    }
}
