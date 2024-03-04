document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('clothesForm').addEventListener('submit', function(event) {
        console.log('DOM content loaded'); // Print a message indicating that the DOM content has been loaded

        event.preventDefault(); // Prevent the form from submitting traditionally

        // Collect form data
        const formData = new FormData(event.target);

        // Convert form data to JSON object
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        // Assign value 0 if checkbox is not checked, otherwise assign value 1
        const thriftedCheckbox = document.getElementById('thrifted');
        jsonData['thrifted'] = thriftedCheckbox.checked ? '1' : '0';

        // Send data to Flask server
        fetch('http://127.0.0.1:5000/clothes', {
            method: 'POST',
            body: JSON.stringify(jsonData),
            headers: {
                'Content-Type': 'application/json'
            }
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