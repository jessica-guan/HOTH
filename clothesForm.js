// add to the donation form html 
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('clothesForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting traditionally

        // Collect form data
        const formData = new FormData(event.target);

        // Assign value 0 if checkbox is not checked, otherwise assign value 1
        const thriftedCheckbox = document.getElementById('thrifted');
        formData.set('thrifted', thriftedCheckbox.checked ? '1' : '0');

        // Send data to Flask server
        fetch('http://127.0.0.1:5000/clothes', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Do something with the response if needed
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});