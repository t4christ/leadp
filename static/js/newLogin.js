const loginLink = document.querySelector("#login")
const registerLink = document.querySelector('#register')
const registerForm = document.querySelector('.form-register')
const loginForm = document.querySelector('.form-login')


loginLink.addEventListener('click', ()=>{
    loginForm.classList.add('effects')
    registerForm.classList.add('effect')
})

registerLink.addEventListener('click', ()=>{
    loginForm.classList.remove('effects')
    loginForm.classList.add('affects')
    registerForm.classList.remove('effect')
    registerForm.classList.add('affect')
})

