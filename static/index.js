const youtubeId = document.getElementById("youtubeId")
const submit = document.getElementById('submit')
const load = document.getElementById('loading')

submit.addEventListener('click', function (e) {
    e.preventDefault()
    // Displaying Loading Message
   load.style.display = "block";
   document.getElementById("content_container").style.opacity = "0.25";

    // Getting Comments id to remove or display comments
    var ulOnePrev = document.getElementById("top_comments")
    var ulTwoPrev = document.getElementById("least_comments")
    if(ulOnePrev)ulOnePrev.remove()
    if(ulTwoPrev)ulTwoPrev.remove()
    setTimeout(function(){
        fetch('/get-comments?youtube-id='+youtubeId.value)
    .then(res => res.json())
    .then(data => {
        var ulOne = document.createElement('ul')
        var ulTwo = document.createElement('ul')
        ulOne.id = "top_comments"
        ulTwo.id = "least_comments"
        document.getElementById('rating__topList').appendChild(ulOne);
        document.getElementById('rating__leastList').appendChild(ulTwo);
        for (let i =0; i<=4;i++){
            var li=document.createElement('li');
            ulOne.appendChild(li);
            li.innerHTML=li.innerHTML + data.items[i].snippet.topLevelComment.snippet.textOriginal;
        }
        for (let i =data.items.length-1; i>=data.items.length-5; i--){
            var li=document.createElement('li');
            ulTwo.appendChild(li);
            li.innerHTML=li.innerHTML + data.items[i].snippet.topLevelComment.snippet.textOriginal;
        }
        load.style.display = "none";
        document.getElementById("content_container").style.opacity = "1";
        document.querySelectorAll(".comments_box").style.boxShadow = "0px 4px 8px rgba(0,0,0,0.25)"

    })
    .catch(err => console.log(err))
    },3000)
    
})



