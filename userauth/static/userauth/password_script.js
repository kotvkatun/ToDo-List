function passwordHider1() {
  var pswd1 = document.getElementById("pswd1");
  if (pswd1.type === "password") {
    pswd1.type = "text";
  } else {
    pswd1.type = "password";
  }
} 

 
function passwordHider2() {
  var pswd1 = document.getElementById("id_password");
  var pswd2 = document.getElementById("confirm_password");
  if (pswd1.type === "password" && pswd2.type === "password") {
    pswd1.type = "text";
    pswd2.type = "text";
  } else {
    pswd1.type = "password";
    pswd2.type = "password";
  }
}

 

function check() {
  var password = document.getElementById('id_password')
  var confirm_password = document.getElementById('confirm_password')
  var message = document.getElementById('message')
  var register_submit = document.getElementById('register_submit')
  if (password.value === confirm_password.value && password.value !== "") {
    message.style.color = 'green';
    message.innerHTML = 'Passwords match! ☑️';
    register_submit.disabled = false;
  } else {
    message.style.color = 'red';
    message.innerHTML = 'Passwords don\'t match! ❌';
    register_submit.disabled = true;
  }
}
