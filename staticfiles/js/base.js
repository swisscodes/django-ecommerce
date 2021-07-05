const burgerButton = document.querySelector(".burger-button");
const linkMenu = document.querySelector(".link-menu");
const categoryMenu = document.querySelector(".category-wrapper");


function burgerClick() {
    burgerButton.onclick = (e) => {
        e.preventDefault();
        burgerButton.classList.toggle("is-active");
        linkMenu.classList.toggle("drop-in");
    };
}burgerClick();


function categoryMenuclick(){
    categoryMenu.onclick = (e) => {
    // e.preventDefault();
    // e.stopPropagation();
    let categoryDisplay = document.querySelector(".category-drop-div");
    categoryDisplay.classList.toggle("menu-display");
    // setTimeout(()=> {
    //     categoryDisplay.classList.toggle("menu-display");  
    // }, 5000);
    };
}categoryMenuclick();


// function categoryMenuOut(){
//     categoryMenu.onmouseout = (e) => {
//     e.preventDefault();
//     let categoryDisplay = document.querySelector(".category-drop-div");
//     categoryDisplay.classList.toggle("menu-display");
//     };
// }categoryMenuOut();