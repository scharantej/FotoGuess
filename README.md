## Design for "Guess Who" Web Application

### HTML Files

- **index.html**: The main page of the application where users can select their opponents, view their friend lists, and start the game.
- **game.html**: The gameplay page where users can view each other's friend lists, crop and upload photos, ask questions about the other player's characters, and receive hints.

### Routes

- **main_page**: The route for the main page (`index.html`). It handles user interactions, such as selecting opponents and starting the game.
  
- **game_page**: The route for the gameplay page (`game.html`). It facilitates the game logic, including asking questions, receiving hints, and keeping score. 

- **upload_photo**: The route for uploading cropped photos. It handles the file upload and storage process. Other routes can reference this route to access uploaded photos.

- **get_hints**: The route for retrieving hints from the server. Other routes can reference this route to display hints to users.

- **submit_answer**: The route for submitting user answers. It updates the game state, such as eliminating characters based on the guesses.

- **check_winner**: The route for checking if there is a winner. Other routes can reference this route to determine when the game ends.