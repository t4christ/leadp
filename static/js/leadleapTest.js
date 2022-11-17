const questionsContainer = document.querySelector('.test-question .questions')
const questions = questionsContainer.querySelectorAll('.question') 
const counterCheck = document.querySelector('#counter')



let clicked = false
let counter = 0

questions.forEach(question =>{
    question.addEventListener('click', (event)=>{
        const victim = event.target
        const options = question.querySelectorAll('.options .option .circle')
        if(victim.className == 'circle'){
            let clickedCheck = 0
            for(let i = 0; i < options.length; i++){
                if(options[i].classList.contains('active')){
                    options[i].classList.remove('active')
                }
            }
            clickedCheck++
            console.log(clickedCheck)
            victim.classList.add('active')
            counter++
        }
            
            counterCheck.innerHTML ="Question Answered: " + counter

            if(counter == questions.length){
                document.querySelector('.completed').innerHTML = "Completed"
            }
    })
    
})
