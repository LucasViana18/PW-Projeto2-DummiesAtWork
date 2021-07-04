let isDark = true;
function theme(){
    if(isDark === true){
        document.querySelector("#colorTheme").innerHTML = "Dark Theme";
        document.querySelector("#colorTheme").classList.remove("btn-light");
        document.querySelector("#colorTheme").classList.add("btn-dark");
        document.querySelectorAll("h1").forEach(h1 => {
            h1.style.color = "black";
        })
        document.querySelectorAll("p").forEach(p => {
            p.style.color = "black";
        })
        document.querySelectorAll("figcaption").forEach(h1 => {
            h1.style.color = "black";
        })
        document.querySelector("body").style.background = "white";

        isDark = false;
    }
    else{
        document.querySelector("#colorTheme").innerHTML = "Light Theme";
        document.querySelector("#colorTheme").classList.remove("btn-dark");
        document.querySelector("#colorTheme").classList.add("btn-light");
        document.querySelectorAll("h1").forEach(h1 => {
            h1.style.color = "white";
        })
        document.querySelectorAll("p").forEach(p => {
            p.style.color = "white";
        })
        document.querySelectorAll("figcaption").forEach(h1 => {
            h1.style.color = "white";
        })
        document.querySelector("body").style.background = "black";
        isDark = true;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("#colorTheme").onclick = theme;
})

function showPage(page) {
    document.querySelectorAll('div[class*="singlePageContent"]').forEach(div => {
        div.style.display = 'none';
    });
    document.querySelectorAll(`div[class*="${page}"]`).forEach(div => {
        div.style.display = 'block';
    });
};

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('button[class*="pageSelector"]').forEach(button => {
        button.onclick = function() {
            showPage(this.dataset.page);
        }
    });
});