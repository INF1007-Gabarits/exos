const onDirClick = function(dir) {
    dir.classList.toggle("open");
}

window.onload = function () {

  directories = document.getElementsByClassName('dir');
  for(let d=0; d < directories.length; d++) {
    let dir = directories[d];
    dir.onclick = function() { onDirClick(dir); }
  }
  
}