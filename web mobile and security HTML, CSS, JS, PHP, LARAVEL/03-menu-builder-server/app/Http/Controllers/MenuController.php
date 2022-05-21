<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MenuController extends Controller
{
    
    function random()
    {
        $dishes = [ "beef", "chicken", "cod", "couscous", "eggrolls", "gazpacho", "kebab",
		"linguine", "meatballs", "pork", "quesadillas", "salad", "salmon", "sandwich",
		"shrimp", "soup", "stirfry", "tacos", "zucchini" ];

        $number1 = rand(0, count($dishes) - 1);
        
        $number2 = rand(0, count($dishes) - 1);

        while ($number1 == $number2) {
            $number2 = rand(0, count($dishes) - 1);
        }

        $starter = $dishes[$number1];
        $main = $dishes[$number2];
        $dessert = "icecream";

        return ["menu" => [ "starter" => $starter, "main" => $main, "dessert" => $dessert  ]];
    }
}
