$(document).ready(function() {
  // Smooth scroll to the About Us section
  $("#scrollToAbout").on("click", function(event) {
    event.preventDefault();
    $("html, body").animate(
      {
        scrollTop: $("#about").offset().top
      },
      800 // Adjust the scrolling speed here (in milliseconds)
    );
  });
});


$(document).on('scroll', function () {
    console.log('scrolled')

    var $nav = $(".navbar-custom");
    $nav.toggleClass('scrolled', $(this).scrollTop() > 1);
});

var navDiv = document.getElementById("navdiv");
var navbarDiv = navDiv.querySelector('.main-nav');
navDiv.addEventListener("mouseover", showMenu, false);
navDiv.addEventListener("mouseleave", hideMenu, false);

var menuDiv;
var mobileBreakpoint = window.matchMedia("(max-width: 768px)");

mobileMenuDiv = document.getElementById("mobile-menu-content");
desktopMenuDiv = document.getElementById("menu-content");
function updateMenuDiv() {
  if (mobileBreakpoint.matches) {
    desktopMenuDiv.style.display = "none"
    menuDiv = mobileMenuDiv
  } else {
    mobileMenuDiv.style.display = "none"
    menuDiv = desktopMenuDiv
  }
}

updateMenuDiv();
mobileBreakpoint.addEventListener("change", updateMenuDiv);

menuDiv.addEventListener("mouseout", hideMenu, false);

var menuIcon = document.getElementById("nav-left-item");
var index = navDiv.getAttribute("data-index") === "True";

// function setNavDivToImage() {
//   navDiv.style.backgroundImage = "url('/static/img/header/lighthouse.png')";
//   navDiv.style.backgroundSize = "cover";
//   navDiv.style.backgroundPosition = "center";
// }

// if (!index) {
//   setNavDivToImage()
// }

function showMenu() {
    var translucent_green = "rgba(119, 144, 113, .9)";
    var menuContentRowDiv = menuDiv.querySelector('.row');
    
    // console.log(index)
    if (index) {
      navbarDiv.style.backgroundColor = translucent_green;
      if (menuContentRowDiv){
        menuContentRowDiv.style.backgroundColor = translucent_green;
      }
    } else {
      if (menuContentRowDiv){
        menuContentRowDiv.style.backgroundColor = "rgb(119, 144, 113)";
      }
    }



    menuDiv.style.display = "block";  
    $('#sandwich-button').removeClass('fa-bars').addClass('fa-xmark');
}


function hideMenu() {
    menuDiv.style.display = "none";
    if (index) {
      navbarDiv.style.backgroundColor = null;
    } 
    $('#sandwich-button').removeClass('fa-xmark').addClass('fa-bars'); 
}

document.getElementById("vcard-link").addEventListener("click", function() {
  var person = {
    name: document.getElementById("name").textContent,
    title: document.getElementById("title").textContent,
    tel: document.getElementById("tel").textContent,
    email: document.getElementById("email").textContent
  };

  var vCardData = [
    "BEGIN:VCARD",
    "VERSION:3.0",
    "N:" + person.name,
    "TITLE:" + person.title,
    "TEL:" + person.tel,
    "EMAIL:" + person.email,
    "END:VCARD"
  ].join("\n");

  var blob = new Blob([vCardData], { type: "text/vcard;charset=utf-8" });
  var url = URL.createObjectURL(blob);

  var link = document.createElement("a");
  link.href = url;
  link.download = person.name + ".vcf";
  link.click();

  URL.revokeObjectURL(url);
});