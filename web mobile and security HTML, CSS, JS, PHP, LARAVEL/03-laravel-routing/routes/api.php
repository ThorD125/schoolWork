<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

use App\Http\Controllers\HelloController;

Route::get('/hello', function () {
    return ["message"=>"Hello from Laravel!"];
});


// Route::get("/hello/{yourname}", function($yourname){
//     return ["message" => "Hello " . $yourname];
// });


Route::get("/hello/{yourname}", [HelloController::class, "hello"]);


