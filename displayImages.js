document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from the server
    fetch('http://127.0.0.1:5000/clothes')
    .then(response => response.json())
    .then(data => {
        // Loop through the data returned by the server
        data.forEach(clothes => {
            // Create an image element for each image URL
            const imgElement = document.createElement('img');
            imgElement.src = clothes.image_url;
            
            // Append the image element to a container in your HTML (e.g., with id 'imageContainer')
            document.getElementById('imageContainer').appendChild(imgElement);
        });
    })
    .catch(error => {
        console.error('Error fetching clothes data:', error);
    });
});