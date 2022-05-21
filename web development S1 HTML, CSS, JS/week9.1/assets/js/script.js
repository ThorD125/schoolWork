"use strict";

document.addEventListener("DOMContentLoaded", function() {
    console.log("Loaded");
    
    
    
    let nIntervalId;
    
    document.querySelector(".animate").addEventListener("click", 
    
    function(e) {
        e.preventDefault();
        if (!nIntervalId) {
            nIntervalId = setInterval(function () {
                let lights = document.querySelectorAll('.lights');
                for (let i = 0;i < 3;i++){
                    if (lights[i].classList.contains('active')) {
                        lights[i].classList.remove('active');
                        if (i < 2){
                            lights[i + 1].classList.add('active');
                        }
                        else {
                            lights[0].classList.add('active');
                        }
                        break;
                    }
                }
            }, 1000);
            e.target.innerHTML = "stop animation";
        }
        else {
            clearInterval(nIntervalId);
            nIntervalId = null;
            e.target.innerHTML = "start animation";
        }
    }
    
    
    );
    
    
    
    
    
    
    
    
    document.querySelectorAll(".inventory>figure figcaption a").forEach(function(e){
        
        e.addEventListener("click",function magic(e){
            e.preventDefault();
            
            
            let selector = e.target.parentNode.parentNode.classList[0];
            let splitted =  "." + selector.split("-")[0];
            // document.querySelector(splitted).style.top = "0";
            
            
            document.querySelector(splitted).classList.add(selector);
            
            e.disabled = true;
            
            setTimeout(function(){
                e.target.remove();
            }, 0.00001);
            document.querySelector(splitted).querySelector("svg").innerHTML = e.target.parentNode.parentNode.querySelector("svg").innerHTML
        });
    });
    
    
    
    
    
    
    
    
    
    
    document.querySelectorAll(".moods>li>a").forEach(function(e){
        
        e.addEventListener("click",function(e){
            
            let color = e.target.getAttribute("data-colour");
            document.querySelector(".head .st0").style.fill = color;
            document.querySelector(".head .st1").style.fill = color;
            document.querySelector(".head .st4").style.fill = color;
            let score = e.target.getAttribute("data-score");
            let scoreCount = document.querySelector("main aside p");
            let fixstring = parseInt(scoreCount.innerHTML) + parseInt(score);
            scoreCount.innerHTML = fixstring.toString();
        });
    });
});