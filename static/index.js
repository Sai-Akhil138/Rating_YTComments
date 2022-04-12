const youtubeId = document.getElementById("youtubeId")
const submit = document.getElementById('submit')
const load = document.getElementById('loading')
const rating = document.getElementById('rating')

submit.addEventListener('click', function (e) {
    e.preventDefault()
    // Displaying Loading Message
   load.style.display = "block";
   rating.style.display = "none"
   document.getElementById("content_container").style.opacity = "0.25";

    var ulPrev = document.getElementById("comments")
    if(ulPrev)ulPrev.remove()

    setTimeout(function(){
        fetch('/get-comments?youtube-id='+youtubeId.value)
    .then(res => res.json())
    .then(data => {
        var ul = document.createElement('ul')
        ul.id = "comments"
        document.getElementById('rating__allList').appendChild(ul);
        var comments = document.getElementById('dropdown-comments')
        var value = comments.options[comments.selectedIndex].value;
        console.log(value)
        if(value == 'all'){
            for (let i =0; i<=data.items.length;i++){
                var li=document.createElement('li');
                ul.appendChild(li);
                li.innerHTML=li.innerHTML + data.items[i].snippet.topLevelComment.snippet.textOriginal;
                load.style.display = "none";
                document.getElementById("content_container").style.opacity = "1";
                rating.style.display = "block"
            }
        }else if(value == 'top100'){
            for (let i =0; i<10;i++){
                var li=document.createElement('li');
                ul.appendChild(li);
                li.innerHTML=li.innerHTML + data.items[i].snippet.topLevelComment.snippet.textOriginal;
                load.style.display = "none";
                document.getElementById("content_container").style.opacity = "1";
                rating.style.display = "block"
            }
        }else if(value == 'top50'){
            for (let i =0; i<5;i++){
                var li=document.createElement('li');
                ul.appendChild(li);
                li.innerHTML=li.innerHTML + data.items[i].snippet.topLevelComment.snippet.textOriginal;
                load.style.display = "none";
                document.getElementById("content_container").style.opacity = "1";
                rating.style.display = "block"
            }
        }

    })
    .catch(err => console.log(err))
    },3000)
    
})



