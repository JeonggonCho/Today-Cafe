// post 페이지 좋아요 비동기 처리
const forms = document.querySelectorAll('.like-forms')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

forms.forEach((form) => {
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const postId = event.target.dataset.postId
        axios({
            method: 'post',
            url: `http://127.0.0.1:8000/posts/${postId}/likes/`,
            headers: {'X-CSRFToken': csrftoken},
        })
            .then((response) => {
                const isLiked = response.data.is_liked
                const likeBtn = document.querySelector(`#like-${postId}`)
                if (isLiked === true) {
                    likeBtn.className.add('post--unlike_btn');
                } else {
                    likeBtn.className.add('post--like_btn');
                }
            })
            .catch((error) => {
                console.log(error.response)
            })
    })
})