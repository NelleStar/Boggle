// collect the elements needed 
const startButton = document.getElementById('start-button');
const startScreen = document.getElementById('start-screen');
const boardContainer = document.getElementById('board-container');
const timerDisplay = document.getElementById('timer');

// set up variables for timer and remaining time
let timer;
let remainingTime = 180;

// start time function
function startTimer() {
    console.log('start timer clicked')
    // first clear timer if needed
    if (timer) {
        clearInterval(timer);
    }

    // set timer to 
    timer = setInterval(updateTimer, 1000);
    updateTimer();
}

// function to update the timer as needed to be called in the startTimer function
function updateTimer() {
    if (remainingTime > 0) {
        remainingTime --;
        timerDisplay.textContent = `Time Remaining: ${remainingTime} seconds`;
    } else {
        clearInterval(timer);
        timerDisplay.textContent = 'Time is up!'
        const wordInput = document.getElementById("word");
        const submitButton = document.getElementById("submit-button");
        wordInput.disabled = true;
        submitButton.disabled = true;
    }
}

startButton.addEventListener('click', startTimer);

// ------------------------------------------------------ //
let totalPoints = 0;

async function checkWord (event) {
    event.preventDefault();
    const word = document.getElementById("word").value;

    const resp = await axios.get('/check-word', {params : { word : word }});
    console.log(resp)

    // Update the result on the screen
    const resultDisplay = document.getElementById("result");
    if (resp.data.result.valid_word_result === "ok") {
      // If the word is valid, display the points earned for the word
      totalPoints += word.length;
      resultDisplay.textContent = `Points: ${totalPoints}`;
    } else {
      // If the word is not valid, display an appropriate message
      resultDisplay.textContent = `Invalid word: ${resp.data.result.valid_word_result}`;
    }

    document.getElementById("word").value = "";
}


const form = document.getElementById("word-form");
form.addEventListener("submit", checkWord)

