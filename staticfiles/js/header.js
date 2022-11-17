
const headerButton = document.querySelector('.sp-br');

headerButton.addEventListener('click', () => {
    const navigation = document.querySelector('.navigation');
    const bars = document.querySelector('.bars');
    bars.classList.toggle('bar-color');
    navigation.classList.toggle('nav');
});