document.addEventListener('DOMContentLoaded', function() {

    // Send GET request to the URL
    fetch(`edit/{username}/`)

    // Put response into jason form
    .then(response => response.jason())
    .then(data => {

        // Log data into the consol
        console.log(data)
    })
})