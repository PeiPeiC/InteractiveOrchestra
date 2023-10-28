document.querySelector('.wheel').addEventListener('mousemove', function(event) {
    let rect = this.getBoundingClientRect();
    let x = event.clientX - (rect.left + rect.width / 2);
    let y = event.clientY - (rect.top + rect.height / 2);
    let angle = Math.atan2(y, x) * (180 / Math.PI);
    document.querySelector('.logo').style.transform = `rotate(${angle}deg)`;
  });
function openCamera() {
    var cameraWindow = window.open('{% url "hand_tracking_camera" %}', 'camera', 'width=640,height=480')
  }