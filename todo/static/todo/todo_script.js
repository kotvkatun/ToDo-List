// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("li");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function () {
    var div = this.parentElement;
    div.remove();
  }
}

// Add a "checked" symbol when clicking on a list item
var form = document.querySelector('ul');
form.addEventListener('click', function (ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);


// Create a new list item when clicking on the "Add" button
function newElement() {
  var formList = document.getElementById("formList")
  var listElement = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  listElement.innerHTML = inputValue;
  formList.appendChild(listElement);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("formList").prepend(listElement);
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  listElement.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      var div = this.parentElement;
      div.remove();
    }
  }
}


//Helper function for evaluating if a list item is checked or not
function isChecked(liItem) {
  if (liItem.className.includes("checked")) {
    return true
  } else {
    return false
  }
}

// Prepare a JSON string with list items
function send() {
  var resultJSON = {};
  var listValues = document.getElementsByTagName("li");
  if (listValues.length === 0) {
    alert("Can't save an empty list!")
  } else {
    for (i = 0; i < listValues.length; i++) {
      var taskObject = "task" + i.toString()
      var taskText = listValues.item(i).innerHTML
      var check = isChecked(listValues.item(i))
      resultJSON = {...resultJSON, [taskObject]: {task: taskText, checked: check}}
    }
    var JSONInput = document.getElementById("JSONInput")
    JSONInput.name = "TodoJSON"
    JSONInput.value = JSON.stringify(resultJSON)
  }
}

