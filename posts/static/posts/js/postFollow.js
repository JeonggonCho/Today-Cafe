// post 페이지 내의 리뷰작성자 팔로우
const form = document.querySelector('#follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

form.addEventListener('submit', function (event) {
    // 이벤트 기본 동작 취소
    event.preventDefault()

    const userId = event.target.dataset.userId
    axios({
        method: 'post',
        url: `/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken},
    })
    .then((response) => {
        // console.log(response.data)
        const isFollowed = response.data.is_followed
        const followBtn = document.querySelector('#follow-form > input[type=submit]')

        if (isFollowed === true) {
            followBtn.value = '언팔로우'
        } else {
            followBtn.value = '팔로우'
        }
        })
    })
