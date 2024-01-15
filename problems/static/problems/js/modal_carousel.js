let myCarousel = document.querySelector('#carouselExampleControls')
let myModalEl = document.getElementById('exampleModal')

myModalEl.addEventListener('show.bs.modal', function (event) {
    const trigger = event.relatedTarget
    let bsCarousel = bootstrap.Carousel.getInstance(myCarousel)
    bsCarousel.to(trigger.dataset.bsSlideTo)
})
