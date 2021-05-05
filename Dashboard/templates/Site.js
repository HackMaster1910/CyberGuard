var logoutbtn = document.getElementById("logoutbtn");

logoutbtn.onclick = function () {
    document.cookie = "session=[LoggedOut]"
};