document.addEventListener("DOMContentLoaded", function () {
    const movieForm = document.getElementById("movie-form");
    const reviewerImages = document.querySelectorAll(".reviewer-image");
    const generatedReview = document.getElementById("generated-review");

    movieForm.addEventListener("submit", function (event) {
        event.preventDefault();
        generatedReview.textContent = ""; // Clear the previous review
    });

    reviewerImages.forEach(function (image) {
        image.addEventListener("click", function () {
            const reviewerName = image.getAttribute("data-reviewer");
            const movieTitle = document.getElementById("movie-input").value;

            if (!movieTitle) {
                alert("Please enter a movie title before clicking on a reviewer.");
                return;
            }

            fetchReview(reviewerName, movieTitle);
        });
    });

    async function fetchReview(reviewerName, movieTitle) {
        const response = await fetch("/generate_review", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                reviewer_name: reviewerName,
                movie_title: movieTitle,
            }),
        });

        if (response.ok) {
            const data = await response.json();
            generatedReview.textContent = `${reviewerName}'s generated review: ${data.review}`;
        } else {
            alert("Error: Failed to generate the review.");
        }
    }
});
