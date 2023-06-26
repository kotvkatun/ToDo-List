function passwordHider1() {
  var pswd1 = document.getElementById("pswd1");
  if (pswd1.type === "password") {
    pswd1.type = "text";
  } else {
    pswd1.type = "password";
  }
} 


function passwordHider2() {
    var pswd1 = document.getElementById("pswd1");
    var pswd2 = document.getElementById("pswd2");
    if (pswd1.type === "password" && pswd2.type === "password") {
      pswd1.type = "text";
      pswd2.type = "text";
    } else {
      pswd1.type = "password";
      pswd2.type = "password";
    }
  } 