document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = {};

    formData.forEach((value, key) => {
        data[key] = parseInt(value, 10);
    });

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.GradeClass) {
            document.getElementById('result').innerText = `Predicted Grade Class: ${result.GradeClass}`;
        } else {
            document.getElementById('result').innerText = `Error: ${result.error}`;
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = `Error: ${error.message}`;
    });
});
