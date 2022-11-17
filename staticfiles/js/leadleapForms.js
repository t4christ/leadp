const login = document.querySelector('.login');
const lForms = document.querySelector('.login-form');
const forms = document.querySelector('.forms');
const rForms = document.querySelector('.register-form');
const loginPanel = document.querySelector("[data-login-panel]").content.cloneNode(true);
const registerPanel = document.querySelector("[data-register-panel]").content.cloneNode(true);
const rPanel = registerPanel.children[0];
const lPanel = loginPanel.children[0];
const regBtn = loginPanel.children[0].querySelector('a');
const logBtn = registerPanel.children[0].querySelector('a');
const spinner = document.querySelector('.spin');

    lForms.append(lPanel);
    rForms.append(rPanel);

regBtn.onclick = ()=>{
    console.log(forms)
    forms.classList.toggle('spin-box')
}
logBtn.onclick = ()=>{
    console.log(forms)
    forms.classList.toggle('spin-box')
}


