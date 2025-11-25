from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# List of categories - Ocean themed
categories = [
    [1, "Marine Biology"],
    [2, "Ocean Exploration"],
    [3, "Marine Conservation"],
    [4, "Oceanography"],
]

# List of books - Ocean themed
# Format: [bookId, categoryId, title, author, isbn, price, image, readNow]
books = [
    # Marine Biology (categoryId = 1)
    [1, 1, "The Soul of an Octopus", "Sy Montgomery", "978-1451697711", 17.99, "octopus.jpg", 1],
    [2, 1, "The World Is Blue", "Sylvia Earle", "978-1426205729", 16.99, "world-blue.jpg", 0],
    [3, 1, "Spineless: The Science of Jellyfish", "Juli Berwald", "978-0735220959", 18.99, "jellyfish.jpg", 1],
    [4, 1, "The Log from the Sea of Cortez", "John Steinbeck", "978-0140187441", 14.99, "cortez.jpg", 1],
    
    # Ocean Exploration (categoryId = 2)
    [5, 2, "The Silent World", "Jacques Cousteau", "978-1426220098", 19.99, "silent-world.jpg", 1],
    [6, 2, "Deep: Freediving, Renegade Science", "James Nestor", "978-0544484351", 16.99, "deep.jpg", 0],
    [7, 2, "Shadow Divers", "Robert Kurson", "978-0375760990", 17.99, "shadow-divers.jpg", 1],
    [8, 2, "The Underworld: Journeys to the Depths", "Susan Casey", "978-0385545556", 28.99, "underworld.jpg", 0],
    
    # Marine Conservation (categoryId = 3)
    [9, 3, "The Outlaw Ocean", "Ian Urbina", "978-0525533221", 18.99, "outlaw-ocean.jpg", 1],
    [10, 3, "Blue Mind", "Wallace J. Nichols", "978-0316252119", 16.99, "blue-mind.jpg", 0],
    [11, 3, "Sea Change: A Message of the Oceans", "Sylvia Earle", "978-0449906736", 15.99, "sea-change.jpg", 1],
    [12, 3, "The Death and Life of Monterey Bay", "Stephen Palumbi", "978-1577171255", 19.99, "monterey-bay.jpg", 1],
    
    # Oceanography (categoryId = 4)
    [13, 4, "The World Ocean", "David Ross", "978-1616100827", 45.99, "world-ocean.jpg", 0],
    [14, 4, "Introduction to Physical Oceanography", "Robert Stewart", "978-0691169811", 89.99, "physical-ocean.jpg", 1],
    [15, 4, "Oceanography: An Invitation to Marine Science", "Tom Garrison", "978-1305105164", 125.99, "invitation-ocean.jpg", 0],
    [16, 4, "The Extreme Life of the Sea", "Stephen Palumbi", "978-0691169811", 22.99, "extreme-life.jpg", 1],
]


# set up routes
@app.route('/')
def home():
    """Homepage - displays welcome text and category selections"""
    return render_template("index.html", categories=categories)


@app.route('/category')
def category():
    """Category page - displays books for a selected category"""
    # Store the categoryId passed as a URL parameter into a variable
    category_id = request.args.get("categoryId", type=int)
    
    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [b for b in books if b[1] == category_id]
    
    # Link to the category page. Pass the selectedCategory, categories and books as parameters
    return render_template(
        "category.html",
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )


@app.route('/search', methods=['GET', 'POST'])
def search():
    """Search results page - to be implemented in Part 2"""
    return render_template('error.html', error="Search functionality coming in Part 2!")


@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)