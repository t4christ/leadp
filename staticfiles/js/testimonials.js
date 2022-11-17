const gallery = document.querySelector('.gallery');
const galleryContainer = document.querySelector('.gallery-container');
const images = document.querySelectorAll('.images');

console.log(galleryContainer.clientWidth);

//The buttons
const pre = document.querySelector('#pre');
const nex = document.querySelector('#nex');

console.log(images.length);
console.log(images[0].clientWidth);
let a = 0;
pre.style.visibility = "hidden";

nex.onclick = ()=>{  
    a = a - images[0].clientWidth;
    
           galleryContainer.style.transitionDuration = 0.4 + "s";
           galleryContainer.style.left = a + "px";
           if(a === (-(images.length - 1) * images[0].clientWidth)){
               nex.style.visibility = "hidden";
           }else{
               pre.style.visibility = "visible";
           }
           console.log(a);
        }

pre.onclick = ()=>{
            a = a + images[0].clientWidth;
            galleryContainer.style.left = a + "px";
            if(a === 0){
                pre.style.visibility = "hidden";
            }else{
                nex.style.visibility = "visible";
            }
            console.log(a);
}