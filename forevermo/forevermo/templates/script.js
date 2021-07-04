function togglePane() { 
        if (this.checked) {
                document.getElementById("plusOnePane").style.display = 'block';
        } else {
                document.getElementById("plusOnePane").style.display = 'none';
        }
}

document.getElementById("plusOneCheck").onclick = togglePane;