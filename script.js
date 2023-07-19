document.getElementById('generate-book').addEventListener('click', function() {
    var numberOfChapters = document.getElementById('number-of-chapters').value;
    var writingStyle = document.getElementById('writing-style').value;
    var prompt = document.getElementById('prompt').value;

    // Perform validation and error handling if needed

    // Make API call to generate the book based on the input values
    // Replace the following code with the actual API call

    // Example API call
    fetch('/generate-book', {
        method: 'POST',
        body: JSON.stringify({
            numberOfChapters: numberOfChapters,
            writingStyle: writingStyle,
            prompt: prompt
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        // Handle the response data and display the generated book
        console.log(data);
    })
    .catch(function(error) {
        // Handle any errors that occur during the API call
        console.error(error);
    });
});
