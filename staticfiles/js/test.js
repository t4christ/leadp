
const bar = document.querySelector('.bar');
const nav = document.querySelector('.nav-links');
const navCtrl = document.querySelector('.nav-ctrl');


window.onload = () => {
    console.log('loaded');
    bar.addEventListener('click', () => {
        nav.classList.toggle('disp'); 
});
};
