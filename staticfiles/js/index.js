const bar = document.querySelector('.bar');
const nav = document.querySelector('.nav-links');
const navCtrl = document.querySelector('.nav-ctrl');
const buttonCtrl = document.querySelector('.button-ctrl');


window.addEventListener('click', (e) => {
    if(e.target.className == "bar" || e.target.className == "button-ctrl"){
        return
    }
        nav.classList.remove('disp')
        navCtrl.classList.remove('show-nav-ctrl')
})

bar.addEventListener('click', (e) => {
    // const targ = e.target

    if((navCtrl.classList.contains('show-nav-ctrl'))){
        navCtrl.classList.remove('show-nav-ctrl');
        nav.classList.toggle('disp'); 
    }else{
        
        nav.classList.toggle('disp'); 
    }
});

buttonCtrl.addEventListener('click', () => {

    if((nav.classList.contains('disp'))){
        nav.classList.remove('disp');
        navCtrl.classList.toggle('show-nav-ctrl'); 
    }else{
        
        navCtrl.classList.toggle('show-nav-ctrl'); 
    }
});

const more = document.querySelector(".who-link a");
const whoResource = document.querySelector(".who-resource");

more.addEventListener("click", ()=> {
    whoResource.classList.toggle('resource-show')
});

// const satisfiedLogo = document.querySelector(".satisfied-logo");
// let total = -77.6;

// setInterval(()=>{
//     if(total >= -1076){
//         satisfiedLogo.style.marginLeft = total + "px";
//         total += total;
//     }else{
//         total = -77.6
//     }
// }, 2000);

const buttonUp = document.querySelector('.btn-up')
const buttonDown = document.querySelector('.btn-down')
const gallery = document.querySelector('.gallery')
const image = gallery.querySelectorAll('img')

let imageSize = image[0].clientHeight
let check = {value:imageSize}


buttonUp.addEventListener('click', ()=>{

    let negCheck = -check.value + "px"
    // console.log(negCheck)
    if(negCheck == -(gallery.clientHeight - (imageSize * 2)) + "px"){
        return
    }else{
        gallery.style.transform = `translateY(${negCheck})`
        check.value += imageSize
    }
});

buttonDown.addEventListener('click', ()=>{
    let posCheck = (imageSize * 2) - (check.value)
    let pixValue = posCheck + "px"
    if(pixValue == imageSize + "px") {
        return
    }else{
        gallery.style.transform = `translateY(${pixValue})`
        check.value -= imageSize
    }
});

const buttons = document.querySelectorAll(".satisfied-client span");
const scrollingContainer = document.querySelector(
    ".satisfied-client-container"
    );
    buttons.forEach((button) => {
        button.addEventListener("click", (e) => {
        if (e.target.className === "right") {
            scrollingContainer.scrollBy(240, 0);
        } else if (e.target.className === "left") {
            scrollingContainer.scrollBy(-240, 0);
        }
    });
});





