// 기본 세팅 (지도 표시 세팅)
var container = document.getElementById('map');
var options = {
    center: new kakao.maps.LatLng(37.54, 126.96), //지도의 중심좌표 (구글맵 켜고 특정 위치 찍으면 위도 경도 표시됨)
    level: 8 //지도의 레벨(확대, 축소 정도, 지도에 한번에 보이는 화면)
};

//지도 생성 및 객체 리턴
var map = new kakao.maps.Map(container, options); 

// 지도 우측 줌 컨트롤러
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

//더미데이터
const dataSet = [
    {
      title: "희락돈까스",
      address: "서울 영등포구 양산로 210",
      category: "양식",
    },
    {
      title: "즉석우동짜장",
      address: "서울 영등포구 대방천로 260",
      category: "한식",
    },
    {
      title: "아카사카",
      address: "서울 서초구 서초대로74길 23",
      category: "일식",
    },
  ];

//주소 기반으로 여러개 마커 표시하기
// 주소-좌표 변환 객체 (반복문 이전에 선언 필요)
// 주소 - 좌표 변환 함수 (비동기 문제 발생 해결) ****************
// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();
function getCoordsByAddress(address) {
  // promise 형태로 반환
  return new Promise((resolve, reject) => {
    // 주소로 좌표를 검색합니다
    geocoder.addressSearch(address, function (result, status) {
      // 정상적으로 검색이 완료됐으면
      if (status === kakao.maps.services.Status.OK) {
        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
        return resolve(coords);
      }
      reject(new Error("getCoordsByAddress Error: not valid Address"));
    });
  });
}

setMap();

function getContent(data) {
    // 인포 윈도우 가공
    return `
    <div class="p-1">    
        <span class="fw-bold mx-auto">${data.title}</span>
    </div>`
}

async function setMap() {
  for (var i = 0; i < dataSet.length; i++) {
    let coords = await getCoordsByAddress(dataSet[i].address);
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
      map: map, // 마커를 표시할 지도
      // position: positions[i].latlng, // 마커를 표시할 위치
      position: coords,
      // title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
    })
    // 마커에 표시할 인포윈도우를 생성합니다 
    var infowindow = new kakao.maps.InfoWindow({
        content: getContent(dataSet[i]), // 인포윈도우에 표시할 내용
    });
    infowindowArray.push(infowindow)

    // 마커에 mouseover 이벤트와 mouseout 이벤트를 등록합니다
    // 이벤트 리스너로는 클로저를 만들어 등록합니다 
    // for문에서 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다
    kakao.maps.event.addListener(marker, 'click', makeOverListener(map, marker, infowindow, coords));
    kakao.maps.event.addListener(map, 'click', makeOutListener(infowindow));
  }
}

// 인포윈도우를 표시하는 클로저를 만드는 함수입니다 
// 클릭 시 다른 윈도우 닫기 & 클릭한 곳으로 지도 중심 옮기기
function makeOverListener(map, marker, infowindow, coords) {
    return function() {
        closeInfiWindow()
        infowindow.open(map, marker)
        map.panTo(coords)
    };
}

let infowindowArray = []
function closeInfiWindow() {
    for (let infowindow of infowindowArray) {
        infowindow.close()
    }
}
// 인포윈도우를 닫는 클로저를 만드는 함수입니다 
function makeOutListener(infowindow) {
    return function() {
        infowindow.close();
    };
}