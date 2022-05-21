<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HelloController;

class HelloController extends Controller
{
    public function hello($yourname){
        $result = "Hello " . $yourname . "!";
        return ["message" => $result];
    }
}
