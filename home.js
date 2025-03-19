// validation.js

document.getElementById('wsignup').addEventListener('submit', function (event) {
    var ownername = document.getElementById('ownername').value;
    var wgender = document.querySelector('input[name="wgender"]:checked');
    var wemail = document.getElementById('wemail').value;
    var wdob = document.getElementById('wdob').value;
    var wphno = document.getElementById('wphno').value;
    var wphoto = document.getElementById('wphoto').value;
    var shopname = document.getElementById('shopname').value;
    var licence = document.getElementById('licence').value;
    var shopimage = document.getElementById('shopimage').value;
    var aadhaar = document.getElementById('aadhaar').value;
    var wdoor = document.getElementById('wdoor').value;
    var wstreet = document.getElementById('wstreet').value;
    var wcity = document.getElementById('wcity').value;
    var wdistrict = document.getElementById('wdistrict').value;
    var wstate = document.getElementById('wstate').value;
    var wpincode = document.getElementById('wpincode').value;

    // Basic validation
    if (!ownername || !wgender || !wemail || !wdob || !wphno || !wphoto ||
        !shopname || !licence || !shopimage || !aadhaar || !wdoor || !wstreet ||
        !wcity || !wdistrict || !wstate || !wpincode) {
        alert("Please fill in all required fields.");
        event.preventDefault();
        return false;
    }

    // Validate email format
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(wemail)) {
        alert("Please enter a valid email address.");
        event.preventDefault();
        return false;
    }

    // Validate phone number (10 digits)
    var phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(wphno)) {
        alert("Please enter a valid 10-digit phone number.");
        event.preventDefault();
        return false;
    }

    // Validate pincode (6 digits)
    var pincodeRegex = /^\d{6}$/;
    if (!pincodeRegex.test(wpincode)) {
        alert("Please enter a valid 6-digit pincode.");
        event.preventDefault();
        return false;
    }

    // You can add more specific validations based on your requirements

    return true; // Submit the form if all validations pass
});
