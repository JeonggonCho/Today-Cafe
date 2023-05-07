// post 페이지의 리뷰 좋아요 비동기 처리
const reviewForms = document.querySelectorAll('.review-like-forms')
const reviewCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

reviewForms.forEach((form) => {
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const postId = event.target.dataset.postId
        const reviewId = event.target.dataset.reviewId
        axios({
            method: 'post',
            url: `http://127.0.0.1:8000/posts/${postId}/reviews/${reviewId}/likes/`,
            headers: {'X-CSRFToken': reviewCsrftoken},
        })
            .then((response) => {
                const isLiked = response.data.is_liked
                const likeBtn = document.querySelector(`#like-${postId}-${reviewId}`)
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