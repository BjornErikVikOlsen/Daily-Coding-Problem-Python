

const getUserChoice = (userInput) => {
  userInput = userInput.toLowerCase();
  
  if(userInput === 'rock' || userInput === 'paper' || userInput === 'scissors'){
    return userInput;
  }
  else{
    console.log('Wrong input');
  }
}

function getComputerChoice(){
  num = Math.floor(Math.random() * 3);
  switch(num){
    case 0:
      return 'rock';
        break;
    case 1:
      return 'paper';
      break;
    case 2:
      return 'scissor';
      break;
  }
}

function determineWinner(userChoice, computerChoice){
  if(userChoice === computerChoice){
    return 'tie';
  }
  if(userChoice === 'rock'){
    if(computerChoice === 'paper'){
      return 'computer won';
    }
    else{
      return 'user won';
    }
  }
  if(userChoice === 'paper'){
    if (computerChoice === 'scissors'){
        return 'computer won';
        }
    else{
      return 'user won';
    }
  }
  if(userChoice === 'scissors'){
    if(computerChoice === 'rock'){
      return 'computer won';
    }
    else{
      return 'computer won';
    }
  }
}

function playGame(){
  let userChoice = getUserChoice('scissors');
  let computerChoice = getComputerChoice();
  console.log(userChoice, computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
}
playGame();